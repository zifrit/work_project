from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import generics
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, TegBook
from . import serializers


# Create your views here.


class BookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.Bookserializers


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.Bookserializers


class user_login(View):
    def post(self, request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponse('Authenticated successfully')
                    else:
                        return HttpResponse('Disabled account')
                else:
                    return HttpResponse('Invalid login')
        else:
            form = LoginForm()
        return render(request, 'site_storage/login.html', {'form': form})

    def get(self, request):
        form = LoginForm()
        return render(request, 'site_storage/login.html', {'form': form})


class save_file(LoginRequiredMixin,View):
    def post(self, request):
        if request.method == 'POST' and request.FILES:
            file = request.FILES['myfile1']
            teg_save_file = str(file).split('.')
            teg_save_file = '.' + teg_save_file[1]
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

    def get(self, request):
        return render(request, 'site_storage/dowload_site.html', {})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'site_storage/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'site_storage/register.html', {'user_form': user_form})