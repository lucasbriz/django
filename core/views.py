from django.shortcuts import render, redirect
from core.forms import FormCliente, FormFabricante, FormVeiculo, FormRotativo, FormMensalista, FormTabela
from core.models import Cliente, Fabricante, Veiculo, Rotativo, Mensalista, Tabela
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
# antes e depois da função pular 2 espaços


def home(request):
    return render(request, 'core/index.html')


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/register.html'


def cadastro_cliente(request):
    try:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            form.save()
            messages.success(request, f'Cliente {nome} cadastrado com sucesso!')
            return redirect('url_lista_clientes')
        contexto = {'form': form, 'title': 'Cadastro de Cliente', 'stringButton': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto={'msg_erro':mensagem_erro}
        return render(request, '500.html', contexto)


def lista_clientes(request):
    dados = Cliente.objects.all()
    if request.POST:
        if request.POST['pesquisa']:
            dados = Cliente.objects.filter(nome=request.POST['pesquisa'])
    contexto = {'dados': dados}
    return render(request, 'core/lista_clientes.html', contexto)


def cadastro_veiculo(request):
    form = FormVeiculo(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form, 'title': 'Cadastro de Veículo', 'stringButton': 'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)


def lista_veiculos(request):
    dados = Veiculo.objects.all()
    if request.POST:
        if request.POST['pesquisa']:
            dados = Veiculo.objects.filter(placa=request.POST['pesquisa'])
    contexto = {'dados': dados}
    return render(request, 'core/lista_veiculos.html', contexto)


def cadastro_fabricante(request):
    form = FormFabricante(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form, 'title': 'Cadastro de Fabricante', 'stringButton': 'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)


def lista_fabricantes(request):
    dados = Fabricante.objects.all()
    if request.POST:
        if request.POST['pesquisa']:
            dados = Fabricante.objects.filter(descricao=request.POST['pesquisa'])
    contexto = {'dados': dados}
    return render(request, 'core/lista_fabricantes.html', contexto)


def altera_cliente(request, id):
    objeto = Cliente.objects.get(id=id)
    form = FormCliente(request.POST or None, request.FILES or None, instance=objeto)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        form.save()
        messages.success(request, f'Dados do cliente {nome} atualizados com sucesso!')
        return redirect('url_lista_clientes')
    contexto = {'form': form, 'title': 'Atualiza Cliente', 'stringButton': 'Salvar Alterações'}
    return render(request, 'core/cadastro.html', contexto)


def exclui_cliente(request, id):
    object = Cliente.objects.get(id=id)
    if request.POST:
        object.delete()
        messages.success(request, 'Cliente excluido com sucesso!')
        return redirect('url_lista_clientes')
    contexto = {'url': '/lista_clientes/', 'objeto': object.nome}
    return render(request, 'core/confirma_exclusao.html', contexto)


# view é uma função que está no servidor e conversa com o cliente no browser - por meio do request como parametro
def cadastro_rotativo(request):
    form = FormRotativo(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_rotativos')
    contexto = {'form': form, 'title': 'Cadastro de Rotativo', 'stringButton': 'Cadastrar', 'calendario': True}
    return render(request, 'core/cadastro.html', contexto)


def listagem_rotativos(request):
    dados = Rotativo.objects.all()
    if request.POST:
        if request.POST['pesquisa']:
            dados = Rotativo.objects.filter(id_veiculo=request.POST['pesquisa'])
    contexto = {'dados': dados}
    return render(request, 'core/listagem_rotativos.html', contexto)


def alterar_rotativo(request, id):
    objeto = Rotativo.objects.get(id=id)
    form = FormRotativo(request.POST or None, instance=objeto)
    if form.is_valid():
        objeto.calcula_total()
        form.save()
        return redirect('url_listagem_rotativos')
    contexto = {'form': form, 'titulo': 'Cadastro de Rotativo', 'stringButton': 'Salvar Alterações', 'calendario': True}
    return render(request, 'core/cadastro.html', contexto)


def alterar_mensalista(request, id):
    objeto = Mensalista.objects.get(id=id)
    form = FormMensalista(request.POST or None, instance=objeto)
    if form.is_valid():
        objeto.calculo_desconto()
        form.save()
        contexto = {'objeto': objeto.id_cliente, 'url': '/lista_mensalistas/'}
        return redirect('url_lista_mensalistas')
    contexto = {'form': form, 'título': 'Atualizar Mensalista', 'stringButton': 'Salvar Alterações', 'calendario': True}
    return render(request, 'core/cadastro.html', contexto)


def cadastro_tabela(request):
    form = FormTabela(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form, 'title': 'Cadastro de Valores', 'stringButton': 'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)


def lista_tabela(request):
    dados = Tabela.objects.all()
    if request.POST:
        if request.POST['pesquisa']:
            dados = Tabela.objects.filter(descricao=request.POST['pesquisa'])
    contexto = {'dados': dados}
    return render(request, 'core/tabela_precos.html', contexto)


def cadastro_mensalista(request):
    form = FormMensalista(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form, 'title': 'Cadastro de Mensalista', 'stringButton': 'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)


def lista_mensalista(request):
    dados = Mensalista.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_mensalistas.html', contexto)
