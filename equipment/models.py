
from  django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Target(models.Model):
	name = models.CharField(max_length=100, db_index=True, verbose_name="Назначение")
	slug = models.SlugField(max_length=255, unique=True, db_index=True)

	class Meta:
		verbose_name = "Назначение"
		verbose_name_plural = "Назначение"


class Category(models.Model):
	name = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=255, unique=True, db_index=True)
	photo = models.ImageField(upload_to="photos/%Y/%m/%d", default=None, blank=True, null=True, verbose_name="Фото")

	class Meta:
		verbose_name = "Тип оборудования"
		verbose_name_plural = "Тип оборудования"

	def get_absolute_url(self):
		return reverse('category', kwargs={'cat_slug': self.slug})

	def __str__(self):
		return self.name


class EquipmentManufacturer(models.Model):
	name = models.CharField(max_length=100, db_index=True, verbose_name="Производитель:")

	class Meta:
		verbose_name = "Производитель оборудования"
		verbose_name_plural = "Производитель оборудования"

	def __str__(self):
		return self.name


class NameFilter(models.Model):
	name = models.CharField(max_length=100, db_index=True, verbose_name="Название параметра фильтра:")

	class Meta:
		verbose_name = "Название фильтра"
		verbose_name_plural = "Название фильтра"

	def __str__(self):
		return self.name


class FilterValue(models.Model):
	value = models.CharField(max_length=100, db_index=True, verbose_name="Параметр фильтра:")

	class Meta:
		verbose_name = "Значение фильтра"
		verbose_name_plural = "Значение фильтра"

	def __str__(self):
		return self.value


class ServiceCenters(models.Model):
	name = models.CharField(max_length=100, db_index=True, verbose_name="Сервисные центры:")

	class Meta:
		verbose_name = "Сервисные центры"
		verbose_name_plural = "Сервисные центры"

	def __str__(self):
		return self.name



class WorkingHours(models.Model):
	service = models.ForeignKey(ServiceCenters, on_delete=models.PROTECT, related_name='workinghours',
							verbose_name="Сервисный центр: ")
	title = models.CharField(max_length=100, verbose_name="Время работы тестировщиков: ")
	class Meta:
		verbose_name = "Время работы тестировщиков"
		verbose_name_plural = "Время работы тестировщиков"

	def __str__(self):
		return f"{self.title} ({self.service})"


class Equipment(models.Model):
	title = models.CharField(max_length=255, verbose_name="Модель оборудования: ")
	photo = models.ImageField(upload_to="photos/%Y/%m/%d", default=None, blank=True, null=True, verbose_name="Image: ")
	cat = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='equipment', verbose_name="Тип оборудования: ")
	tar = models.ForeignKey(Target, on_delete=models.PROTECT, related_name='equipment', verbose_name="Назначение: ")
	manufacture = models.ForeignKey(EquipmentManufacturer, on_delete=models.PROTECT, default=None, blank=False, null=True, verbose_name="Производитель")
	is_available = models.BooleanField(default=True, verbose_name="В наличие")

	name_filter = models.ForeignKey(NameFilter, on_delete=models.PROTECT, default=None, blank=True, null=True, verbose_name="Название дополнительного фильтра: ")
	value_filter = models.ForeignKey(FilterValue, on_delete=models.PROTECT, default=None, blank=True, null=True, verbose_name="Значение фильтра: ")

	class Meta:
		verbose_name = "Оборудование"
		verbose_name_plural = "Оборудование"

	def __str__(self):
		return f"{self.title} ({self.cat.name})"

	objects = models.Manager()

	#кнопка смотреть на сайте
	def get_absolute_url(self):
		return reverse('post', kwargs={'post_slug': self.slug})



