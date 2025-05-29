from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from vacation.models import Villa, Yacht, Vehicle
from .cart import Cart
from .forms import CartAddProductForm


@login_required
@require_POST
def cart_add(request, model_type, product_id):
    model_map = {
        'villa': Villa,
        'yacht': Yacht,
        'vehicle': Vehicle,
    }
    model = model_map.get(model_type)
    if not model:
        return HttpResponseBadRequest("Invalid product type")

    product = get_object_or_404(model, pk=product_id)
    cart = Cart(request)

    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            count_product=cd['count_prod'],
            update_count=cd['update']
        )
    return redirect('list_cart')


def cart_remove(request, product_id):
    model_type = request.GET.get('type')

    if model_type == 'villa':
        model = Villa
    elif model_type == 'yacht':
        model = Yacht
    elif model_type == 'vehicle':
        model = Vehicle
    else:
        return redirect('list_cart')

    product = get_object_or_404(model, pk=product_id)
    cart = Cart(request)
    cart.remove(product, model_type=model_type)
    return redirect('list_cart')


def cart_info(request):
    cart = Cart(request)
    return render(request, 'cart_html/detail.html', {'cart': cart})


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('index_vacation')
