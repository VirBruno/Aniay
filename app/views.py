from datetime import date

from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import Proveedor, Juguete, Usuario


def home(request):
    """
    Vista para mostrar la página de inicio.
    """
    juguetes = Juguete.objects.all()
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('proveedores_repo')  # vista admin
        else:
            return render(request, 'home.html', {'juguetes': juguetes})  # vista cliente
    else:
        return render(request, 'home.html', {'juguetes': juguetes})  # cliente sin login
    """juguetes = Juguete.objects.all()  # o filtro si querés algunos específicos
    return render(request, 'home.html', {'juguetes': juguetes}) CÓDIGO ANTERIOR"""


def proveedores_repository(request):
    """
    Vista para mostrar el repositorio de proveedores.
    """
    proveedores = Proveedor.objects.all()
    return render(request, "proveedores/repository.html", {"proveedores": proveedores})


def proveedores_form(request, id=None):
    """
    Vista para mostrar y procesar el formulario de usuario.

    Esta vista maneja la presentación y el procesamiento del formulario de proveedor.
    Si se recibe una solicitud POST, la vista intenta guardar o actualizar el proveedor
    según los datos recibidos. Si se recibe una solicitud GET, la vista muestra el formulario
    para crear un nuevo proveedor o para actualizar uno existente, según el parámetro 'id'.
    """
    if request.method == "POST":
        proveedor_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if proveedor_id == "":
            saved, errors = Proveedor.save_proveedor(request.POST)
        else:
            proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
            saved, errors = proveedor.update_proveedor(request.POST)

        if saved:
            return redirect(reverse("proveedores_repo"))

        return render(
            request, "proveedores/form.html", {"errors": errors, "proveedor": request.POST},
        )

    proveedor = None
    if id is not None:
        proveedor = get_object_or_404(Proveedor, pk=id)

    return render(request, "proveedores/form.html", {"proveedor": proveedor})


def proveedores_delete(request):
    """
    Vista para eliminar un proveedor.

    Esta vista elimina un proveedor de la base de datos según el ID proporcionado en la solicitud POST.
    """
    proveedor_id = request.POST.get("proveedor_id")
    proveedor = get_object_or_404(Proveedor, pk=int(proveedor_id))
    proveedor.delete()

    return redirect(reverse("proveedores_repo"))

def juguetes_repository(request):
    """Vista para mostrar el repositorio de juguetes.

    Esta vista obtiene todas las jugutes de la base de datos y las pasa a la plantilla
    'juguetes/repository.html' para su renderizado.
    """
    juguetes = Juguete.objects.all()
    return render(request, "juguetes/repository.html", {"juguetes": juguetes})

def juguetes_form(request, id=None):
    today = date.today().strftime('%Y-%m-%d')
    proveedores = Proveedor.objects.all()   # <-- faltaba

    if request.method == "POST":
        juguete_id = request.POST.get("id", "")
        proveedor_id = request.POST.get("proveedor")
        proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
        image = request.FILES.get("image")

        if juguete_id == "":
            juguete = Juguete.objects.create(
                name=request.POST["name"],
                brand=request.POST["brand"],
                description=request.POST["description"],
                price=request.POST["price"],
                proveedor=proveedor,
                image=request.FILES.get("image")
                
            )
        else:
            juguete = get_object_or_404(Juguete, pk=juguete_id)
            juguete.name = request.POST["name"]
            juguete.brand = request.POST["brand"]
            juguete.description = request.POST["description"]
            juguete.price = request.POST["price"]
            juguete.proveedor = proveedor
            juguete.image=request.FILES.get("image")

        return redirect("juguetes_repo")

    juguete = None
    if id is not None:
        juguete = get_object_or_404(Juguete, pk=id)

    return render(request, "juguetes/form.html", {
        "juguete": juguete,
        "today": today,
        "proveedores": proveedores,})

    juguete = None
    if id is not None:
        juguete = get_object_or_404(Juguete, pk=id)
        
    return render(request, "juguetes/form.html", {"juguete": juguete, "today": today})

def juguetes_delete(request):
    """
    Vista para eliminar una juguete.

    Esta vista elimina una juguete de la base de datos según el ID proporcionado en la solicitud POST.
    """
    juguete_id = request.POST.get("juguete_id")
    juguete = get_object_or_404(Juguete, pk=int(juguete_id))
    juguete.delete()

    return redirect(reverse("juguetes_repo"))

def nuevo_juguete(request):
    if request.method == 'POST':
        form = JugueteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_juguetes')
    else:
        form = JugueteForm()
    return render(request, 'juguetes_form.html', {'form': form})

def usuarios_repository(request):
    """
    Vista para mostrar el repositorio de usuarios.
    """
    usuarios = Usuario.objects.all()
    return render(request, "usuarios/repository.html", {"usuarios": usuarios})


def usuarios_form(request, id=None):
    """
    Vista para mostrar y procesar el formulario de usuario.

    Esta vista maneja la presentación y el procesamiento del formulario de usuario.
    Si se recibe una solicitud POST, la vista intenta guardar o actualizar el usuario
    según los datos recibidos. Si se recibe una solicitud GET, la vista muestra el formulario
    para crear un nuevo usuario o para actualizar uno existente, según el parámetro 'id'.
    """
    if request.method == "POST":
        usuario_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if usuario_id == "":
            saved, errors = Usuario.save_usuario(request.POST)
        else:
            usuario = get_object_or_404(Usuario, pk=usuario_id)
            saved, errors = Usuario.update_usuario(request.POST)

        if saved:
            return redirect(reverse("usuarios_repo"))

        return render(
            request, "usuarios/form.html", {"errors": errors, "usuario": request.POST},
        )

    usuario = None
    if id is not None:
        usuario = get_object_or_404(Usuario, pk=id)

    return render(request, "usuarios/form.html", {"usuario": usuario})


def usuarios_delete(request):
    """
    Vista para eliminar un usuario.

    Esta vista elimina un usuario de la base de datos según el ID proporcionado en la solicitud POST.
    """
    usuario_id = request.POST.get("usuario_id")
    usuario = get_object_or_404(Usuario, pk=int(usuario_id))
    usuario.delete()

    return redirect(reverse("usuarios_repo"))