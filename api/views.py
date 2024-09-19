from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status  
from teacher.models import Teacher
from .serializers import TeacherSerializer
from trainers.models import Trainers
from .serializers import TrainersSerializer
from KICD.models import Kicd
from .serializers import KicdSerializer
from assessments.models import Assessment
from .serializers import AssessmentSerializer
from modules.models import Module
from .serializers import ModuleSerializer
from marking_scheme.models import MarkingScheme
from .serializers import MarkingSchemeSerializer

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            teachers = teachers.filter(first_name=first_name)  
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TrainerListView(APIView):
    def get(self, request):
        trainers = Trainer.objects.all()  
        first_name = request.query_params.get("first_name")
        if first_name: 
            trainers = trainers.filter(first_name=first_name) 
        serializer = TrainersSerializer(trainers, many=True) 
        return Response(serializer.data)

    def post(self, request):
        serializer = TrainerSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrainerDetailView(APIView): 
    def get(self, request, id):
        trainer = Trainer.objects.get(id=id) 
        serializer = TrainerSerializer(trainer)  
        return Response(serializer.data)

    def put(self, request, id):
        trainer = Trainer.objects.get(id=id) 
        serializer = TrainerSerializer(trainer, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        trainer = Trainer.objects.get(id=id) 
        trainer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class KicdListView(APIView):
    def get(self, request):
        kicds = Kicd.objects.all()  
        first_name = request.query_params.get("first_name")
        if first_name:
            kicds = kicds.filter(first_name=first_name) 
        serializer = KicdSerializer(kicds, many=True)  
        return Response(serializer.data)

    def post(self, request):
        serializer = KicdSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KicdDetailView(APIView):
    def get(self, request, id):
        kicd = Kicd.objects.get(id=id)  
        serializer = KicdSerializer(kicd)  
        return Response(serializer.data)

    def put(self, request, id):
        kicd = Kicd.objects.get(id=id) 
        serializer = KicdSerializer(kicd, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        kicd = Kicd.objects.get(id=id)  
        kicd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AssessmentListView(APIView):
    def get(self, request):
        assessments = Assessment.objects.all()
        serializer = AssessmentSerializer(assessments, many=True)  
        return Response(serializer.data)

    def post(self, request):
        serializer = AssessmentSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssessmentDetailView(APIView):
    def get(self, request, id):
        assessment = Assessment.objects.get(id=id)  
        serializer = AssessmentSerializer(assessment)  
        return Response(serializer.data)

    def put(self, request, id):
        assessment = Assessment.objects.get(id=id) 
        serializer = AssessmentSerializer(assessment, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        assessment = Assessment.objects.get(id=id) 
        assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ModuleListView(APIView):
    def get(self, request):
        modules = Module.objects.all()  
        serializer = ModuleSerializer(modules, many=True) 
        return Response(serializer.data)

    def post(self, request):
        serializer = ModuleSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModuleDetailView(APIView):
    def get(self, request, id):
        module = Module.objects.get(id=id)  
        serializer = ModuleSerializer(module) 
        return Response(serializer.data)

    def put(self, request, id):
        module = Module.objects.get(id=id)  
        serializer = ModuleSerializer(module, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response

class MarkingSchemeListView(APIView):
    def get(self, request):
        modules = MarkingScheme.objects.all()  
        serializer = MarkingSchemeSerializer(MarkingScheme, many=True) 
        return Response(serializer.data)

    def post(self, request):
        serializer = MarkingSchemeSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MarkingSchemeDetailView(APIView):
    def get(self, request, id):
        module = MarkingScheme.objects.get(id=id)  
        serializer = MarkingSchemeSerializer(module) 
        return Response(serializer.data)

    def put(self, request, id):
        module = MarkingScheme.objects.get(id=id)  
        serializer = MarkingSchemeSerializer(MarkingScheme, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response
