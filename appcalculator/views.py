from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render, redirect  
from .forms import FeatureForm,AppcalculatorForm
from .models import Appcalculator,Feature
from django.http import HttpResponse
import json
# Create your views here.  
def app(request):  
    form=AppcalculatorForm()
    print(form)
    return render(request,'index.html',{'form':form}) 
def api(request):  
     if request.method == "POST":  
       category_id= request.POST['category_id']
       mainlist=[]
       feature=Feature.objects.filter(category=category_id)
       for i in feature:
           newlist=[]
           newlist.append(i.feature)
           newlist.append(i.hours)
           mainlist.append(newlist)
       return HttpResponse(json.dumps(mainlist), content_type="application/json")
                  
     else:   
        form=AppcalculatorForm()
        return render(request,'index.html',{'form':form})  
 
     
  

