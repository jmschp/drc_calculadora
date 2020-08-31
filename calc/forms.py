from django import forms


class CalcDosagemForm(forms.Form):
    produto = forms.CharField(label='Produto', max_length=255)
    qtd_ml = forms.IntegerField(label="Quantidade de ml")
    concentracao_cbd_mg = forms.IntegerField(label="Concentração de CBD em mg")
    gotas_dose = forms.IntegerField(label="Sua prescrição, quantas gotas por dose", required=False)
    mg_dose = forms.DecimalField(label="Miligramas por dose", required=False, decimal_places=2)


if __name__ == "__main__":
    pass
