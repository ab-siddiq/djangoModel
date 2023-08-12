# djangoModel
# Create superuser
```python
 py manage.py createsuperuser
```
# Register model
```django
from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Student)
```
# Show data except obhect in database
```django
from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=30)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.TextField(default="Md. Sohrab Ali")
    # show data
    def __str__(self) -> str:
        return f"Roll: {self.roll}, Name: {self.name}"
```
# Pass data from view to show in frontend
```django
from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    student = models.Student.objects.all()
    return render(request,"home.html",{"studentData":student})
```
