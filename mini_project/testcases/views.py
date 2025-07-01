from django.shortcuts import render
from django.http import HttpResponse
from .models import TestCase


def index(request):
    recent_test_cases = TestCase.objects.order_by("-date_created")
    output = f" - ".join([t.title for t in recent_test_cases])
    return HttpResponse(output)

def display_test_case_detail(request, test_case_id):
    return HttpResponse(f"You are looking at the details of Test Case {test_case_id}.")

def display_test_case_steps(request, test_case_id):
    # return HttpResponse(f"You are looking at the test steps of Test Case {test_case_id}.")
    target_test_case = TestCase.objects.get(pk=test_case_id)
    target_test_steps = target_test_case.teststep_set.all()
    output = " ".join([f"{step.action}: {step.expected_result}" for step in target_test_steps])

    return HttpResponse(output)