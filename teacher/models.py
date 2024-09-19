from django.db import models

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    kicd_id = models.PositiveSmallIntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    region = models.CharField(max_length=50)  
    tsc_number = models.IntegerField()  
    school = models.CharField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
