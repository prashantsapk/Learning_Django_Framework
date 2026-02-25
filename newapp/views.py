from django.shortcuts import render
from .models import Newappvarity
from django.shortcuts import get_object_or_404


def newapp(request):
    chais= Newappvarity.objects.all
    return render(request,'website/new.html',{'chais':chais})

def newappdescription(request,chai_id):
    chai= get_object_or_404(Newappvarity,pk=chai_id)
    return render(request,'website/details.html',{'chai':chai})

# Create your views here.
