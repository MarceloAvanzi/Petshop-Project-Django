from django.contrib import admin

from usuario.models import Pets, Usuario

# Register your models here.
@admin.action(description='Ativar pessoas selecionadas')
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=True)

@admin.action(description='Desativar pessoas selecionadas')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=False)

class pessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'email',
        'celular',
        'idade',
        'ativa'
    ]
    list_filter = [
        'ativa'
    ]
    search_fields = [
        'nome_completo'
    ]
    actions = [
        ativar_todos,
        desativar_todos
    ]

admin.site.register(Usuario, pessoaAdmin)
admin.site.register(Pets)
