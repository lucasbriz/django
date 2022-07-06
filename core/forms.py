from django.forms import ModelForm
from core.models import Cliente, Fabricante, Veiculo, Rotativo, Mensalista, Tabela
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class FormFabricante(ModelForm):
    class Meta:
        model = Fabricante
        fields = '__all__'


class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class FormVeiculo(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class FormRotativo(ModelForm):
    class Meta:
        model = Rotativo
        fields = '__all__'
        #fields = ['data_entrada', 'id_veiculo', 'id_tabela'] - metodo para personalizar um formulário
        widgets = {'data_entrada':DateTimePickerInput(),
                   'data_saida':DateTimePickerInput()}


class FormMensalista(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'


class FormTabela(ModelForm):
    class Meta:
        model = Tabela
        fields = '__all__'

