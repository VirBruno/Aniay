from datetime import date

from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import Client, Medicine, Pet, Product, Vet


def home(request):
    """
    Vista para mostrar la página de inicio.
    """
    return render(request, "home.html")


def clients_repository(request):
    """
    Vista para mostrar el repositorio de clientes.
    """
    clients = Client.objects.all()
    return render(request, "clients/repository.html", {"clients": clients})


def clients_form(request, id=None):
    """
    Vista para mostrar y procesar el formulario de cliente.

    Esta vista maneja la presentación y el procesamiento del formulario de cliente.
    Si se recibe una solicitud POST, la vista intenta guardar o actualizar el cliente
    según los datos recibidos. Si se recibe una solicitud GET, la vista muestra el formulario
    para crear un nuevo cliente o para actualizar uno existente, según el parámetro 'id'.
    """
    if request.method == "POST":
        client_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if client_id == "":
            saved, errors = Client.save_client(request.POST)
        else:
            client = get_object_or_404(Client, pk=client_id)
            saved, errors = client.update_client(request.POST)

        if saved:
            return redirect(reverse("clients_repo"))

        return render(
            request, "clients/form.html", {"errors": errors, "client": request.POST},
        )

    client = None
    if id is not None:
        client = get_object_or_404(Client, pk=id)

    return render(request, "clients/form.html", {"client": client})


def clients_delete(request):
    """
    Vista para eliminar un cliente.

    Esta vista elimina un cliente de la base de datos según el ID proporcionado en la solicitud POST.
    """
    client_id = request.POST.get("client_id")
    client = get_object_or_404(Client, pk=int(client_id))
    client.delete()

    return redirect(reverse("clients_repo"))

def pets_repository(request):
    """Vista para mostrar el repositorio de mascotas.

    Esta vista obtiene todas las mascotas de la base de datos y las pasa a la plantilla
    'pets/repository.html' para su renderizado.
    """
    pets = Pet.objects.all()
    return render(request, "pets/repository.html", {"pets": pets})

def pets_form(request, id=None):
    """
    Vista para mostrar y procesar el formulario de mascota.

    Esta vista maneja la presentación y el procesamiento del formulario de mascota.
    """
    today = date.today().strftime('%Y-%m-%d')
    if request.method == "POST":
        pet_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if pet_id == "":
            saved, errors = Pet.save_pet(request.POST)
        else:
            pet = get_object_or_404(Pet, pk=pet_id)
            saved, errors = pet.update_pet(request.POST)

        if saved:
            return redirect(reverse("pets_repo"))

        return render(
            request, "pets/form.html", {"errors": errors, "pet": request.POST, "today": today},
        )

    pet = None
    if id is not None:
        pet = get_object_or_404(Pet, pk=id)
        pet.birthday = pet.birthday.strftime('%Y-%m-%d')

    return render(request, "pets/form.html", {"pet": pet, "today": today})

def pets_delete(request):
    """
    Vista para eliminar una mascota.

    Esta vista elimina una mascota de la base de datos según el ID proporcionado en la solicitud POST.
    """
    pet_id = request.POST.get("pet_id")
    pet = get_object_or_404(Pet, pk=int(pet_id))
    pet.delete()

    return redirect(reverse("pets_repo"))

def medicines_repository(request):
    """
    Vista para mostrar el repositorio de medicamentos.
    """
    medicines = Medicine.objects.all()
    return render(request, "medicines/repository.html", {"medicines": medicines})

def medicines_form(request, id=None):
    """
    Vista para mostrar y procesar el formulario de medicamento.
    """
    if request.method == "POST":
        medicine_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if medicine_id == "":
            saved, errors = Medicine.save_medicine(request.POST)
        else:
            medicine = get_object_or_404(Medicine, pk=medicine_id)
            saved, errors = medicine.update_medicine(request.POST)

        if saved:
            return redirect(reverse("medicines_repo"))

        return render(
            request, "medicines/form.html", {"errors": errors, "medicine": request.POST},
        )

    medicine = None
    if id is not None:
        medicine = get_object_or_404(Medicine, pk=id)

    return render(request, "medicines/form.html", {"medicine": medicine})

def medicines_delete(request):
    """
    Vista para eliminar un medicamento.

    Esta vista elimina un medicamento de la base de datos según el ID proporcionado en la solicitud POST.
    """
    medicine_id = request.POST.get("medicine_id")
    medicine = get_object_or_404(Medicine, pk=int(medicine_id))
    medicine.delete()

    return redirect(reverse("medicines_repo"))

def vets_repository(request):
    """
    Vista para mostrar el repositorio de veterinarios.
    """
    vets = Vet.objects.all()
    return render(request, "vet/repository.html", {"vets": vets})

def vets_form(request, id=None):
    """
    Vista para mostrar y procesar el formulario de veterinario.
    """
    if request.method == "POST":
        vet_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if vet_id == "":
            saved, errors = Vet.save_vet(request.POST)
        
        else:
            vet = get_object_or_404(Vet, pk=vet_id)
            saved, errors = vet.update_vet(request.POST)

        if saved:
            return redirect(reverse("vets_repo"))

        return render(
            request, "vet/form.html", {"errors": errors, "vet": request.POST},
        )

    vet = None
    if id is not None:
        vet = get_object_or_404(Vet, pk=id)

    return render(request, "vet/form.html", {"vet": vet})

def vets_delete(request):
    """
    Vista para eliminar un veterinario.
    """
    vet_id = request.POST.get("vet_id")
    vet = get_object_or_404(Vet, pk=int(vet_id))
    vet.delete()

    return redirect(reverse("vets_repo"))

def products_repository(request):
    """
    Vista para mostrar el repositorio de productos.

    Esta vista obtiene todos los productos de la base de datos y los pasa a la plantilla
    'products/repository.html' para su renderizado.
    """
    products = Product.objects.all()
    return render(request, "products/repository.html", {"products": products})


def products_form(request, id=None):
    """
    Vista para mostrar y procesar el formulario de producto.

    Esta vista maneja la presentación y el procesamiento del formulario de producto.
    """
    if request.method == "POST":
        product_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if product_id == "":
            saved, errors = Product.save_product(request.POST)
        else:
            product = get_object_or_404(Product, pk=product_id)
            saved, errors = product.update_product(request.POST)

        if saved:
            return redirect(reverse("products_repo"))

        return render(
            request, "products/form.html", {"errors": errors, "product": request.POST},
        )

    product = None
    if id is not None:
        product = get_object_or_404(Product, pk=id)

    return render(request, "products/form.html", {"product": product})


def products_delete(request):
    """
    Vista para eliminar un producto.

    Esta vista elimina un producto de la base de datos según el ID proporcionado en la solicitud POST.
    """
    product_id = request.POST.get("product_id")
    product = get_object_or_404(Product, pk=int(product_id))
    product.delete()

    return redirect(reverse("products_repo"))
