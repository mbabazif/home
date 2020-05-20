from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request): 
    return render(request, 'index.html' )