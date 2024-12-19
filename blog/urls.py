from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf.urls.static import static

from blog import settings

urlpatterns = [
    path('miniblog/', include('miniblog.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/miniblog/', permanent=True)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)