from django.db import models

# Create your models here.
#Clase Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    
    def __str__(self):
        return self.nombre

#Clase tipo consulta
class TipoConsulta(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    
    def __str__(self):
        return self.nombre

#Clase Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name="Categoria")
    descripcion = models.CharField(max_length=150, verbose_name="Descripción")
    imagen = models.ImageField(upload_to='img/productos', verbose_name="Imagen del producto", null=True)
    precio =  models.IntegerField(verbose_name="Precio")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    def __str__(self):
        return self.nombre
    
    #Borrar imagenes desde el admin
    def delete(self, using=None, keep_parent=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        
#Clase Contacto

class Contacto (models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    correo = models.EmailField(verbose_name="Correo")
    tipo_consulta = models.ForeignKey(TipoConsulta, on_delete=models.PROTECT, verbose_name="Tipo Consulta")
    mensaje = models.TextField(max_length=1000, verbose_name="Mensaje")
    avisos = models.BooleanField(verbose_name="Avisos")
    
    def __str__(self) :
        return self.nombre