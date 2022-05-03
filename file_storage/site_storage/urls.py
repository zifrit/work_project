from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('save/', views.save_file, name='save_file'),
    path('book_list/', views.BookView.as_view()),
    path('book_list/<int:pk>/', views.BookDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)