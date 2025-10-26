from django.db import models

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre_marca = models.CharField(max_length=100)
    contacto_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_email = models.EmailField(blank=True, null=True)
    pais_origen = models.CharField(max_length=100)
    es_exclusiva = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_marca

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='productos')
    id_familia = models.CharField(max_length=100, blank=True, null=True, help_text="Ej: Floral, Amaderado, Cítrico")
    foto = models.ImageField(upload_to='img_productos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.id_marca.nombre_marca})"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"