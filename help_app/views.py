from django.shortcuts import render
from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

def top(request):
    return render(request, 'help_app/top.html', {})

def login(request):
    return render(request, 'help_app/login.html', {})

def register(request):
    return render(request, 'help_app/register.html', {})


# def parent_top(request):
#     return render(request, 'help_app/parent_usersmanage.html', {})

def parent_tasklist(request):
    return render(request, 'help_app/parent_tasklist.html', {})

def parent_assign(request):
    return render(request, 'help_app/parent_assign.html', {})

def parent_taskregister(request):
    return render(request, 'help_app/parent_taskregister.html', {})

def parent_complete(request):
    return render(request, 'help_app/parent_complete.html', {})


# def child_top(request):
#     return render(request, 'help_app/child_top.html', {})

def child_tasklist(request):
    return render(request, 'help_app/child_tasklist.html', {})

def child_complete(request):
    return render(request, 'help_app/child_complete.html', {})

def child_history(request):
    return render(request, 'help_app/child_history.html', {})


def certification(request):
    return render(request, 'help_app/certification.html', {})

def parent_usersmanage(request):
    return render(request, 'help_app/parent_usersmanage.html', {})
#
# def (request):
#     return render(request, 'help_app/.html', {})



