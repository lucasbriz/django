from django.contrib import admin
from core.models import Cliente, Fabricante, Veiculo, Tabela, Mensalista, Rotativo, FormaPagamento

# Register your models here.


admin.site.register(Cliente)
admin.site.register(Fabricante)
admin.site.register(Veiculo)
admin.site.register(Tabela)
admin.site.register(Mensalista)
admin.site.register(Rotativo)
admin.site.register(FormaPagamento)


