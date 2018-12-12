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


# Create your views here.


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

@csrf_exempt
def top(request):
    return render_to_response('record/top.html')
