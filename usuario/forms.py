from django.forms import DateField, ModelForm, TextInput
from .models import Usuario,Agendamento

class PetForm(ModelForm): #PetForm
    class Meta:
        model = Usuario
        fields = ['nome','raça','porte','idade','ativa']


class FormAgendamento(ModelForm):
    data = DateField(
        widget=TextInput(
            attrs = {"type": "date"}
        )
    )
    class Meta:
        model = Agendamento
        fields = ['data','horario','banho','tosa','pulgas','observacao']
    # def save(self, commit=True):
    #     agendamento = super(FormAgendamento, self).save(commit=True)
    #     if commit:
    #         agendamento.save()
    #     return agendamento

# class MeuPetForm(ModelForm):
#     class Meta:
#         model = Pets
#         fields =['nome','raça','porte','idade','ativa']