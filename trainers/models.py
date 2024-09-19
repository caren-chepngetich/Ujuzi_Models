from django.db import models

class Trainers(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    tsc_number = models.IntegerField()
    email = models.EmailField()
    region = models.CharField(max_length=50) 
    tsc_number = models.IntegerField()  

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
