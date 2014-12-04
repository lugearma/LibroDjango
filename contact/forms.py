from django import forms

# NOTA
# Cada campo es obligatorio, si queremos hacerlos opconales sera
# necesario que le pongamos "required = False"

class ContactForm(forms.Form):
	asunto = forms.CharField()
	email = forms.EmailField(required = False)
	message = forms.CharField()
