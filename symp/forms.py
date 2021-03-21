from django import forms

class SympForm(forms.Form):
    CHOICES = (('a','Fever or chills'),
               ('b','Cough'),
               ('c','Shortness of breath'),
               ('d','Fatigue'),
               ('e', 'New loss of taste/smell'),
               ('f','Sore throat'),
               ('g','Congestion'),
               ('h','Nausea/vomiting'),
               ('i','Diarrhea'),
    )

    Symptoms = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= CHOICES)

class EmergencyList(forms.Form):
    EMCHOICES = (('a','Trouble breathing'),
                ('b','Persistent pain or pressure in the chest'),
                ('c','New confusion'),
                ('d','Inability to stay awake'),
                ('e','Pale, gray or blue-colored skin, lips or nail beds'),
    )

    Emergency_warning_signs = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= EMCHOICES)