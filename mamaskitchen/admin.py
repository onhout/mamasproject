from django.contrib import admin
from .models import MenuItem, MenuPicURL
# Register your models here.


class ChoiceInLine(admin.StackedInline):
    model = MenuPicURL
    extra = 1


class MenuItemModelAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "amount", "created_at")
    inlines = [ChoiceInLine]

    class Meta():
        model = MenuItem
        
admin.site.register(MenuItem, MenuItemModelAdmin)
admin.site.register(MenuPicURL)