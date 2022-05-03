from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models import Book

# Create your views here.


def save_file(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        # print(f'первый принт{file}')
        # print(f'второй принт{fs}')
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        # print(f'третий принт{file_url}')
        return render(request, 'site_storage/dowload_site.html', {
            'file_url': file_url
        })
    return render(request, 'site_storage/dowload_site.html', {})