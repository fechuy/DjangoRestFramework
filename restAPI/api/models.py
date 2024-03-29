from tabnanny import verbose
from django.db import models

# Create your models here.

class Categoria(models.Model):
    descripcion = models.CharField(max_length=255, help_text="Descripcion de la categoria", unique=True)
    def __str__(self) -> str:
        return '{}'.format(self.descripcion)
    class Meta:
        verbose_name_plural = "Categorias"

class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Sub Categoría'
    )
 
    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)
 
    class Meta:
        verbose_name_plural = "Sub Categorías"
        unique_together = ('categoria','descripcion')
 
 
class Producto(models.Model):
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción del Producto',
        unique=True
    )
    fecha_creado = models.DateTimeField()
    vendido = models.BooleanField(default=False)
 
    def __str__(self):
        return '{}'.format(self.descripcion)
 
    class Meta:
        verbose_name_plural = "Productos"