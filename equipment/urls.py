from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from .views import your_view, home_view
from django.views.generic import TemplateView

urlpatterns = [
    # часть, которая добавляется после доменного имени и ссылка на ф-цию представления
    path('', views.index,  name='home'),    #http://127.0.0.1:8000/equipment/
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('category/<slug:cat_slug>/', views.category_show, name='category'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    # path('', TemplateView.as_view(template_name='base.html'), name='base'),
    path('', your_view, name='your_view'),
    path('', home_view, name='home'),
    path('admin/', LoginView.as_view(template_name='admin/login.html'), name='admin-login'),
    # URL-маршрут для административной панели Django
    path('admin/', admin.site.urls),
]

