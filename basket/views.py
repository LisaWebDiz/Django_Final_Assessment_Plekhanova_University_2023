from django.shortcuts import render, redirect, get_object_or_404
from vacation.models import Villa # Yacht, Category
from .basket import Basket
from .forms import BasketAddProductForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


@login_required
@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product_obj = get_object_or_404(Villa, pk=product_id)
    form = BasketAddProductForm(request.POST)

    if form.is_valid():
        basket_info = form.cleaned_data
        basket.add(product=product_obj,
                   count_product=basket_info['count_prod'],
                   update_count=basket_info['update'])

    return redirect('list_basket')


def basket_remove(request, product_id):
    basket = Basket(request)
    product_obj = get_object_or_404(Villa, pk=product_id)

    basket.remove(product_obj)
    return redirect('list_basket')


def basket_info(request):
    basket = Basket(request)
    return render(request, 'basket_html/detail.html', {'basket': basket})


def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('villas_list')



