from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('employees/', include('employees.urls')),
    path('coding/', include('coding.urls')),
    path('tools/', include('tools.urls')),
    path('designations/', include('designations.urls')),
    path('projects/', include('projects.urls')),
    path('resume-generator/', include('resume_generator.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
