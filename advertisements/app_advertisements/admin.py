from django.contrib import admin

from .models import Advertisements
from django.db.models.query import QuerySet


class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description', 'price', 'created_date', 'updated_date'] #столбцы для отображения в таблице
    list_filter = [ 'auction', 'created_at', 'updated_at']
    actions = ['make_action_as_false']
    fieldsets =(
        ('Общие', {
            'fields':(
                'title', 'description'
            ),
        }),
        ('Финансы', {
            'fields':(
                'price', 'auction'
            ),
            'classes': ['collapse'] #скрыть/показать блок
        }),
    )
    @admin.action(description='Убрать возможность торга')
    def make_action_as_false(self, request, queryset:QuerySet):
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def make_action_as_true(self, request, queryset:QuerySet):
        queryset.update(auction = True)

admin.site.register(Advertisements, AdvertisementsAdmin)