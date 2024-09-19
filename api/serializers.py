from rest_framework import serializers
from trainers.models import Trainers
from KICD.models import Kicd 
from teacher.models import Teacher
from assessments.models import Assessment
from modules.models import Module
from marking_scheme.models import MarkingScheme


class TrainersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainers
        fields = "__all__"

class KicdSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Kicd  
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class AssessmentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Assessment  
        fields = "__all__"

class ModuleSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Module  
        fields = "__all__"

class MarkingSchemeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = MarkingScheme 
        fields = "__all__"
