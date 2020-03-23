from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em> My Second App </em>")

def help(request):
    my_dict = {'insert_me':'Hello I am coming from help/help.html'}
    return render(request,'help/help.html',context=my_dict)

