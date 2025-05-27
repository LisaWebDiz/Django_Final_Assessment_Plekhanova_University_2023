from django.urls import path

from vacation.views import *

urlpatterns = [
    path('', index, name="index_vacation"),

    path('villas/', villas, name='villas_list'),
    path('villas/<int:villa_id>/', villa_details, name='the_villa'),

    path('villas/add/', VillaCreateView.as_view(), name='add_villa'),
    path('villas/update/<int:pk>/', VillaUpdateView.as_view(), name='edit_villa'),
    path('villas/del/<int:pk>/', VillaDeleteView.as_view(), name='del_villa'),

    path('yachts/', yachts, name='yachts_list'),
    path('yachts/<int:yacht_id>/', yacht_details, name='the_yacht'),

    path('yachts/add/', YachtCreateView.as_view(), name='add_yacht'),
    path('yachts/update/<int:pk>/', YachtUpdateView.as_view(), name='edit_yacht'),
    path('yachts/del/<int:pk>/', YachtDeleteView.as_view(), name='del_yacht'),

    path('vehicles/', vehicles, name='vehicles_list'),
    path('vehicles/<int:vehicle_id>/', vehicle_details, name='the_vehicle'),

    path('vehicles/add/', VehicleCreateView.as_view(), name='add_vehicle'),
    path('vehicles/update/<int:pk>/', VehicleUpdateView.as_view(), name='edit_vehicle'),
    path('vehicles/del/<int:pk>/', VehicleDeleteView.as_view(), name='del_vehicle'),

    path('registration/', user_registration, name='regis'),
    path('login/', user_login, name='log_in'),
    path('logout/', user_logout, name='log_out'),

    path('email/', contact_email, name='email_contact'),

    path('api/villas/list', vacation_villas_api_list, name='vacation_villas_api_list'),
    path('api/villas/detail/<int:pk>', vacation_villa_api_detail, name='vacation_villa_api_detail'),

    path('api/yachts/list', vacation_yachts_api_list, name='vacation_yachts_api_list'),
    path('api/yachts/detail/<int:pk>', vacation_yacht_api_detail, name='vacation_yacht_api_detail'),

    path('api/vehicles/list', vacation_vehicles_api_list, name='vacation_vehicles_api_list'),
    path('api/vehicles/detail/<int:pk>', vacation_vehicle_api_detail, name='vacation_vehicle_api_detail')
]
