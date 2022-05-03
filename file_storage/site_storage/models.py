from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def user_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Book(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to=user_directory_path, null=True, default=None)
    teg = models.ForeignKey(to='TegBook', null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'FileBook'

class TegBook(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'TegBook'

    def __str__(self):
        return self.name