from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect(reverse('blog_app:blog_list'))