from urllib import request

from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import activate_user, SignUpForm, AddChild, AddWork
from help_app.models import *
from django.http import HttpResponse, HttpRequest

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from . import forms
from django.http.response import HttpResponse
from django.template.context_processors import csrf
from .models import Parents, Children, Houseworks, Tasks, Days_comment, Comment
import datetime
from datetime import date
from django.utils import timezone
from django.http import Http404

import json



from django.shortcuts import render
from django.views import generic
import datetime

# from django.contrib.staticfiles.templatetags.staticfiles import static



# Create your views here.
"""
class IndexView(generic.TemplateView):
    form = AddChild
    template_name = "registration/index.html"
    child = Children.objects.all()
"""


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ActivateView(TemplateView):
    template_name = "registration/activate.html"

    def get(self, request, uidb64, token, *args, **kwargs):
        result = activate_user(uidb64, token)
        return super().get(request, result=result, **kwargs)


def index(request):
    params = {'name': '', 'on_user': request.user, 'children': Children.objects.filter(parent=request.user).all(),
              'form': None}
    if request.method == 'POST':
        form = AddChild(request.POST)
        params['name'] = request.POST['name']
        params['form'] = form
        if params['name'] != '':
            child = Children()
            child.name = params['name']
            child.parent = params['on_user']
            child.save()
    else:
        params['form'] = AddChild()
    return render(request, 'registration/index.html', params)


def addwork(request):
    params = {'name': '', 'on_user': request.user, 'works': Houseworks.objects.filter(parent=request.user).all(),
              'point': '',
              'form': None}
    if request.method == 'POST':
        form = AddChild(request.POST)
        params['name'] = request.POST['name']
        params['point'] = request.POST['point']
        params['form'] = form
        if params['name'] != '':
            new_work = Houseworks()
            new_work.job_name = params['name']
            new_work.parent = params['on_user']
            new_work.point = params['point']
            new_work.save()
        return redirect(parent_tasklist)
    else:
        params['form'] = AddWork()
    return render(request, 'registration/addwork.html', params)


def newwork(request):
    params = {'name': '', 'point': ''}
    if request.method == 'POST':
        form = AddWork(request.POST)
        params['name'] = request.POST['name']
        params['point'] = request.POST['point']
        params['form'] = form
    return render(request, 'registration/newwork.html', params)

def child_page(request):
    params = {}
    data = {}
    if request.method == 'POST':
        update_id = request.POST['complete_id']
        task = Tasks.objects.filter(id=update_id).first()
        task.state = -1
        task.save()

    child_data = []
    params['children'] = Children.objects.filter(parent=request.user).all()
    for child in params.get('children'):
        child_list = []
        child_list.append(child.name)
        today = datetime.date.today()
        task_list = []
        tasks = Tasks.objects.filter(parent=request.user, child=child.id, state=0, date=today).all()
        comments = Comment.objects.filter(parent=request.user, child=child.id, date=today).all()
        for task in tasks:
            task_list.append(task)
        child_list.append(task_list)
        child_list.append(comments)
        child_data.append(child_list)
    data['children'] = child_data

    return render(request, 'registration/child_tasklist.html', data)


############

# Create your views here.

        #return render(request, 'registration/addwork.html', params)


class IndexView(generic.TemplateView):
    template_name = "index.html"


def parent_tasklist(request):
    tasklist_houseworks = Houseworks.objects.filter(parent_id=request.user.id)
    return render(request, 'help_app/parent_tasklist.html', {'tasks': tasklist_houseworks})
    # return render(request, 'help_app/parent_tasklist.html', {})


