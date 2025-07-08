from django import forms

class NewTestCaseForm(forms.Form):
    new_title = forms.CharField(label="Title", max_length=50)
    new_ts_action = forms.CharField(label="Action", max_length=300)
    new_ts_result = forms.CharField(label="Expected Result", max_length=300)

