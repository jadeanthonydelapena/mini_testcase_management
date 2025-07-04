from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("testcases/<int:test_case_id>/", views.display_test_case_detail, name="detail"),
]
