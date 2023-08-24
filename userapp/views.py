from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import UserDetails

from userapp import models

# Create your views here.
def sayHello(request):
    return HttpResponse("Django Project is created & web page is executed")

def html_page(request):
   return render(request,"index.html")
   

def test_page(request):
     name=request.POST['your_name']
     template = loader.get_template('test.html')
     context = {
       'myname': name,
     }
     return HttpResponse(template.render(context, request))

     

def members(request):
  myusers = UserDetails.objects.all().values()
  template = loader.get_template('all_users.html')
  context = {
    'myusers': myusers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  myusers = UserDetails.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myusers': myusers,
  }
  return HttpResponse(template.render(context, request))



    

