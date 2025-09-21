from django.contrib import admin
from django.urls import path

from . import views
from django.conf import settings

from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("proveedores/", view=views.proveedores_repository, name="proveedores_repo"),
    path("proveedores/nuevo/", view=views.proveedores_form, name="proveedores_form"),
    path("proveedores/editar/<int:id>/", view=views.proveedores_form, name="proveedores_edit"),
    path("proveedores/eliminar/", view=views.proveedores_delete, name="proveedores_delete"),
    path("juguetes/", view=views.juguetes_repository, name="juguetes_repo"),
    path("juguetes/nuevo/", view=views.juguetes_form, name="juguetes_form"),
    path("juguetes/editar/<int:id>/", view=views.juguetes_form, name="juguetes_edit"),
    path("juguetes/eliminar/", view=views.juguetes_delete, name="juguetes_delete"),
    path("usuarios/", view=views.usuarios_repository, name="usuarios_repo"),
    path("usuarios/nuevo/", view=views.usuarios_form, name="usuarios_form"),
    path("usuarios/editar/<int:id>/", view=views.usuarios_form, name="usuarios_edit"),
    path("usuarios/eliminar/", view=views.usuarios_delete, name="usuarios_delete"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
