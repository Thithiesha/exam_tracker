from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_score/', views.add_exam_score, name='add_score'),
    path('add-subject/', views.add_subject, name='add_subject'),
    path('add-exam-score/', views.add_exam_score, name='add_exam_score'),
    path('subject/<int:subject_id>/', views.subject_detail, name='subject_detail'),
]