# POSTのあとparent_assignにいくのができない
def parent_assign(request):
    if Houseworks.objects.filter(parent=request.user).all().count() == 0:
        default_work1 = Houseworks()
        default_work1.job_name = 'お皿洗い'
        default_work1.point = 3
        default_work1.parent = request.user
        default_work1.save()

        default_work2 = Houseworks()
        default_work2.job_name = 'お片付け'
        default_work2.point = 3
        default_work2.parent = request.user
        default_work2.save()

    dataset = {}
    labels = ['こども', '任せる仕事','コメント']
    # 入力結果を格納する辞書
    results = {}
    radios = {}
    ret = ''
    if request.method == 'POST':

        results[labels[0]] = request.POST.getlist("child")
        results[labels[1]] = request.POST.getlist("task")
        results[labels[2]]  = request.POST['text']
        ret = 'OK'
        c = {'results': results, 'ret': ret}
        # print(results[labels[1]])
        print(results[labels[0]])
        # child_result = results[labels[0]]

        # 今日既に割り振ったタスクを消去
        old_task = Tasks.objects.filter(child_id=int(results[labels[0]][0]),parent_id=request.user.id,date=date.today())
        print(old_task)
        old_task.delete()

        if Comment.objects.filter(parent_id=request.user.id,child_id=int(results[labels[0]][0]),date=date.today()).count() > 0:
            old_comment = Comment.objects.filter(parent_id=request.user.id,child_id=int(results[labels[0]][0]),date=date.today())
            old_comment.delete()

        Comment(parent_id=request.user.id,child_id=int(results[labels[0]][0]),comment=results[labels[2]]).save()

        for result in results[labels[1]]:
            print(result)
            Tasks(child_id=int(results[labels[0]][0]), parent_id=request.user.id, work_id=int(result)).save()
        return redirect(parent_assign)
        # return render(request, 'help_app/parent_assign.html', c)
    else:

        form = forms.ChkForm()
        assign_houseworks = Houseworks.objects.filter(parent_id=request.user.id)
        choice1 = []
        for work in assign_houseworks:
            choice1.append((work.id, work.job_name))

        assign_children = Children.objects.filter(parent_id=request.user.id)
        choice2 = []

        comment_data = {}
        # 子供に割り振られたタスクのデータ化
        for child in assign_children:
            data = []
            choice2.append((child.id, child.name))
            init_tasks = Tasks.objects.filter(child_id=child.id,date=date.today())
            for task in init_tasks:
                for housework in assign_houseworks:
                    if task.work_id == housework.id:
                        data.append(housework.id)
            dataset[child.id] = data
            print(dataset)
            comments = Comment.objects.filter(child_id=child.id,date=date.today())
            # if comment:
            for comment in comments:
                print(comment.comment)
                comment_data[child.id] = comment.comment
                print(comment_data)

        form.fields['child'].choices = choice2
        # form.fields['child'].initial = [assign_children[0].id]
        form.fields['task'].choices = choice1
        # ここでinitialに、選択済みのタスクを入れられるようにしたい
        tasklist = Tasks.objects.filter(parent_id=request.user.id, state=-1).values()
        form.fields['task'].initial = ['0']

        if Children.objects.filter(parent=request.user).all().count() == 0:
            count = 0
        else:
            count = 1


        c = {'form': form, 'ret': ret, 'dataset': json.dumps(dataset), 'count': count, 'comment_data': json.dumps(comment_data)}
        # CFRF対策（必須）
        c.update(csrf(request))
        return render(request, 'help_app/parent_assign.html', c)


def parent_taskregister(request, pk):
    try:
        houseworks = Houseworks.objects.get(pk=pk)
    except Houseworks.DoesNotExist:
        raise Http404

    if request.method == "POST":
        houseworks.job_name = request.POST["job_name"]
        houseworks.save()
        return redirect(parent_tasklist)
    else:
        context = {"housework": houseworks}
        return render(request, 'help_app/parent_taskregister.html', context)


def parent_task_delete(request, pk):
    try:
        housework = Houseworks.objects.get(pk=pk)
    except Houseworks.DoesNotExist:
        raise Http404
    housework.delete()
    return redirect(parent_tasklist)


def parent_complete(request):
    return render(request, 'help_app/parent_complete.html', {})


def child_tasklist(request):
    return render(request, 'help_app/child_tasklist.html', {})


def child_complete(request):
    return render(request, 'help_app/child_complete.html', {})


