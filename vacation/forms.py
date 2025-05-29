from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Villa, Yacht, Vehicle


class VillaForm(forms.ModelForm):
    class Meta:
        model = Villa
        fields = ['title', 'region', 'description', 'rooms_number', 'bedrooms_number', 'bathrooms_number', 'total_area',
                  'living_area', 'sea_distance', 'additional_info', 'price_per_day', 'exist']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingInput',
                    'placeholder': "Наименование"
                }
            ),
            'region': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Регион"
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Описание"
                }
            ),
            'rooms_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Количество комнат"
                }
            ),
            'bedrooms_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Количество спален"
                }
            ),
            'bathrooms_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Количество ванных комнат"
                }
            ),
            'total_area': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Общая площадь, кв. м"
                }
            ),
            'living_area': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Жилая площадь, кв. м"
                }
            ),
            'sea_distance': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Расстояние до моря"
                }
            ),
            'additional_info': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Дополнительные характеристики"
                }
            ),
            'price_per_day': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Стоимость аренды на 1 сутки, евро"
                }
            ),
            'exist': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            )
        }


class YachtForm(forms.ModelForm):
    class Meta:
        model = Yacht
        fields = ['title', 'length', 'width', 'cabins_number', 'beds_number', 'maximum_speed', 'additional_info',
                  'price_per_day', 'exist']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingInput',
                    'placeholder': "Наименование"
                }
            ),
            'length': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Длина, м"
                }
            ),
            'width': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ширина, м"
                }
            ),
            'cabins_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Количество кают"
                }
            ),
            'beds_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Количество спальных мест"
                }
            ),
            'maximum_speed': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Максимальная скорость, узл"
                }
            ),
            'additional_info': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Дополнительные характеристики"
                }
            ),
            'price_per_day': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Стоимость аренды на 1 сутки, евро"
                }
            ),
            'exist': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            )
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['title', 'description', 'color', 'seats_number', 'doors_number', 'horsepower', 'engine',
                  'transmission', 'drive', 'maximum_speed', 'price_per_day', 'exist']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingInput',
                    'placeholder': "Наименование"
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Описание"
                }
            ),
            'color': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Цвет кузова"
                }
            ),
            'seats_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Количество мест"
                }
            ),
            'doors_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Количество дверей"
                }
            ),
            'horsepower': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Мощность, л.с."
                }
            ),
            'engine': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Объекм двигателя, куб. см"
                }
            ),
            'transmission': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Трансмиссия"
                }
            ),
            'drive': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Привод"
                }
            ),
            'maximum_speed': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Максимальная скорость, км/час"
                }
            ),
            'price_per_day': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Стоимость аренды на 1 сутки, евро"
                }
            ),
            'exist': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            )
        }


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class':'form-control', }),
        min_length=2,
    )
    email = forms.CharField(
        label='Адрес электронной почты',
        widget=forms.EmailInput(attrs={'class': 'form-control', }),
        min_length=2,
    )
    password1 = forms.CharField(
        label='Придумайте пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )
    password2 = forms.CharField(
        label='Введите пароль повторно',
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Ваш логин',
        widget=forms.TextInput(attrs={'class': 'form-control', }),
        min_length=2,
    )
    password = forms.CharField(
        label='Ваш пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )


class ContactForm(forms.Form):
    subject = forms.CharField(
        label="Тема сообщения",
        widget=forms.TextInput(
            attrs={'class': 'form-control'},
        )
    )
    content = forms.CharField(
        label="Текст сообщения",
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 11, },
        )
    )
