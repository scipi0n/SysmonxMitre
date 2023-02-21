from django import forms


class UploadFileForm(forms.Form):
    Ev1 = '1'
    Ev3 = '3'
    Ev7 = '7'
    Ev8 = '8'
    Ev10 = '10'
    Ev11 = '11'
    Ev12 = '12'
    Ev17 = '17'
    Ev22 = '22'

    COUNTRY_CHOICES = (
        (Ev1, 'Evento 1: Creación de proceso'),
        (Ev3, 'Evento 3: Conexión de red'),
        (Ev7, 'Evento 7: Imagen cargada'),
        (Ev8, 'Evento 8: Creación de hilo remoto'),
        (Ev10, 'Evento 10: Acceso a proceso'),
        (Ev11, 'Evento 11: Creación de fichero'),
        (Ev12, 'Eventos 12, 13 y 14: Evento de registro'),
        (Ev17, 'Eventos 17 y 18: Eventos de tuberías (pipes)'),
        (Ev22, 'Evento 22: Query Dns')
    )
    file = forms.FileField()
    ips = forms.CharField()
    mult = forms.MultipleChoiceField(label="C",widget=forms.SelectMultiple, choices=COUNTRY_CHOICES)

class selectExcludesForm(forms.Form):
    select = forms.SelectMultiple

class ipsTextForm(forms.Form):
    ips = forms.CharField()