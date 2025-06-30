from django.db import models


class TestCase(models.Model):
    title = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    date_created = models.DateField('Date Created')

    def __str__(self):
        return self.title


class TestStep_Result(models.TextChoices):
    NOT_RUN = 'notrun', 'Not Run'
    PASS = 'pass', 'Pass'
    FAIL = 'fail', 'Fail'

class TestStep(models.Model):
    action = models.CharField(max_length=200)
    expected_result = models.CharField(max_length=200)
    result = models.CharField(max_length=10, choices=TestStep_Result.choices, default=TestStep_Result.NOT_RUN)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.action} : {self.expected_result}'
    



