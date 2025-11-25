from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Screensite URLs (login, signup, home, apply)
    path('', include('Screensite.urls')),

    # Manager / Product app URLs
    path('manager/', include('Projects.urls', namespace='Projects')),

    # If you actually have an app named Projects, keep this:
    path('Projects/', include('Projects.urls')),
]

