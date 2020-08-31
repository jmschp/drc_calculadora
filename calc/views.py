from django.shortcuts import render
from .models import Produto
from .forms import CalcDosagemForm


# Create your views here.


def index(request):
    produtos = Produto.objects.all()
    dados = {
        "produtos": produtos
    }
    return render(request, 'calc/index.html', dados)


def calc_dosagem(request):
    gotas_por_ml = 20
    if request.method == "POST":
        form = CalcDosagemForm(request.POST)
        if form.is_valid():
            produto = form.cleaned_data['produto']
            qtd_ml = form.cleaned_data['qtd_ml']
            concentracao_cbd_mg = form.cleaned_data['concentracao_cbd_mg']
            mg_dose = form.cleaned_data['mg_dose']
            gotas_dose = form.cleaned_data['gotas_dose']
            total_gotas = (form.cleaned_data['qtd_ml'] * gotas_por_ml)
            if form.cleaned_data['mg_dose'] is None:
                mg_dose = (gotas_dose * concentracao_cbd_mg) / (qtd_ml * gotas_por_ml)
            elif form.cleaned_data['gotas_dose'] is None:
                gotas_dose = int((qtd_ml * gotas_por_ml * mg_dose) / concentracao_cbd_mg)
            dados = {
                'produto': produto,
                'qtd_ml': qtd_ml,
                'concentracao_cbd_mg': concentracao_cbd_mg,
                'gotas_dose': gotas_dose,
                'mg_dose': mg_dose,
                "total_gotas": total_gotas
            }
            return render(request, 'calc/calc_resultado.html', dados)
    else:
        form = CalcDosagemForm()
        dados = {'form': form}
        return render(request, 'calc/calc_dosagem.html', dados)


# def comp_preco(request):
#     pass
