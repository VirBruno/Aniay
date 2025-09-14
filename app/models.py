import re
from datetime import datetime

from django.db import models


def validate_fields(data, required_fields):
    """
    Valida los campos de datos según los requisitos especificados.
    """
    errors = {}

    for key, value in required_fields.items():
        field_value = data.get(key, "")

        if field_value == "":
            errors[key] = f"Por favor ingrese un {value}"
        elif key == 'name':
            name_error = validate_aniay_name(field_value)
            if name_error:
                errors["name"] = name_error
        elif key == 'email':
            email_error = validate_aniay_email(field_value)
            if email_error:
                errors["email"] = email_error
        elif key == 'price' and  float(field_value) <0.0:
            errors["price"] = "El precio debe ser mayor a cero"
        elif key == 'price' and int(field_value) < 0:
            errors["price"] = "El peso de la mascota no puede ser negativo"
        elif key =='phone':
            phone_error = validate_phone(field_value)
            print(phone_error)
            if phone_error:
                errors["phone"] = phone_error
    return errors

def validate_date_of_birthday(date_str):
    """
    Valida si una fecha de nacimiento es válida y está en el formato correcto.
    """
    try:
        birth_date = datetime.strptime(date_str, '%Y-%m-%d')
        today = datetime.today()
        if birth_date > today:
            return "La fecha no puede ser mayor al dia de hoy"
        return None
    except ValueError:
        return "Formato de fecha incorrecto"
    
def validate_aniay_name(value):
    """
    Valida si un nombre contiene solo letras, espacios y caracteres especiales comunes en español.
    """
    regex = r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$'
    if not re.match(regex, value):
        return "El nombre solo debe contener letras y espacios"
    return None

def validate_phone(number):
    """
    Valida si un número de teléfono es válido y contiene solo dígitos.
    """
    if not(number.isnumeric()):
        return "El teléfono indicado debe contener sólo números"
    
    """regex = r'^54'

    if not re.match(regex, number):
        return "El teléfono debe comenzar siempre con 54"
    return None""" 
    
def validate_aniay_email(value):
    """
    Valida si una dirección de correo electrónico cumple con el formato.
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not re.match(regex, value):
        return "Por favor ingrese un email valido"

    regex = r'^[a-zA-Z0-9._%+-]+@(hotmail|gmail)\.com$'
    if not re.match(regex, value):
        return "El email debe finalizar con @hotmail.com"

    return None

class Proveedor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_required_fields():
        """
        Devuelve un diccionario que mapea los campos requeridos a sus descripciones en español."""
        return {
            "name": "nombre",
            "email": "email",
            "phone": "teléfono",
        }

    @classmethod
    def save_proveedor(cls, proveedor_data):
        """
        Crea un nuevo cliente utilizando los datos proporcionados"""
        errors = validate_fields(proveedor_data, Proveedor.get_required_fields())

        if len(errors.keys()) > 0:
            return False, errors

        Proveedor.objects.create(
            name=proveedor_data.get("name"),
            phone=proveedor_data.get("phone"),
            email=proveedor_data.get("email"),
            address=proveedor_data.get("address"),
        )

        return True, None

    def update_proveedor(self, proveedor_data):
        """
        Actualiza los datos del cliente con la información proporcionada."""
        errors = validate_fields(proveedor_data, Proveedor.get_required_fields())

        if len(errors.keys()) > 0:
            return False, errors

        self.name = proveedor_data.get("name", "") or self.name
        self.email = proveedor_data.get("email", "") or self.email
        self.phone = proveedor_data.get("phone", "") or self.phone
        self.address = proveedor_data.get("address", "")

        self.save()

        return True, None

class Juguete(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="juguetes/", null=True, blank=True)

    def __str__(self):
        return self.name

# Relación con proveedor
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,   # si se borra el proveedor, se borran sus juguetes
        related_name="juguetes"     # así podés acceder con proveedor.juguetes.all()
    )

    def __str__(self):
        return f"{self.name} ({self.proveedor.name})"

    @staticmethod
    def get_required_fields():
        """
    Devuelve un diccionario que mapea los campos requeridos a sus descripciones en español."""
        return {
            "name": "nombre",
            "brand": "marca", 
            "description": "proveedor",
            "price": "precio",
        }



    @classmethod
    def save_juguete(cls, juguete_data):
        """
        Crea una nueva mascota utilizando los datos proporcionados.
"""
        errors = validate_fields(juguete_data, Juguete.get_required_fields())

        if len(errors.keys()) > 0:
            return False, errors


        Juguete.objects.create(
            name=juguete_data.get("name"),
            brand=juguete_data.get("brand"),
            description=juguete_data.get("description"),
            price=juguete_data.get("price"),
        )

        return True, None
    
    def update_juguete(self, juguete_data):
        """
        Actualiza los datos de la mascota con la información proporcionada."""
        errors = validate_fields(juguete_data, Juguete.get_required_fields())

        if len(errors.keys()) > 0:
            return False, errors

        self.name = juguete_data.get("name", "") or self.name
        self.brand = juguete_data.get("brand", "") or self.brand
        self.description = juguete_data.get("description", "") or self.description
        self.price = juguete_data.get("price", "") or self.price

        self.save()

        return True, None
