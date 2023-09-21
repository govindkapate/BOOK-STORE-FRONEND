from django.shortcuts import render,HttpResponse


# Create your views here.

def index(request):
    #return HttpResponse("this is home page")
    context={
        "variable":"This is Don",
        "name":"Govind"
    }
 
    return render(request,'index.html',context)


def about(request):
    #return HttpResponse("this is about home page")
    return render(request,'about.html')

def services(request):
    #return HttpResponse("this is service page")
    return render(request,'services.html')

def contact(request):
    #return HttpResponse("this is contact for more services")
    return render(request,'contact.html')


