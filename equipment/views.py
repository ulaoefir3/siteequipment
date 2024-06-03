
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import DetailView

from equipment.models import Equipment, Target, Category, ServiceCenters

# Create your views here.


menu = [
	{'title': "Абонентское оборудование", 'url_name': 'about'},
	{'title': "Оборудование для продажи", 'url_name': 'contact'},
	# {'title': "Войти", 'url_name': 'login'},
]

#ГЛАВНАЯ СТРАНИЦА
def index(request):
	equipments_for_rent = Equipment.objects.filter(tar__slug="rent")
	equipments_for_sale = Equipment.objects.filter(tar__slug="sale")

	categories_for_rent = Category.objects.filter(equipment__in=equipments_for_rent).distinct()
	categories_for_sale = Category.objects.filter(equipment__in=equipments_for_sale).distinct()
	service_centers = ServiceCenters.objects.all()

	data = {
		'title': "Главная страница",
		'menu': menu,
		'equipments_for_rent': equipments_for_rent,
		'equipments_for_sale': equipments_for_sale,
		'categories_for_rent': categories_for_rent,
		'categories_for_sale': categories_for_sale,
		'service_centers': service_centers
	}
	return render(request, 'equipment/index.html', data)


def category_show(request, cat_slug):
	category = get_object_or_404(Category, slug=cat_slug)
	equipments = Equipment.objects.filter(cat=category)
	service_centers = ServiceCenters.objects.all()
	equipments_for_rent = Equipment.objects.filter(tar__slug="rent")
	equipments_for_sale = Equipment.objects.filter(tar__slug="sale")
	categories_for_rent = Category.objects.filter(equipment__in=equipments_for_rent).distinct()
	categories_for_sale = Category.objects.filter(equipment__in=equipments_for_sale).distinct()

	data = {
		'title': category,
		'menu': menu,
		'category': category,
		'equipments': equipments,
		'service_centers': service_centers,
		'equipments_for_rent': equipments_for_rent,
		'equipments_for_sale': equipments_for_sale,
		'categories_for_rent': categories_for_rent,
		'categories_for_sale': categories_for_sale

	}
	return render(request, 'equipment/category.html', data)
def your_view(request):
    service_centers = ServiceCenters.objects.all()
    return render(request, 'base.html', {'service_centers': service_centers})
def home_view(request):
    categories_for_rent = Category.objects.all()
    return render(request, 'category.html', {'categories_for_rent': categories_for_rent})

class DataMixin:
	pass
class ShowPost(DataMixin, DetailView):
	model = Equipment
	template_name = 'sequipment/post.html'
	slug_url_kwarg = 'post_slug'
	context_object_name = 'post'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return self.get_mixin_context(context, title=context['post'].title)

	# def get_object(self, queryset=None):
	# 	#выбираем статью только из опубликованных записей, по сталу та что в черновике - выдаст ошибку
	# 	return get_object_or_404(Equipment.published, slug=self.kwargs[self.slug_url_kwarg])

def about(request):
	return render(request, 'equipment/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_id):
	return HttpResponse(f"Отображение статьи с id = {post_id}")


def addpage(request):
	return HttpResponse("Добавление статьи")

def contact(request):
	return HttpResponse("Обратная связь")

def login(request):
	return HttpResponse("Авторизация")

def page_not_found(request, exception):
	return HttpResponseNotFound("<h1>Страница не найдена</h1>")

