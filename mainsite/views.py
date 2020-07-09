from django.shortcuts import render


def index(request):
    context = {}
    return render(request,'mainsite/index.html',context)
