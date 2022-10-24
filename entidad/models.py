from django.db import models


TIPO_IVA_CHOICE = (
    ("CF", "Consumidor final"),
    ("RI", "Responsable inscripto"),
    ("MT", "Monotributista")
)


# Create your models here.
class Localidad(models.Model):
    nombre = models.CharField("Nombre localidad", max_length=50)
    cp = models.CharField("Cod. Postal", max_length=10)
    provincia = models.CharField(max_length=20)
    
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = 'Localidades'
    
    def __str__(self):
        return "%s - CP: %s" % (self.nombre, self.cp)



class Persona(models.Model):
    nombre = models.CharField("Nombre/s", max_length=150)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(null=True, blank=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_nac = models.DateField("Fecha de nacimiento", null=True, blank=True)
    tipo_iva = models.CharField("Tipo de IVA", max_length=2, choices=TIPO_IVA_CHOICE, default="CF")
    
    class Meta:
        ordering = ["apellido", "nombre"]
    
    def __str__(self):
        return "%s, %s" % (self.apellido, self.nombre)

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    
    class Meta:
        ordering = ["apellido", "nombre"]
        verbose_name_plural = "Autores"
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    editorial = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.titulo} ({self.autor})"




# <Modelo>.objects.create() Inserta un nuevo registro
# <Modelo>.objects.all() Retorna todos los registros de la tabla
# <Modelo>.objects.get(<nombre_campo>=<valor>) Retorna un registro particular obtenido a partir del argumento
# <Modelo>.objects.filter(<nombre_campo__*) Retorna un conjunto de datos que coincida con el argumento
# CAMPOS NUMERICOS
# * gt (>), gte (>=), lt (<), lte (<=), = (=)
# CAMPOS DE TEXTO
# contains, startswith, endswith