from django import forms

class SendPDFForm(forms.Form):
    email = forms.EmailField(label='E-Mail', max_length=255, required=True)


LANGUAGE_CHOICES = [
    ('', 'Select language'),
    ('Cornish', 'Cornish'),
    ('Manx', 'Manx'),
    ('Breton', 'Breton'),
    ('Inuktitut', 'Inuktitut'),
    ('Kalaallisut', 'Kalaallisut'),
    ('Romani', 'Romani'),
    ('Occitan', 'Occitan'),
    ('Ladino', 'Ladino'),
    ('Northern Sami', 'Northern Sami'),
    ('Upper Sorbian', 'Upper Sorbian'),
    ('Kashubian', 'Kashubian'),
    ('Zazaki', 'Zazaki'),
    ('Chuvash', 'Chuvash'),
    ('Livonian', 'Livonian'),
    ('Tsakonian', 'Tsakonian'),
    ('Saramaccan', 'Saramaccan'),
    ('Bislama', 'Bislama'),
]

class TranslateForm(forms.Form):
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, label="Translate to", required=False)