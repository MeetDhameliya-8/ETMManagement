from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Screensite pages (login, signup, etc.)
    path('', include('Screensite.urls')),

    # Projects app URLs start with /Projects/
    path('Projects/', include(('Projects.urls', 'Projects'), namespace='Projects')),
]





