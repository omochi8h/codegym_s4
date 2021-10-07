from django.urls import path
from . import views

app_name = 'help_app'
urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path('', views.top, name='top'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),

    # path('parent_top', views.parent_top, name='parent_top'),
    path('parent_tasklist/', views.parent_tasklist, name='parent_tasklist'),
    path('parent_assign', views.parent_assign, name='parent_assign'),

    # path('parent_taskregister', views.parent_taskregister, name='parent_taskregister'),
    path('parent_taskregister/<int:pk>/', views.parent_taskregister, name='parent_taskregister'),
    path('parent_usersmanage', views.parent_usersmanage, name='parent_usersmanage'),
    path('parent_complete', views.parent_complete, name='parent_complete'),

    # path('child_top', views.child_top, name='child_top'),
    path('child_tasklist', views.child_tasklist, name='child_tasklist'),
    path('child_complete', views.child_complete, name='child_complete'),
    path('child_history', views.child_history, name='child_history'),
    path('certification', views.certification, name='certification'),

    # path('', views., name=''),
    # path('', views., name=''),
    # path('', views., name=''),

]