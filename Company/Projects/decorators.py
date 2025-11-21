from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def manager_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/Screensite/login/')

        if not hasattr(request.user, 'manager_profile'):
            raise PermissionDenied("Only managers can access this section.")

        return view_func(request, *args, **kwargs)

    return wrapper
