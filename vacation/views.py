from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import permission_required
from django.core import serializers
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cart.forms import CartAddProductForm
from .forms import VillaForm, YachtForm, VehicleForm, RegistrationForm, LoginForm, ContactForm
from .models import Villa, Yacht, Vehicle, VillaPhotos, YachtPhotos, VehiclePhotos  # , Category
from .serializer import VillaSerializer, YachtSerializer, VehicleSerializer

data = serializers.serialize('python', VillaPhotos.objects.all(), fields=('photo_1', 'photo_2'))


def index(request):
    return render(request, 'vacation_html/index.html')


def villas(request):
    villas_list = Villa.objects.all()
    villa_photos = list(VillaPhotos.objects.all().values_list('villa_id',
                                                              'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5',
                                                              'photo_6', 'photo_7', 'photo_8', 'photo_9', 'photo_10',
                                                              named=True))

    context = {
        'villas_list': villas_list,
        'villa_photos': villa_photos,
    }

    paginator = Paginator(Villa.objects.all(), 3)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    context['page_obj'] = page_objects
    return render(request, 'vacation_html/villas_list.html', context)


def yachts(request):
    yachts_list = Yacht.objects.all()
    yacht_photos = list(YachtPhotos.objects.all().values_list('yacht_id',
                                                              'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5',
                                                              'photo_6', 'photo_7', 'photo_8', 'photo_9', 'photo_10',
                                                              named=True))

    context = {'yachts_list': yachts_list,
               'yacht_photos': yacht_photos,
              }

    paginator = Paginator(Yacht.objects.all(), 3)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    context['page_obj'] = page_objects
    return render(request, 'vacation_html/yachts_list.html', context)


def vehicles(request):
    vehicles_list = Vehicle.objects.all()
    vehicle_photos = list(VehiclePhotos.objects.all().values_list('vehicle_id',
                                                              'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5',
                                                              'photo_6', 'photo_7', 'photo_8', 'photo_9', 'photo_10',
                                                              named=True))

    context = {'vehicles_list': vehicles_list,
               'vehicle_photos': vehicle_photos,
               }

    paginator = Paginator(Vehicle.objects.all(), 3)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    context['page_obj'] = page_objects
    return render(request, 'vacation_html/vehicles_list.html', context)


def villa_details(request, villa_id):
    the_villa = get_object_or_404(Villa, pk=villa_id)
    villa_photos = list(VillaPhotos.objects.all().values_list(
        'villa_id', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'photo_7', 'photo_8', 'photo_9',
        'photo_10', named=True)
    )
    cart_form = CartAddProductForm
    context = {
                'villa_item': the_villa,
                'cart_form': cart_form,
                'villa_photos': villa_photos,
    }

    return render(request, 'vacation_html/villa_info.html', context)


def yacht_details(request, yacht_id):
    the_yacht = get_object_or_404(Yacht, pk=yacht_id)
    yacht_photos = list(YachtPhotos.objects.all().values_list(
        'yacht_id', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'photo_7', 'photo_8', 'photo_9',
        'photo_10', named=True)
    )
    cart_form = CartAddProductForm
    context = {
                'yacht_item': the_yacht,
                'yacht_photos': yacht_photos,
                'cart_form': cart_form,
    }

    return render(request, 'vacation_html/yacht_info.html', context)


def vehicle_details(request, vehicle_id):
    the_vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    vehicle_photos = list(VehiclePhotos.objects.all().values_list(
        'vehicle_id', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'photo_7', 'photo_8',
        'photo_9', 'photo_10', named=True)
    )
    cart_form = CartAddProductForm
    context = {
        'vehicle_item': the_vehicle,
        'vehicle_photos': vehicle_photos,
        'cart_form': cart_form,
    }

    return render(request, 'vacation_html/vehicle_info.html', context)


