from django.shortcuts import render

# Create your views here.
def myHomeView(request,*args,**kwargs):
	return render(request,"home/index.html")