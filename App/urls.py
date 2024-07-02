from django.urls import path
from .views import home, contact, products, buy, logIn, register, add, list, modify, delete, add_product, delete_product, subtract_product, clean_cart, usuarioAdd
                

#Para subir imagenes 
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contact, name='contact'),
    path('productos/', products, name='products'),
    path('comprar/', buy, name='buy'),
    path('login/', logIn, name='login'),
    path('registro/', register, name='register'),
    path('usuarioAdd/',usuarioAdd, name='usuarioAdd'),
    path('agregar/', add, name="add"),   
    path('listar/', list, name="list"),   
    path('modificar/<id>/', modify, name="modify"),
    path('eliminar/<id>/', delete, name="delete"),
    path('añadir/<int:producto_id>/', add_product, name="add_product"),
    path('borrar/<int:producto_id>/', delete_product, name="delete_product"),
    path('restar/<int:producto_id>/', subtract_product, name="subtract_product"),
    path('limpiar/', clean_cart, name="clean_cart"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
