from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("testcases/add/", views.add_test_case, name="add_testcase"),
    path("testcases/<int:test_case_id>/", views.display_test_case_detail, name="detail"),
]
