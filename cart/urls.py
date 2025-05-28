from django.urls import path

from .views import *
from vacation.views import contact_email

urlpatterns = [
    path('', cart_info, name='list_cart'),
    path('add/<str:model_type>/<int:product_id>/', cart_add, name='add_cart'),
    path('remove/<int:product_id>/', cart_remove, name='remove_cart'),
    path('clear/', cart_clear, name='clear_cart'),
    path('email/', contact_email, name='email_contact'),

]
