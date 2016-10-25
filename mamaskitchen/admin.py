from django.contrib import admin
from .models import MenuItem, MenuPicURL, FoodType, FoodItemRelationship
# Register your models here.


class ItemURLInline(admin.StackedInline):
    model = MenuPicURL
    extra = 1


class TypeTabular(admin.TabularInline):
    model = FoodItemRelationship
    extra = 1


class MenuItemModelAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "amount", "created_at")
    inlines = (
        ItemURLInline,
        TypeTabular,
    )

    class Meta():
        model = MenuItem


class FoodTypeModelAdmin(admin.ModelAdmin):
    inlines = (TypeTabular,)

admin.site.register(MenuItem, MenuItemModelAdmin)
admin.site.register(FoodType, FoodTypeModelAdmin)