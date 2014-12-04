from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from books.models import Libro
from contact.forms import ContactForm
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

def muestra_META(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))

# Ya no es necesaria esta vista ya que en la de abajo la engloba
# def form_busqueda(request):
# 	return render_to_response('buscarForm.html')

def busqueda(request):
	errors = [];
	#tomamos la variable q del form que nos llego por request.GET
	if'q' in request.GET:
		nombre = request.GET['q']
		if not nombre:
			errors.append('Entra el termino de la busqueda')
		elif len(nombre) > 20:
			errors.append('Menos caracteres porfa')
		else:
			libro = Libro.objects.filter(titulo__icontains = nombre)
			return render_to_response('resBusqueda.html', 
			{ 'books': libro, 'query': nombre })
	return render_to_response('buscarForm.html', {'err': errors})

def contacto(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['asunto'],
				cd['message'],
				cd.get('email', 'gerolas_bofo@hotmail.com'),
				['gerolas_bofo@hotmail.com'],
			)
			return HttpResponseRedirect('/contacto/gracias/')
	else:
		form = ContactForm()
	return render_to_response('contact_form.html', {'form': form})
