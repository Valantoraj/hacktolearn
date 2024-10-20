from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("disease/",views.disease,name="disease"),
    path("mental/",views.mental,name="mental"),
    path("hospitals_nearby/",views.hospitals_nearby,name="hospitals_nearby"),
    path("blood_cancer/",views.blood_cancer,name="blood_cancer"),
    path("brain_cancer/",views.brain_cancer,name="brain_cancer"),
    path("kidney_cancer/",views.kidney_cancer,name="kidney_cancer"),
    path("lung_cancer/",views.lung_cancer,name="lung_cancer"),
    path("skin_cancer/",views.skin_cancer,name="skin_cancer"),
    path("result/",views.result,name="result"),
]