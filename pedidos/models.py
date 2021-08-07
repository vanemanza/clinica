from django.db import models
from pacientes.models import Pacientes
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

class Categoria(models.Model):

    TIPOS = (
    ('lentes', 'lentes'),
    ('armazones', 'armazones'),
    ('ortóptica', 'ortóptica'),
    ('accesorios', 'accesorios'),
    )

    tipos = models.CharField(max_length=20, choices=TIPOS, verbose_name="categorias")
   
    class Meta:

        verbose_name="categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.tipos

class Productos(models.Model):
    
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to="pedidos", null=True, blank=True)   
    precio = models.FloatField()    
    stock = models.IntegerField(default=1, null=True)

    class Meta:

        verbose_name= "producto"
        verbose_name_plural="productos"    



class Pedidos(models.Model):

    ESTADOS = (
    ('pendiente', 'pendiente'),
    ('pedido', 'pedido'),
    ('taller', 'taller'),
    ('finalizado', 'finalizado'),
    )

    FORMAS_PAGO = (
        ('tarjeta', 'tarjeta'),
        ('efectivo', 'efectivo'),
        ('debito', 'debito'),
    )

    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)   
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE) 
    precio = models.FloatField()
    cantidad = models.IntegerField()    
    forma_pago = models.CharField(max_length=20, default='tarjeta', choices=FORMAS_PAGO,
        verbose_name='Forma de pago')    
    estado = models.CharField(max_length=1, default='pendiente', choices=ESTADOS,
        verbose_name="Estado")
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        
