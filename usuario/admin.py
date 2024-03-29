from django.contrib import admin

from usuario.models import Usuario,Agendamento

# Register your models here.
@admin.action(description='Ativar pessoas selecionadas')
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=True)

@admin.action(description='Desativar pessoas selecionadas')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=False)

class pessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'raça',
        'porte',
        'idade',
        'ativa'
    ]
    list_filter = [
        'ativa'
    ]
    search_fields = [
        'nome'
    ]
    actions = [
        ativar_todos,
        desativar_todos
    ]

class agendamentoAdmin(admin.ModelAdmin):
    list_display = [
        'data','horario','tosa','pulgas','observacao','usuariologado','pet'
    ]

admin.site.register(Usuario, pessoaAdmin)
admin.site.register(Agendamento, agendamentoAdmin)
