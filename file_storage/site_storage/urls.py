from django.urls import path

from file_storage import settings
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


from django.conf.urls.static import static

urlpatterns = [
    path('save/', views.save_file.as_view(), name='save_file'),
    path('book_list/', views.BookView.as_view()),
    path('book_list/<int:pk>/', views.BookDetail.as_view()),
    path('login/', views.user_login.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('', views.user_login.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)