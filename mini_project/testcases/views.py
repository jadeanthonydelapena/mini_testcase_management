from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TestCase


def index(request):
    test_cases_all = TestCase.objects.all()
    template = loader.get_template('testcases/index.html')
    context = {'test_cases_list': test_cases_all}
    return HttpResponse(template.render(context, request))

def display_test_case_detail(request, test_case_id):
    return HttpResponse(f"You are looking at the details of Test Case {test_case_id}.")

def display_test_case_steps(request, test_case_id):
    # return HttpResponse(f"You are looking at the test steps of Test Case {test_case_id}.")
    target_test_case = TestCase.objects.get(pk=test_case_id)
    target_test_steps = target_test_case.teststep_set.all()
    output = " ".join([f"{step.action}: {step.expected_result}" for step in target_test_steps])

    return HttpResponse(output)