class VillaCreateView(CreateView):
    model = Villa
    form_class = VillaForm
    template_name = 'vacation_html/villa_add.html'
    context_object_name = 'form'
    success_url = reverse_lazy('villas_list')

    @method_decorator(permission_required('vacation.add_villa'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class VillaUpdateView(UpdateView):
    model = Villa
    form_class = VillaForm
    template_name = 'vacation_html/villa_edit.html'
    context_object_name = 'form'
    success_url = reverse_lazy('villas_list')

    @method_decorator(permission_required('vacation.change_villa'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class VillaDeleteView(DeleteView):
    model = Villa
    success_url = reverse_lazy('villas_list')

    @method_decorator(permission_required('vacation.delete_villa'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class YachtCreateView(CreateView):
    model = Yacht
    form_class = YachtForm
    template_name = 'vacation_html/yacht_add.html'
    context_object_name = 'form'
    success_url = reverse_lazy('yachts_list')

    @method_decorator(permission_required('vacation.add_yacht'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class YachtUpdateView(UpdateView):
    model = Yacht
    form_class = YachtForm
    template_name = 'vacation_html/yacht_edit.html'
    context_object_name = 'form'
    success_url = reverse_lazy('yachts_list')

    @method_decorator(permission_required('vacation.change_yacht'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class YachtDeleteView(DeleteView):
    model = Yacht
    success_url = reverse_lazy('yachts_list')

    @method_decorator(permission_required('vacation.delete_villa'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class VehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vacation_html/vehicle_add.html'
    context_object_name = 'form'
    success_url = reverse_lazy('vehicles_list')

    @method_decorator(permission_required('vacation.add_vehicle'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class VehicleUpdateView(UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vacation_html/vehicle_edit.html'
    context_object_name = 'form'
    success_url = reverse_lazy('vehicles_list')

    @method_decorator(permission_required('vacation.change_vehicle'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class VehicleDeleteView(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicles_list')

    @method_decorator(permission_required('vacation.delete_villa'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


def user_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            return redirect('log_in')
    else:
        form = RegistrationForm()
    return render(request, 'vacation_html/auth/registration.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print('is_anon', request.user.is_anonymous)
            print('is_auth', request.user.is_authenticated)
            login(request, user)
            print('is_anon', request.user.is_anonymous)
            print('is_auth', request.user.is_authenticated)
            print(user)
            return redirect('index_vacation')
    else:
        form = LoginForm()
    return render(request, 'vacation_html/auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index_vacation')


def contact_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['content'],
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_RECEIVER],
                fail_silently=False
            )
            if mail:
                return redirect('index_vacation')
    else:
        form = ContactForm()
    return render(request, 'vacation_html/email.html', {'form': form})


@api_view(['GET', 'POST'])
def vacation_villas_api_list(request):
    if request.method == 'GET':
        villas_list = Villa.objects.all()
        serializer = VillaSerializer(villas_list, many=True)
        return Response({'villas_list': serializer.data})
    elif request.method == 'POST':
        serializer = VillaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def vacation_yachts_api_list(request):
    if request.method == 'GET':
        yachts_list = Yacht.objects.all()
        serializer = YachtSerializer(yachts_list, many=True)
        return Response({'villas_list': serializer.data})
    elif request.method == 'POST':
        serializer = YachtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def vacation_vehicles_api_list(request):
    if request.method == 'GET':
        vehicles_list = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles_list, many=True)
        return Response({'villas_list': serializer.data})
    elif request.method == 'POST':
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def vacation_villa_api_detail(request, pk, format=None):
        villa_obj = get_object_or_404(Villa, pk=pk)
        if villa_obj.exist:
            if request.method == 'GET':
                serializer = VillaSerializer(villa_obj)
                return Response(serializer.data)
            elif request.method == 'PUT':
                serializer = VillaSerializer(villa_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': "Данные успешно изменены", 'vacation': serializer.data})
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif request.method == 'DELETE':
                villa_obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def vacation_yacht_api_detail(request, pk, format=None):
        yacht_obj = get_object_or_404(Yacht, pk=pk)
        if yacht_obj.exist:
            if request.method == 'GET':
                serializer = YachtSerializer(yacht_obj)
                return Response(serializer.data)
            elif request.method == 'PUT':
                serializer = YachtSerializer(yacht_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': "Данные успешно изменены", 'vacation': serializer.data})
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif request.method == 'DELETE':
                yacht_obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def vacation_vehicle_api_detail(request, pk, format=None):
        vehicle_obj = get_object_or_404(Vehicle, pk=pk)
        if vehicle_obj.exist:
            if request.method == 'GET':
                serializer = VehicleSerializer(vehicle_obj)
                return Response(serializer.data)
            elif request.method == 'PUT':
                serializer = VehicleSerializer(vehicle_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': "Данные успешно изменены", 'vacation': serializer.data})
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif request.method == 'DELETE':
                vehicle_obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
