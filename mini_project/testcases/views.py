from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Running the testcases app.")

def display_test_case_detail(request, test_case_id):
    return HttpResponse(f"You are looking at the details of Test Case {test_case_id}.")

def display_test_case_steps(request, test_case_id):
    return HttpResponse(f"You are looking at the test steps of Test Case {test_case_id}.")
