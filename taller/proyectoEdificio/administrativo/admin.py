from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Edificio, Departamento

# Agregar la clase Edificio para administrar desde
# interfaz de administración
# admin.site.register(Edificio)

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Edificio
class EdificioAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'direccion', 'ciudad','tipo')
    search_fields = ('nombre', 'ciudad','tipo' )

# admin.site.register se lo altera
# el primer argumento es el modelo (Edificio)
# el segundo argumento la clase EdificioAdmin
admin.site.register(Edificio, EdificioAdmin)

# Agregar la clase Departamento para administrar desde
# interfaz de administración
# admin.site.register(Departamento)

# Se crea una clase que hereda
# de ModelAdmin para el modelo Departamento
class DepartamentoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre_propietario', 'costo', 'numero_cuartos')
    # se agrega el atributo 
    # raw_id_fields que permite acceder a una interfaz 
    # para buscar los edificios y seleccionar el que 
    # se desee, en caso de no usarlo, se nos proporciona un select
    # de los edificios o la opcion de agregar o editar un edificio
    raw_id_fields = ('edificio',)

admin.site.register(Departamento, DepartamentoAdmin)
