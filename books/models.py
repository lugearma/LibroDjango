from django.db import models

#-------------NOTAS A CONSIDERAR------------------------
#Cada modelo se representa mediante una clase de python
#Los metodos __unicode__(), devuelven algunas cadenas, si utilizamos 
#	este metodo es forzozo retornar un objeto tipo unicode
#verbose_name, permite colocarle un nombre a los campos de nuestro modelos

class Editor(models.Model):
	nombre = models.CharField(max_length = 30)
	direccion = models.CharField(max_length = 50)
	ciudad = models.CharField(max_length = 60, blank = True)
	estado = models.CharField(max_length = 30, blank = True)
	website = models.URLField(blank = True)

	def __unicode__(self):
		return self.nombre

	class Meta():
		ordering = ['nombre']

class Autor(models.Model):
	nombre = models.CharField(max_length = 30)
	apellido = models.CharField(max_length = 30)
	#blank = True, permite que se quede en blanco
	email = models.EmailField(blank = True)

	def __unicode__(self):
		return u'%s %s' % (self.nombre, self.apellido)

class Libro(models.Model):
	titulo = models.CharField(max_length = 100)
	#ManyToManyField, sirve para elegir de una lista varios
	autores = models.ManyToManyField(Autor)
	#ForeignKey(), solo nos permitira elegir una
	editorial = models.ForeignKey(Editor, verbose_name = 'Editorial')
	fecha_de_publicacion = models.DateField(blank = True, null = True)

	def __unicode__(self):
		return self.titulo

