from django.db import models



class Assessment(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    kicd_id = models.IntegerField(default=1)
    teachers_id = models.IntegerField()
    teachers_grade = models.IntegerField()
    assessment_duration = models.DateTimeField(auto_now_add=True)
    assessment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.assessment_date} {self.assessment_duration}'
    <           
    ````````````````````````````````````````````````````````````



    ``````````