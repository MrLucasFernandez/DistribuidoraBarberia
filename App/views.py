from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .forms import ContactForm, ProductForm
from django.contrib import messages
from .models import Producto, Contacto
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import Http404
from App.cart import Cart
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from .serializer import UsuariosSerializer
from rest_framework.response import Response


# Create your views here.

#Inicio
def home (request):
    return render(request, 'app/home.html') 

#Contacto
def contact (request):
    return render(request, 'app/contact.html')

#Productos
def products (request):
    productos = Producto.objects.filter(cantidad__gt=0)
    
    return render(request, 'app/products.html', {'productos':productos})

#Reserva
def buy (request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    
    data={
        'entity':productos,
        'paginator':paginator
    }
    return render(request, 'app/buy.html', data)

#Vista registro
def register(request):
    return render(request, 'registration/register.html')

#Añadir usuario
@api_view(["POST"])
def usuarioAdd(request):
    serializer = UsuariosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return render(request, 'app/home.html')


#Login
def logIn(request):
    return render(request, 'accounts/login.html')

#Contacto
def contact(request):
    data = {
        'form': ContactForm()
    }
    if request.method == 'POST':
        formulario = ContactForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Formulario enviado")
        else:
            data['form'] = formulario
    return render(request, 'app/contact.html', data)

#Agregar Servicio
@permission_required('app.add_servicio')
def add (request):
    data = {
        'form': ProductForm()
    }
    if request.method == 'POST':
        formulario = ProductForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado correctamente")
        else:
            data['form'] = formulario
    return render(request, 'app/crud/add.html', data)

#Listar
@permission_required('app.view_producto')
@permission_required( 'app.view_contacto')
def list(request):
    contactos = Contacto.objects.all()
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    
    data={
        'entity':productos,
        'entity2':contactos,
        'paginator':paginator
    }
    return render(request, 'app/crud/list.html', data)

#Modificar

@permission_required('app.change_producto')
def modify(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductForm(instance=producto), 'id': id
    }    
    if request.method == 'POST':
        formulario = ProductForm(data=request.POST,instance=producto ,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modficado correctamente")
            return redirect(to="list")
        else:
            data['form'] = formulario
    return render(request, 'app/crud/modify.html', data)

#Eliminar
@permission_required('app.delete_producto')
def delete(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Producto eliminado correctamente")
    return redirect(to="list")


#Carrito
def add_product(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.add_product(producto)
    return redirect("buy")

def delete_product(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.delete_product(producto)
    return redirect("buy")

def subtract_product(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.subtract(producto)
    return redirect("buy")

def clean_cart(request):
    cart = Cart(request)
    cart.clean()
    return redirect("buy")