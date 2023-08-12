from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=30)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.TextField(default="Md. Sohrab Ali")
    
    def __str__(self) -> str:
        return f"Roll: {self.roll}, Name: {self.name}"