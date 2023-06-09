from django.contrib import admin
from .models import MenuItem, Category, Review


class ReviewAdminInline(admin.TabularInline):
    model = Review
    extra = 0


class MenuItemAdmin(admin.ModelAdmin):
    inlines = (ReviewAdminInline,)

    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Category, CategoryAdmin)
