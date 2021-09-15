from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(max_length=50)
    age=forms.IntegerField(max_value=80)

class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)

class WebpageForm(forms.Form):
    topicname=forms.CharField(max_length=100)
    name=forms.CharField(max_length=100)
    url=forms.URLField(max_length=100)

class AccessForm(forms.Form):
    topicname=forms.CharField(max_length=100)
    name=forms.CharField(max_length=100)
    url=forms.URLField(max_length=100)
    date=forms.DateField()