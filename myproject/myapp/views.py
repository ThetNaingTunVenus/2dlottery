from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views.generic import TemplateView, View
# Create your views here.
from.models import *
class Test(View):
    def get(self,request):
        return HttpResponse("hello world")