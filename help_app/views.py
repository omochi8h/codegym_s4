from django.shortcuts import render, redirect
from django.views import generic
from . import forms
from django.http.response import HttpResponse
from django.template.context_processors import csrf
from .models import Parents,Children,Houseworks,Tasks
import datetime
from django.utils import timezone
from django.http import Http404
# from django.contrib.staticfiles.templatetags.staticfiles import static

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

def top(request):
    return render(request, 'help_app/top.html', {})

def login(request):
    return render(request, 'help_app/login.html', {})

def register(request):
    return render(request, 'help_app/register.html')


# def parent_top(request):
#     return render(request, 'help_app/parent_usersmanage.html', {})

def parent_tasklist(request):
    tasklist_houseworks = Houseworks.objects.filter(parent_id=1)
    return render(request, 'help_app/parent_tasklist.html', {'tasks': tasklist_houseworks})

# POSTのあとparent_assignにいくのができない
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
        # c = {'results': results,'ret':ret}
        # results[labels[0]] = request.POST.getlist("child")
        # results[labels[1]] = request.POST.getlist("task")
        print(results[labels[1]])
        print(results[labels[0]])
        # child_result = results[labels[0]]
        for result in results[labels[1]]:
            print(result)
            Tasks(child_id=int(results[labels[0]][0]), parent_id=1, work_id=int(result), comment='こんにちは').save()
        return render(request, 'help_app/parent_assign.html')


    else:
        form = forms.ChkForm()
        assign_houseworks = Houseworks.objects.filter(parent_id=1)
        choice1 = []
        for work in assign_houseworks:
            choice1.append((work.id, work.job_name))

        assign_children = Children.objects.filter(parent_id=1)
        choice2 = []
        i = 1
        for child in assign_children:
            choice2.append((child.id, child.name))
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


def parent_taskregister(request,pk):
    try:
        houseworks = Houseworks.objects.get(pk=pk)
    except Houseworks.DoesNotExist:
        raise Http404

    if request.method == "POST":
        houseworks.job_name = request.POST["job_name"]
        houseworks.save()
        # return redirect(view_article,pk)
        return render('help_app/parent_tasklist.html', {})
        # return  redirect('parent_tasklist/')
    context = {"housework": houseworks}

    return render(request, 'help_app/parent_taskregister.html', context)

def task_delete(request,pk):
    try:
        housework = Houseworks.objects.get(pk=pk)
    except Houseworks.DoesNotExist:
        raise Http404
    housework.delete()
    return redirect(parent_tasklist())

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



