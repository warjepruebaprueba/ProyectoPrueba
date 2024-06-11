from django.db import models
from django.contrib.auth.models import User

class Lista(models.Model):
        
    PAGO = [
        ('Tarjeta', 'Tarjeta'),
        ('Efectivo', 'Efectivo'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=20)
    pago = models.CharField(max_length=20, choices=PAGO)
    pagado = models.BooleanField(default=False)

    
    @property
    def nombre_usuario(self):
        return self.usuario.username
    
    def __str__(self):
        return f"{self.usuario.username}"

