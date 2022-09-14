from django.shortcuts import render, redirect
from mymovie.models import NoticeTab
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import HttpResponseRedirect


def mainFunc(request):
        
    return render(request, 'main.html')