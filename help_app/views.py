from django.shortcuts import render
from django.views import generic
from . import forms
from django.http.response import HttpResponse
from django.template.context_processors import csrf
from .models import Parents,Children,Houseworks,Tasks
# from django.contrib.staticfiles.templatetags.staticfiles import static

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
    parent_id = 1
    labels = ['こども','任せる仕事']
    # 入力結果を格納する辞書
    results = {}
    radios = {}
    ret = ''
    if request.method == 'POST':
        results[labels[0]] = request.POST.getlist("child")
        results[labels[1]] = request.POST.getlist("task")
        ret = 'OK'
        c = {'results': results,'ret':ret}

    else:
        form = forms.ChkForm()
        assign_houseworks = Houseworks.objects.filter(parent_id=1)
        choice1 = []
        for work in assign_houseworks:
            choice1.append((work, work.job_name))

        assign_children = Children.objects.filter(parent_id=1)
        choice2 = []
        i = 1
        for child in assign_children:
            choice2.append((i, child.name))
            print(child)
            i=i+1

        form.fields['child'].choices = choice2
        form.fields['child'].initial = ['1']
        # ここで一番目の子供を初期洗濯にしたいけど以下のコードではダメだった
        # form.fields['child'].initial = [assign_children[1]]
        form.fields['task'].choices = choice1
        # ここでinitialに、選択済みのタスクを入れられるようにしたい
        form.fields['task'].initial = ['0']

        c = {'form': form,'ret':ret}
        # CFRF対策（必須）
        c.update(csrf(request))
    return render(request, 'help_app/parent_assign.html', c)

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



