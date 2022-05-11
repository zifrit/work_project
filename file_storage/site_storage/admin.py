from django.contrib import admin
from .models import Book, TegBook


# Register your models here.
# admin.site.register(advertisements)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'book', 'teg')
    search_fields = ('title','teg')
    list_editable = ('teg','book','title')
    list_filter = ('teg',)
    pass

@admin.register(TegBook)
class TegBookAdmin(admin.ModelAdmin):
    pass