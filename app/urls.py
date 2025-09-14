from django.contrib import admin
from django.urls import path

from . import views
from django.conf import settings

from django.conf.urls.static import static

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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
