from django.contrib import admin
from django.urls import path

from skrateproject import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index),
    path('users',views.users,name='users'),
    path('users/new',views.us_new,name='new'),
    path('existing',views.existing,name='existing'),
    path('users/register',views.register),
    path('tickets',views.tick,name='tickets'),
    path('tickets/newtick',views.new_tick,name='newtick'),
    path('tickets/viewtick',views.viewtickpage,name='viewtick'),
    path('tickets/viewtick/',views.viewtick),
    path('tickets/delete',views.delTicket,name='delete'),
    path('tickets/changetick',views.changeticket,name='changetick')
]