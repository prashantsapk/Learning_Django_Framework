from django.shortcuts import render
from .models import Newappvarity,store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm


def newapp(request):
    chais= Newappvarity.objects.all
    return render(request,'website/new.html',{'chais':chais})

def newappdescription(request,chai_id):
    chai= get_object_or_404(Newappvarity,pk=chai_id)
    return render(request,'website/details.html',{'chai':chai})

def chai_store_view(request):
    stores=None
    if request.method == 'POST':
        form=ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety=form.cleaned_data['chai_varity']
            store.objects.filter(chai_varieties=chai_variety)
    else:
        form=ChaiVarityForm()


    return render(request,'website/chai_stores.html',{'stores':stores,'form':form})

# Create your views here.