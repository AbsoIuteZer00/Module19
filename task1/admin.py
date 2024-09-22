from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Game)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cost',)
    search_fields = ('name',)
    list_filter = ('cost', 'size',)


admin.site.register(Post)
