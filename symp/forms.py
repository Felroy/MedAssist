from django import forms

class SympForm(forms.Form):
    CHOICES = (('a','AA'),
               ('b','BB'),
               ('c','CC'),
               ('d','DD'),
    )

    Symptoms = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= CHOICES)
