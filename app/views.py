from app.models import Topic
from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *
# Create your views here.

def fun_student(request):
    form=StudentForm()
    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'first.html',context={'form':form})

def fun_topic(request):
    form=TopicForm()
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            topic=request.POST['topic_name']
            t=Topic.objects.get_or_create(topic_name=topic)[0]
            t.save()
            return HttpResponse('Inserted Sucessfully')
    return render(request,'topic.html',context={'form':form})

def fun_webpage(request):
    form=WebpageForm()
    if request.method=='POST':
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            tn=request.POST['topicname']
            n=request.POST['name']
            url=request.POST['url']
            t=Topic.objects.get_or_create(topic_name=tn)[0] 
            t.save()
            w=Webpage.objects.get_or_create(topic_name=t,name=n,url=url)[0]
            w.save()
            return HttpResponse('Inserted Sucessfully')
    return render(request,'webpage.html',context={'form':form})

def fun_access(request):
    form=AccessForm()
    if request.method=='POST':
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            tn=request.POST['topicname']
            n=request.POST['name']
            u=request.POST['url']
            d=request.POST['date']
            t=Topic.objects.get_or_create(topic_name=tn)[0] 
            t.save()
            w=Webpage.objects.get_or_create(topic_name=t,name=n,url=u)[0]
            w.save()
            a=Access_Record.objects.get_or_create(name=w,date=d)[0]
            a.save()
            return HttpResponse('Inserted Sucessfully')
    return render(request,'access.html',context={'form':form})