from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


project_patterns = [
    url(r'^exporter/', include('exporter.urls')),
    url(r'^admin/', admin.site.urls),
]

scripts = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = project_patterns + scripts
