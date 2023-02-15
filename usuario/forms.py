import datetime
from django.forms import DateField, ModelForm, TextInput, TimeField, TimeInput
from .models import Usuario,Agendamento

class PetForm(ModelForm): #PetForm
    class Meta:
        model = Usuario
        fields = ['nome','raça','porte','idade','ativa']


class FormAgendamento(ModelForm):
    data = DateField(
        initial=datetime.date.today,
        widget=TextInput(
            attrs = {"type": "date"}
        )
    )
    horario = TimeField(
        label='Hora',
        widget=TimeInput(
            format='%H:%M',
            attrs={
                'type': 'time',
            }),
        input_formats=('%H:%M',),
    )
    class Meta:
        model = Agendamento
        fields = ['pet','data','horario','tosa','pulgas','observacao']












# class MeuPetForm(ModelForm):
#     class Meta:
#         model = Pets
#         fields =['nome','raça','porte','idade','ativa']