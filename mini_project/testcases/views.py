from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import TestCase, TestStep
from .forms import NewTestCaseForm


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

def add_new_test_case(request):
    if request.method == "POST":
        form = NewTestCaseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            t = TestCase(title=data['new_title'], owner="Jade De la Pena", date_created=timezone.now())
            t.save()

            t.teststep_set.create(action=data['new_ts_action'], expected_result=data['new_ts_result'])
            
            return HttpResponseRedirect('success-add-test-case/')
    else:
        form = NewTestCaseForm()

    template = loader.get_template('testcases/add_test_case.html')
    context = {"form": form}
    return HttpResponse(template.render(context, request))


def success_add_test_case(request):
    return HttpResponse("Test Case Added Successfully.")
