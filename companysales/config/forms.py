from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'phone_number': 'Номер телефона',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddSellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'phone': 'Номер телефона',
            'position': 'Должность'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'phone': 'Номер телефона',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'phone': 'Номер телефона',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Название товара',
            'description': 'Описание',
            'image': 'Изображение',
            'stock': 'Количество(шт)',
            'price': 'Цена'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class OrderUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].empty_label = 'Покупатель не выбран'
        self.fields['seller'].empty_label = 'Продавец не выбран'
        self.fields['product'].empty_label = 'Товар не выбран'

    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'customer': 'Покупатель',
            'seller': 'Продавец',
            'product': 'Товар(продукт)',
            'date': 'Дата продажи',
            'total': 'Сумма'
        }
        widgets = {
            'customer': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'seller': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'product': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'total': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class Find1Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['seller'].empty_label = 'Выбирете продавца из списка'

    class Meta:
        model = Order
        fields = ['seller']
        widgets = {
            'seller': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            )
        }


class Find2Form(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['date']
        labels = {
            'date': 'Дата продажи',
        }
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            )
        }


class Find3Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].empty_label = 'Выберете продукт из списка'

    class Meta:
        model = Order
        fields = ['product']
        widgets = {
            'product': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            )
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1')


class ProfileForm(forms.ModelForm):
    city = forms.CharField(label="City", widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="Phone", widget=forms.TextInput(attrs={'class': 'form-control'}))
    avatar = forms.ImageField(label="Avatar", required=False, error_messages={'required': ' '},
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control',
                                    'type': 'file'}))
    first_name = forms.CharField(label="First name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Last name", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('city', 'phone', 'avatar', 'first_name', 'last_name')





