from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from vacation.views import contact_email
from .views import *

urlpatterns = [
    path('', cart_info, name='list_cart'),
    path('add/<str:model_type>/<int:product_id>/', cart_add, name='add_cart'),
    path('remove/<int:product_id>/', cart_remove, name='remove_cart'),
    path('clear/', cart_clear, name='clear_cart'),
    path('email/', contact_email, name='email_contact'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
