from django.db import models

class categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey(
        marca, 
        on_delete=models.CASCADE,
        related_name='productos',
        null=True,
        blank=True)
    categoria = models.ForeignKey(
        categoria, 
        on_delete=models.CASCADE,
        related_name='productos')
    

    def __str__(self):
        return f'{self.categoria.nombre}: {self.nombre} ({self.marca.nombre}) - {self.precio}'