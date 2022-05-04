from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from rest_framework import generics

from .models import Book, TegBook
from . import serializers

# Create your views here.


def save_file(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['myfile1']
        teg_save_file = str(file).split('.')
        teg_save_file = '.'+teg_save_file[1]
        fs = FileSystemStorage()
        # print(f'первый принт{file}')
        # print(f'второй принт{fs}')
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        # print(f'третий принт{file_url}')
        if TegBook.objects.filter(name__startswith=teg_save_file):
            print(True)
        else:
            TegBook.objects.create(name=teg_save_file)
            print(False)
        for i in TegBook.objects.all():
            if i.name == teg_save_file:
                Book.objects.create(title='some title', book=f'/{str(file)}', user=request.user,
                                    teg=TegBook.objects.get(id=i.id))
        return render(request, 'site_storage/dowload_site.html', {
            'file_url': file_url
        })
    return render(request, 'site_storage/dowload_site.html', {})


class BookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.Bookserializers

class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.Bookserializers