

# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import CommunicationForm
from Projects.models import EmployeeUpdate


@login_required
def add_communication(request, update_id):
    update = get_object_or_404(EmployeeUpdate, id=update_id)

    if request.method == "POST":
        form = CommunicationForm(request.POST)
        if form.is_valid():
            communication = form.save(commit=False)
            communication.update = update
            communication.created_by = request.user
            communication.save()

    return redirect("employee_update")

