from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)
