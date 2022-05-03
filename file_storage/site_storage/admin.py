from django.contrib import admin
from .models import Book, TegBook


# Register your models here.
# admin.site.register(advertisements)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(TegBook)
class TegBookAdmin(admin.ModelAdmin):
    pass