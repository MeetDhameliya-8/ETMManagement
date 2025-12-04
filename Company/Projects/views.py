

# Create your views here.
# Create your views here.
from django.shortcuts import redirect, render,get_object_or_404, HttpResponse
from .models import Project, Task
from .decorators import manager_required
from django.contrib.auth.decorators import login_required
from Profile.models import EmployeeProfile, User
from functools import wraps
from .models import Project







def manager_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('Screensite:login')

        # normalize role and check
        role = str(getattr(request.user, 'role', '')).upper().strip()
        if role not in ('MG', 'MANAGER'):
            return redirect('Screensite:home')   # redirect non-managers to home (not to dashboard)

        return view_func(request, *args, **kwargs)
    return wrapper






  # if you save decorator there
@login_required(login_url='/Screensite/login/')
def create_project(request):
    if request.user.role != "MG":
        return HttpResponse("Unauthorized")

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")

        project = Project.objects.create(
            title=title,
            description=description,
            deadline=deadline,
            manager=request.user
        )

        return redirect("project:assign_members", project_id=project.id)

    return render(request, "project/create_project.html")






@manager_required
def manager_dashboard(request):
    projects = Project.objects.filter(manager=request.user)
    return render(request, "Projects/manager_dashboard.html", {"projects": projects})







# Projects/views.py


@login_required(login_url='Screensite:login')
def my_projects(request):
    # show projects where the current user is manager OR part of team — adjust as needed
    projects = Project.objects.filter(manager=request.user).prefetch_related('team_members')
    return render(request, "Projects/my_projects.html", {"projects": projects})







@manager_required
def assign_members(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Fetch only employees (not managers, not interns)
    employees = User.objects.filter(role="Emp")

    if request.method == "POST":
        selected_members = request.POST.getlist("members")

        project.team_members.set(selected_members)
        project.save()

        return redirect("manager_dashboard")

    return render(request, "Projects/assign_members.html", {
        "project": project,
        "employees": employees,
    })





@manager_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project=project)

    return render(request, "projects/project_detail.html", {
        "project": project,
        "tasks": tasks,
    })




@manager_required
def add_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        status = request.POST.get("status")

        Task.objects.create(
            project=project,
            title=title,
            description=description,
            status=status
        )

        # IMPORTANT: After success, redirect to project detail
        return redirect("project:project_detail", project_id=project.id)

    return render(request, "projects/add_task.html", {
        "project": project
    })




