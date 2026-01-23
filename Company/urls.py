from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Screensite pages (login, signup, etc.)
    path('', include('Screensite.urls')),

    # For communication
    path('interactions/', include('Interactions.urls')),

    # Projects app URLs start with /Projects/
    path('Projects/', include(('Projects.urls', 'Projects'), namespace='Projects')),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

