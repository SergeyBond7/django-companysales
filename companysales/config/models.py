from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Customer(models.Model):
    first_name = models.CharField(max_length=64, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=64, blank=False, verbose_name='Фамилия')
    email = models.EmailField(max_length=64, blank=True, null=True, verbose_name='Почта')
    phone = models.CharField(max_length=32, blank=False, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return self.first_name + " " + self.last_name


class Seller(models.Model):
    first_name = models.CharField(max_length=64, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=64, blank=False, verbose_name='Фамилия')
    email = models.EmailField(max_length=64, blank=True, null=True, verbose_name='Почта')
    phone = models.CharField(max_length=32, blank=False, verbose_name='Телефон')

    POSITION_CHOICES = [
        (0, 'Продавец'),
        (1, 'Старший продавец'),
        (2, 'Руководитель отдела продаж')
    ]


    date = models.DateField(blank=False, verbose_name='Дата контракта')
    position = models.IntegerField(
        blank=False,
        choices=POSITION_CHOICES,
        default=0,
        verbose_name='Должность'
    )

    def flavor_verbose(self):
        return dict(Seller.POSITION_CHOICES)[self.position]


    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'

    def __str__(self):
        return self.first_name + " " + self.last_name


class Product(models.Model):
    name = models.CharField(max_length=64, blank=False, verbose_name='Название')
    description = models.TextField(blank=True, default='', verbose_name='Описание')
    image = models.ImageField(upload_to='product_images/%Y/%m/%d', verbose_name='Изображение')
    stock = models.IntegerField(blank=True, default=0, verbose_name='В наличии (шт)')
    price = models.DecimalField(max_digits=19, decimal_places=2, default=0, verbose_name='Цена')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
        related_name= 'orders',
        related_query_name='order',
        verbose_name='Покупатель'
    )
    seller = models.ForeignKey(
        'Seller',
        on_delete=models.CASCADE,
        related_name='orders',
        related_query_name='order',
        verbose_name='Продавец'
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='orders',
        related_query_name='order',
        verbose_name='Продукт'
    )
    date = models.DateField(auto_now_add=False, verbose_name='Дата заказа')
    total = models.DecimalField(max_digits=19, decimal_places=2, default=0, verbose_name='Сумма продажи')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.seller}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    city = models.CharField(max_length=64, default='', verbose_name='Город')
    phone = models.CharField(blank=True, max_length=64, default='', verbose_name='Телефон')
    avatar = models.ImageField(blank=True, upload_to='profile_avatars/%Y/%m/%d', verbose_name='Аватар',
                               default='profile_avatars/default.jpg')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

