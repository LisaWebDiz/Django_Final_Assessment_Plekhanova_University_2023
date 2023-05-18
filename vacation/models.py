from django.db import models
from django.urls import reverse


# class Category(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#
#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'Катеририя'
#         verbose_name_plural = 'Категории'
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('index_vacation', args=[self.slug])


class Villa(models.Model):
    title = models.CharField(max_length=120, default='Вилла', null=False, verbose_name='Наименование')
    region = models.CharField(max_length=50, default='Регион', null=False, verbose_name='Регион')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    rooms_number = models.IntegerField(null=True, verbose_name='Количество комнат')
    bedrooms_number = models.IntegerField(null=True, verbose_name='Количество спален')
    bathrooms_number = models.IntegerField(null=True, verbose_name='Количество ванных комнат')
    total_area = models.FloatField(null=True, verbose_name='Общая площадь, кв. м')
    living_area = models.FloatField(null=True, verbose_name='Жилая площадь, кв. м')
    sea_distance = models.CharField(max_length=10, null=False, verbose_name='Расстояние до моря')
    additional_info = models.TextField(blank=True, null=True, verbose_name='Дополнительные характеристики')
    price_per_day = models.FloatField(null=False, verbose_name='Стоимость аренды на 1 сутки, евро')
    photo = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото')
    publication_date = models.DateField(auto_now_add=True, null=True, verbose_name='Дата добавления')
    update_date = models.DateField(auto_now=True, null=True, verbose_name='Дата обновления')
    exist = models.BooleanField(default=True, null=True, verbose_name='Предлагается?')
    slug = models.SlugField(max_length=200, default=False, db_index=True)

    def __str__(self):
        return 'Вилла: ' + self.title

    def get_absolute_url(self):
        return reverse('the_villa', kwargs={'villa_id': self.pk})

    class Meta:
        verbose_name = 'Вилла'
        verbose_name_plural = 'Виллы'
        ordering = ['-price_per_day']
        index_together = (('id', 'slug'),)

    # category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, related_name='products_villa')


class Yacht(models.Model):
    title = models.CharField(max_length=120, default='Яхта', null=False, verbose_name='Наименование')
    length = models.FloatField(null=False, verbose_name='Длина, м')
    width = models.FloatField(null=False, verbose_name='Ширина, м')
    cabins_number = models.IntegerField(null=False, verbose_name='Количество кают')
    beds_number = models.IntegerField(null=False, verbose_name='Количество спальных мест')
    maximum_speed = models.FloatField(null=False, verbose_name='Максимальная скорость, узл')
    additional_info = models.TextField(blank=True, null=True, verbose_name='Дополнительные характеристики')
    price_per_day = models.FloatField(null=False, verbose_name='Стоимость аренды на 1 сутки, евро')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Фото')
    publication_date = models.DateField(auto_now_add=True, null=True, verbose_name='Дата добавления')
    update_date = models.DateField(auto_now=True, null=True, verbose_name='Дата обновления')
    exist = models.BooleanField(default=True, null=True, verbose_name='Предлагается?')
    slug = models.SlugField(max_length=200, default=False, db_index=True)


    def __str__(self):
        return 'Яхта: ' + self.title

    def get_absolute_url(self):
        return reverse('the_yacht', kwargs={'yacht_id': self.pk})

    class Meta:
        verbose_name = 'Яхта'
        verbose_name_plural = 'Яхты'
        ordering = ['-price_per_day']
        index_together = (('id', 'slug'),)

    # category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, related_name='products_yacht')


class Vehicle(models.Model):
    title = models.CharField(max_length=120, default='Автомобиль', null=False, verbose_name='Модель')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    color = models.CharField(max_length=30, null=False, verbose_name='Цвет кузова')
    seats_number = models.IntegerField(null=False, verbose_name='Количество мест')
    doors_number = models.IntegerField(null=False, verbose_name='Количество дверей')
    horsepower = models.IntegerField(null=False, verbose_name='Мощность, л.с.')
    engine = models.FloatField(null=False, verbose_name='Объекм двигателя, куб. см')
    transmission = models.CharField(max_length=15, null=False, verbose_name='Трансмиссия')
    drive = models.CharField(max_length=15, null=False, verbose_name='Привод')
    maximum_speed = models.FloatField(null=False, verbose_name='Максимальная скорость, км/час')
    price_per_day = models.FloatField(null=False, verbose_name='Стоимость аренды на 1 сутки, евро')
    photo = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото')
    publication_date = models.DateField(auto_now_add=True, null=True, verbose_name='Дата добавления')
    update_date = models.DateField(auto_now=True, null=True, verbose_name='Дата обновления')
    exist = models.BooleanField(default=True, null=True, verbose_name='Предлагается?')



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('the_vehicle', kwargs={'vehicle_id': self.pk})

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['-price_per_day']


class VillaPhotos(models.Model):
    photo_1 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 1')
    photo_2 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 2')
    photo_3 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 3')
    photo_4 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 4')
    photo_5 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 5')
    photo_6 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 6')
    photo_7 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 7')
    photo_8 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 8')
    photo_9 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 9')
    photo_10 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 10')

    def __str__(self):
        return 'Фотография виллы № ' + str(self.pk)

    def get_absolute_url(self):
        return reverse('villa_photo', kwargs={'villa_photo_id': self.pk})

    class Meta:
        verbose_name = 'Фотография виллы'
        verbose_name_plural = 'Фотографии вилл'

    def get_fields(self):
        return [field.value_from_object(self) for field in self.__class__._meta.fields]

    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, null=True, verbose_name='Вилла')


class YachtPhotos(models.Model):
    photo_1 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 1')
    photo_2 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 2')
    photo_3 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 3')
    photo_4 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 4')
    photo_5 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 5')
    photo_6 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 6')
    photo_7 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 7')
    photo_8 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 8')
    photo_9 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 9')
    photo_10 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 10')

    def __str__(self):
        return 'Фотография яхты № ' + str(self.pk)

    def get_absolute_url(self):
        return reverse('yacht_photo', kwargs={'yacht_photo_id': self.pk})

    class Meta:
        verbose_name = 'Фотография яхты'
        verbose_name_plural = 'Фотографии яхт'

    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE, null=True, verbose_name='Яхта')


class VehiclePhotos(models.Model):
    photo_1 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 1')
    photo_2 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 2')
    photo_3 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 3')
    photo_4 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 4')
    photo_5 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 5')
    photo_6 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 6')
    photo_7 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 7')
    photo_8 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 8')
    photo_9 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 9')
    photo_10 = models.ImageField(null=True, blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото 10')

    def __str__(self):
        return 'Фотография автомобиля №' + str(self.pk)

    def get_absolute_url(self):
        return reverse('vehicle_photo', kwargs={'vehicle_photo_id': self.pk})

    class Meta:
        verbose_name = 'Фотография автомобиля'
        verbose_name_plural = 'Фотографии автомобилей'

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, verbose_name='Автомобиль')







