from django.contrib import admin
from models import Editor, Autor, Libro

#Aqui es donde registramos o anadimos los modelos para que se
	#vean en el admin

#Configuramos el modelo Autor
class AutorAdmin(admin.ModelAdmin):
	#Para separa por campos
	list_display = ('nombre', 'apellido', 'email',) 
	#Anade una barra de busqueda en autores
	search_fields = ('nombre', 'apellido',)

#COnfiguramos el modelo Books
class BookAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'editorial','fecha_de_publicacion',)
	#Nos ayuda a filtrar resultados el
		# lado derecho sale(en este caso por fecha de public)
	list_filter = ('fecha_de_publicacion',)
	date_hierarchy = 'fecha_de_publicacion'
	ordering = ('-fecha_de_publicacion',)
	#mustra el cuadro con las multiple opciones que se pueden seleccionar
	filter_horizontal = ('autores',)
	raw_id_fields = ('editorial',)
 
#Registramos los modelos en el Admin
#Reciven como argumento las clases(Modelos)
admin.site.register(Editor)
#Registra el modelo Autor con las opciones de AutorAdmin
admin.site.register(Autor, AutorAdmin)
#Registra el modelo Libro con las opciones de BookAdmin
admin.site.register(Libro, BookAdmin)
