from django.shortcuts import render
from .models import Record
from .serializer import RecordSerializer
from rest_framework import viewsets
from django.http.response import HttpResponse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from . import forms, models
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Avg, Max, Min, Count





# Create your views here.




class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


def home(request):
    if request.user.is_authenticated:
        return HttpResponse("login")
    else:
        return HttpResponse("logout")


def top(request):
    record = {
        'records': Record.objects.all().order_by('-date'),
    }
    return render(request,'record/top.html',record)


def record_forms(request):
    form = forms.RecordForm(request.POST or None)
    d = {
        'form': forms.RecordForm(initial = {
        'name': request.user.username}),
    }
    if form.is_valid():
        models.Record.objects.create(**form.cleaned_data)
        return redirect('http://localhost:8000/top/templates')

    return render(request, 'record/create.html', d)


class SignUp(CreateView):
    form_class = UserCreationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://localhost:8000/top/templates')
        return render(request, 'record/signup.html', {'form': form})


def all_record(request):
    record = {
        'records': Record.objects.all().order_by('-date'),
    }
    return render(request,'record/all_record.html',record)

def result(request):

    d = {
        'form': forms.Result(),
    }

    post_pks = request.POST.getlist('delete')
    if len(post_pks) != 0:  # <input type="checkbox" name="delete"のnameに対応
        Record.objects.filter(pk__in=post_pks).delete()
        return render(request,'record/result.html',d)  # 一覧ページにリダイレクト

    form = forms.Result(request.POST or None)
    if form.is_valid():
        if form.cleaned_data['tool'] == "全ての道具" and form.cleaned_data['skill'] == "":
            record = {
                'records': Record.objects.all().filter(name__contains=request.user.username).order_by('-date'),
                'form': forms.Result(),
                }
        elif form.cleaned_data['tool'] != "全ての道具" or form.cleaned_data['skill'] == "":
            record = {
                'records': Record.objects.all().filter(tool__contains=form.cleaned_data['tool'], name__contains=request.user.username).order_by('-date'),
                'form': forms.Result(),
            }
        elif form.cleaned_data['tool'] == "全ての道具" or form.cleaned_data['skill'] != "":
            record = {
                'records': Record.objects.all().filter(skill__contains=form.cleaned_data['skill'], name__contains=request.user.username).order_by('-date'),
                'form': forms.Result(),
            }
        else:
            record = {
                'records': Record.objects.all().filter(tool__contains=form.cleaned_data['tool'],skill__contains=form.cleaned_data['skill'], name__contains=request.user.username).order_by('-date'),
                'form': forms.Result(),
            }
        return render(request,'record/result.html',record)



    return render(request, 'record/result.html', d)





def rank(request):
    d = {
        'form': forms.Rank(),
    }

    post_pks = request.POST.getlist('delete')
    if len(post_pks) != 0:  # <input type="checkbox" name="delete"のnameに対応
        Record.objects.filter(pk__in=post_pks).delete()
        return render(request,'record/rank.html',d)  # 一覧ページにリダイレクト

    form = forms.Rank(request.POST or None)
    if form.is_valid():

        record = {
                'records': Record.objects.all().filter(tool__contains=form.cleaned_data['tool'],skill__contains=form.cleaned_data['skill'],num__contains=form.cleaned_data['num'] ).order_by('-count'),
                'form': forms.Rank(),
                'rank': range(100),
        }
        return render(request,'record/rank.html',record)



    return render(request, 'record/rank.html', d)
