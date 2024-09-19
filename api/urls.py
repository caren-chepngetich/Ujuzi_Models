
from django.urls import path
from .views import TeacherListView
from .views import TrainerListView
from .views import KicdListView
from .views import AssessmentListView
from .views import ModuleListView
from .views import MarkingSchemeListView
from.views import TeacherDetailView
from.views import TrainerDetailView
from.views import KicdDetailView
from.views import AssessmentDetailView
from.views import ModuleDetailView
from.views import MarkingSchemeDetailView



urlpatterns =[
    path("trainers/",TrainerListView.as_view(),name="trainer_list_view"),
    path('teachers/<int:id>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('trainers,/<int:id>/', TrainerDetailView.as_view(), name='teacher-detail'),
    path('assessment/<int:id>/', AssessmentDetailView.as_view(),name="Assessment_detail_view"),
    path("teacher/", TeacherListView.as_view(),name="teacher_list_view"),
    path("KICD/", KicdListView.as_view(),name="kicdoflficia_list_view"),
    path('KICD/<int:id>/', KicdDetailView.as_view(), name='teacher-detail'),
    path("assessment/",AssessmentListView.as_view(),name="assessment_list_view"),
    path("module", ModuleListView.as_view(),name="module_list_view"),
    path("module", ModuleDetailView.as_view(),name="module_detail_view"),
    path("marking/", MarkingSchemeListView.as_view(),name="Markingscheme_detai_view"),
    path("markingscheme/", MarkingSchemeDetailView.as_view(),name="Markingscheme_detail_view"),

]