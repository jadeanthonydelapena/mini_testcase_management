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
    test_case = TestCase.objects.get(pk=test_case_id)
    test_case_steps = test_case.teststep_set.all()

    template = loader.get_template('testcases/test_case_detail.html')
    context = {'test_case' : test_case, 'test_case_steps' : test_case_steps}
    return HttpResponse(template.render(context, request))
