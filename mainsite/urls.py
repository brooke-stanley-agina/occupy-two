from django.urls import path
from . import views

app_name = 'mainsite'

urlpatterns = [
    path('',views.index,name='index'),
    path('/about_page/',views.about_page,name='about_page'),
    path('/activities/',views.activities,name='activities')
]
