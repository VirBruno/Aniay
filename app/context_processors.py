from django.urls import reverse

links = [
    {"label": "Home", "href": reverse("home"), "icon": "bi bi-house-door"},
    {"label": "Proveedores", "href": reverse("proveedores_repo"), "icon": "bi bi-people"},
    {"label": "Juguetes", "href": reverse("juguetes_repo"), "icon": "bi bi-puzzle"},
    {"label": "Carrito", "href": reverse("juguetes_repo"), "icon": "bi bi-cart"},
    {"label": "Login", "href": reverse("login"), "icon": "bi bi-key"},
 
]

def navbar(request):
    """Genera los enlaces de la barra de navegación activos basados en la solicitud.
    """
    def add_active(link):
        copy = link.copy()

        if copy["href"] == "/":
            copy["active"] = request.path == "/"
        else:
            copy["active"] = request.path.startswith(copy.get("href", ""))

        return copy

    return {"links": map(add_active, links)}

def home_items(request):
    """ Genera los elementos para mostrar en la página de inicio.
    """
    items = [
     {"label": "Proveedores", "href": reverse("proveedores_repo"), "icon": "bi bi-people"},
    {"label": "Juguetes", "href": reverse("juguetes_repo"), "icon": "bi bi-puzzle"},
    
    ]
    return {"home_items": items}
