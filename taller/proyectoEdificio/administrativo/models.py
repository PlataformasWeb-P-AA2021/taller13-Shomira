from django.db import models

# Create your models here.

class Edificio(models.Model):
    #Opciones Edificio
    tipo_edificio = (
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
        )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField("Tipo Edificio",max_length=30, \
            choices=tipo_edificio) 

    def __str__(self):
        return "%s - %s - %s - %s.\n" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)
            
    def obt_costo_total_departamentos(self):
        valor = [d.costo for d in self.departamentos.all()]
        valor = sum(valor)
        return valor
    
    def obtener_num_total_cuartos(self):
        valor = [d.numero_cuartos for d in self.departamentos.all()]
        valor = sum(valor)
        return valor
            
class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=100)
    costo = models.FloatField()   
    numero_cuartos = models.IntegerField()   
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s -  %s - %s.\n" % (self.nombre_propietario,
                          self.costo,
                          self. numero_cuartos)