def child_history(request):
    params = {}

    today = datetime.date.today()
    year = today.year
    month = today.month
    firstDay = str(year) + '-' + str(month) + '-' + '01'
    last = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
    lastDay = str(year) + '-' + str(month) + '-' + str(last.day)
    dayCount = int(last.day)

    all_data = []
    children = Children.objects.filter(parent=request.user).all()
    for child in children:
        child_data = []
        child_data.append(child.name)
        child_data.append(0)
        child_data.append(0)
        child_data.append(0)

        task_all = Tasks.objects.filter(parent=request.user, child=child.id, state=1)
        for point in task_all:
            child_data[1] += point.work.point

        task_month = Tasks.objects.filter(parent=request.user, child=child.id, state=1, date__gte=firstDay,
                                          date__lte=lastDay)
        for point in task_month:
            child_data[2] += point.work.point

        task_today = Tasks.objects.filter(parent=request.user, child=child.id, state=1, date=today)
        for point in task_today:
            child_data[3] += point.work.point

        task_data = []
        for i in range(dayCount):
            task_data.append(0)
        tasks = Tasks.objects.filter(parent=request.user, child=child.id, state=1, date__gte=firstDay,
                                     date__lte=lastDay)
        for task in tasks:
            day = int(task.date.day) - 1
            if task_data[day] == 0:
                task_data[day] = []
                task_name = task.work.job_name
                task_data[day].append(task_name)
            else:
                task_name = task.work.job_name
                task_data[day].append(task_name)
        child_data.append(task_data)
        all_data.append(child_data)
    params['histry'] = all_data
    return render(request, 'help_app/child_history.html', params)


def certification(request):
    return render(request, 'help_app/certification.html', {})

def parent_userslist(request):
    params = {'name': '', 'on_user': request.user, 'children': Children.objects.filter(parent=request.user).all()}
    return render(request, 'help_app/parent_userslist.html', params)

def parent_usersmanage(request):
    params = {'name': '', 'on_user': request.user, 'children': Children.objects.filter(parent=request.user).all(),
              'form': None}
    if request.method == 'POST':
        form = AddChild(request.POST)
        params['name'] = request.POST['name']
        params['form'] = form
        if params['name'] != '':
            child = Children()
            child.name = params['name']
            child.parent = params['on_user']
            child.save()
        return redirect(parent_userslist)
    else:
        params['form'] = AddChild()
        return render(request, 'help_app/parent_usersmanage.html', params)
    # return render(request, 'help_app/parent_usersmanage.html', params)
    # return render(request, 'help_app/parent_usersmanage.html', {})

def parent_usersedit(request, pk):
    try:
        child = Children.objects.get(pk=pk)
    except Children.DoesNotExist:
        raise Http404

    if request.method == "POST":
        child.name = request.POST["name"]
        child.save()
        return redirect(parent_userslist)
    else:
        context = {"child": child}
        return render(request, 'help_app/parent_usersedit.html', context)

def parent_users_delete(request, pk):
    try:
        child = Children.objects.get(pk=pk)
    except Children.DoesNotExist:
        raise Http404
    child.delete()
    return redirect(parent_userslist)

def parent_approval(request):
    tasklist = Tasks.objects.filter(parent_id=request.user.id,state=-1).values()
    childlist = Children.objects.filter(parent_id=request.user.id).values()
    houseworklist = Houseworks.objects.filter(parent_id=request.user.id).values()
    count = {}
    for child in childlist:
        if Tasks.objects.filter(parent_id=request.user.id, child_id=child['id'] ,state=-1).all().count() == 0:
            count[child['id']] = 0
        else:
            count[child['id']] = 1
    return render(request, 'help_app/parent_approval.html', {'tasks': tasklist, 'children': childlist,'houseworks':houseworklist, 'count': count})

def parent_approval_on(request, pk):
    try:
        task = Tasks.objects.get(pk=pk)
    except Tasks.DoesNotExist:
        raise Http404
    task.state = 1
    task.save()
    return redirect(parent_approval)
#
# def (request):
#     return render(request, 'help_app/.html', {})




