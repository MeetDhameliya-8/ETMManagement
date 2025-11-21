

# Create your views here.
# Create your views here.
from django.shortcuts import redirect, render,get_object_or_404, HttpResponse
from .models import Project, Task
from .decorators import manager_required
from django.contrib.auth.decorators import login_required
from Profile.models import EmployeeProfile, User
 

def manager_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role != "MG":
            return redirect("Screensite:home")  # or error page
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

        return redirect("Project:assign_members", project_id=project.id)

    return render(request, "Project/create_project.html")






@manager_required
def manager_dashboard(request):
    projects = Project.objects.filter(manager=request.user)
    return render(request, "Project/manager_dashboard.html", {"projects": projects})






@login_required
def my_projects(request):
    projects = request.user.assigned_projects.all()
    return render(request, "ProjectApp/my_projects.html", {"projects": projects})






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

    return render(request, "Project/assign_members.html", {
        "project": project,
        "employees": employees,
    })





@manager_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project=project)

    return render(request, "Project/project_detail.html", {
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
        return redirect("Project:project_detail", project_id=project.id)

    return render(request, "Project/add_task.html", {
        "project": project
    })



''' well right now inside subproject folder there is app Project
inside teplates/project these templates exist
- add_task, assign_members, bash_dashboard,create_project,assign_members, project_detail,project_card and then in static/project/css there is one template manager_dashboard.css and inside complete another folder there 
is a bash_dashboard.html exist which is name is screensite and that is not app with __init__ files that's how things are '''
