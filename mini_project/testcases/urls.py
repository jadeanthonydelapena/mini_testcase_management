from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("testcases/<int:test_case_id>/", views.display_test_case_detail, name="detail"),
    path('testcases/add-test-case/', views.add_new_test_case, name="add-new-test-case"),
    # path('testcases/add-test-case/', views.dummy, name="add-new-test-case"),
    path('testcases/add-test-case/success-add-test-case/', views.success_add_test_case, name="success-add-test-case"),
]
