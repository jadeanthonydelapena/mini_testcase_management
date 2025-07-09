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
    context = { 'test_case_id': f"{test_case.id:03}", 'test_case' : test_case, 'test_case_steps' : test_case_steps}
    return HttpResponse(template.render(context, request))

def add_new_test_case(request):
    if request.method == "POST":
        actions = []
        results = []
        title = None

        for key, value in request.POST.items():
            if 'title' in key:
                title = value
            elif key.startswith('step_action'):
                actions.append(value)
            elif key.startswith('step_result'):
                results.append(value)

        t = TestCase(title=title, owner="Jade De la Pena", date_created=timezone.now())
        t.save()

        for i in range(len(actions)):
            t.teststep_set.create(action=actions[i], expected_result=results[i])

        return HttpResponseRedirect('success-add-test-case/')
    
    else:
        template = loader.get_template('testcases/add_test_case.html')
        return HttpResponse(template.render({}, request))


def success_add_test_case(request):
    return HttpResponse("Test Case Added Successfully.")
