from django import forms

# NOTA
# Cada campo es obligatorio, si queremos hacerlos opconales sera
# necesario que le pongamos "required = False"

class ContactForm(forms.Form):
	asunto = forms.CharField(max_length = 100)
	email = forms.EmailField(required = False, label = 'Direccion de correo')
	message = forms.CharField(widget = forms.Textarea)

	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Mas letras porfa")
	return message