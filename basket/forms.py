from django import forms

DAYS_MAX_COUNT = [(i, str(i)) for i in range(1, 31)]


class BasketAddProductForm(forms.Form):
    count_prod = forms.TypedChoiceField(choices=DAYS_MAX_COUNT, coerce=int, label='Количество дней')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

