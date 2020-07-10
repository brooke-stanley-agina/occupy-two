from django.shortcuts import render


def index(request):
    context = {}
    return render(request,'mainsite/index.html',context)


def about_page(request):
    context = {}
    return render(request,'mainsite/about.html',context)

def activities(request):
    context = {}
    return render(request,'mainsite/activities.html',context)