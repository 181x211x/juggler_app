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
from django.contrib.auth.models import User
from .models import Record
from django.shortcuts import redirect
from . import forms, models


# Create your views here.


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

@csrf_exempt
def top(request):
    record = {
        'records': Record.objects.all(),
    }

    return render_to_response('record/top.html',record)


def record_forms(request):
    form = forms.RecordForm(request.POST or None)
    if form.is_valid():
        models.Record.objects.create(**form.cleaned_data)
        return redirect('http://localhost:8000/top/templates')
    d = {
        'form': forms.RecordForm(),
    }
    return render(request, 'record/create.html', d)
