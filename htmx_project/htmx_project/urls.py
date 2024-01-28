from django.contrib import admin
from django.urls import include, path
from htmx_app.urls import drf_urlpatterns
from htmx_app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.HomepageView.as_view(), name='homepage'),
    path('htmx_test/', views.HtmxTestView.as_view(), name='htmx_test'),
] + drf_urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
