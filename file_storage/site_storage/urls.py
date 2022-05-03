from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('save/', views.save_file, name='save_file'),
]
urlpatterns = format_suffix_patterns(urlpatterns)