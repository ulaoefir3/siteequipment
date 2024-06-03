from django import forms
from django.contrib import admin, messages
from django.forms import Textarea
from django.utils.safestring import mark_safe
from django.db import models
from .models import Category, Equipment, Target, EquipmentManufacturer, NameFilter, FilterValue, ServiceCenters, WorkingHours

admin.site.register(Category)
# admin.site.register(Equipment)
admin.site.register(Target)
admin.site.register(EquipmentManufacturer)
admin.site.register(NameFilter)
admin.site.register(FilterValue)
admin.site.register(ServiceCenters)


# @admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
	fields = ['title', 'photo', 'cat', 'tar']
	list_display = ('id', 'title', 'cat', 'tar')
	# автоматически формирует slug
	# prepopulated_fields = {"slug": ("title",)}
	list_display_links = ('id', 'title')
	search_fields = ['title', 'cat__name']
	list_filter = ('cat', 'manufacture')  # Поля, по которым будет производиться фильтрация
	# 	list_per_page = 20
	# панель для сохранения сверху
	save_on_top = True


class WorkingHoursAdminForm(forms.ModelForm):
    class Meta:
        model = WorkingHours
        fields = '__all__'
        widgets = {
            'title': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }

class WorkingHoursAdmin(admin.ModelAdmin):
    form = WorkingHoursAdminForm
    list_display = ('get_service', 'get_title')

    def get_service(self, obj):
        return obj.service

    get_service.short_description = 'Service'

    def get_title(self, obj):
        return obj.title

    get_title.short_description = 'Title'

admin.site.register(WorkingHours, WorkingHoursAdmin)




# @admin.register(Category)
# class WomenAdmin(admin.ModelAdmin):
# 	list_display = ('id', 'name')
# 	list_display_links = ('id', 'name')


admin.site.register(Equipment, EquipmentAdmin)
