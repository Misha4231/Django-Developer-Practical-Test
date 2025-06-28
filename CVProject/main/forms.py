from django import forms

class SendPDFForm(forms.Form):
    email = forms.EmailField(label='E-Mail', max_length=255, required=True)