from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=30)
    roll = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    # show data
    def __str__(self) -> str:
        return f"Roll: {self.roll}, Name: {self.name}"