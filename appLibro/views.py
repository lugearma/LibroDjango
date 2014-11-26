from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

#Vista hola mundo
def hello(request):
	return HttpResponse("Hola flaca corps :)")

#Vista que muestra la hora actual
def hora_actual(request):
	now = datetime.datetime.now()
	return render_to_response('horaActual.html', { 'hora_actual': now })

#Vista que agrega horas de mas respecto a la actual
def horas_de_mas(request, agregado):
	try:
		agregado = int(agregado)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours = agregado)
	return render_to_response('horasFuturas.html', {'agregado_mas': agregado, 'horas_futuras': dt})

def book_list(request):
	books = Book.objects.oreder_by('name')
	return render_to_response('book_list.html', {'books': books})


