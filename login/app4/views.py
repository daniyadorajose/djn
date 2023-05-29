from django.shortcuts import render
from.forms import todoform
from.models import tbl


# Create your views here.

def func(request):
    form=todoform()
    t=tbl.objects.all()
    if request.method=='POST':
        form= todoform(request.method)
        if form.is_valid():
            form.save()

        
    return render (request,'index.html',{'fo':form,'todo':t})





