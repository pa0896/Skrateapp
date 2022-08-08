import string
from django.shortcuts import render,redirect,HttpResponse
import random
from skrateproject.models import User,Ticket
import datetime

#variables
username = []
user = {}
temp_name = ''
auth_key = []
auth_temp = ''

#check the following
user_i = 0
id_j = 0

# Create your views here.

def index(request):
    return render(request,'index.html')

def users(request):
    return render(request,'users.html')

def us_new(request):
    return render(request,'new.html')

def existing(request):
    return redirect(index(request))

def register(request):
    temp_name = request.POST['usid']
    username.append(temp_name)
    role = request.POST['role']
    if(role == 'Admin'):
        auth_temp = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=20))
    else:
        auth_temp = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=13))
    #auth_key.append(auth_temp)
    #user = dict(zip(username, auth_key))
    #return render(request,'result.html',{'result':auth_key})
    #global user_i
    #user_i = user_i + 1
    ins = User(username=temp_name,role=role,auth_key=auth_temp)
    ins.save()
    return HttpResponse(user[0])

def tick(request):
    return render(request,'tickets.html')

def new_tick(request):
    return render(request,'newtick.html')

def new_tickreg(request):
    title = request.POST['title']
    desc = request.POST['description']
    priority = request.POST['priority']
    createdAt = datetime.now().time()
    status = 'Open'
    assignedTo = username[random.randint(0,len(username))]
    ins = Ticket(title=title,description=desc,status=status,priority=priority,assignedTo=assignedTo,createdAt=createdAt)
    ins.save()

def viewtick(request):
    #res = Ticket.objects.all()
    if(request.GET['ticketid']):
        temp = request.GET['ticketid']
        res = Ticket.objects.filter(ticketid=temp)
        return render(request,'sol.html',{'i':res})
    if(request.GET['status']):
        temp = request.GET['status']
        res = Ticket.objects.filter(status=temp)
        return render(request, 'sol.html', {'i': res})
    if(request.GET['all']):
        temp = request.GET['all']
        res = Ticket.objects.all()
        return render(request, 'sol.html', {'i': res})
    if(request.GET['priority']):
        temp = request.GET['priority']
        res = Ticket.objects.filter(priority=temp)
        return render(request,'sol.html',{'i': res})

def viewtickpage(request):
    return render(request,'viewtick.html')

def changeticket(request):
    status = request.POST['status']
    ticket_id = Ticket(request.POST['ticketid'])
    if(ticket_id.is_valid()):
        res = Ticket.objects.get(ticketid = ticket_id)
        ticket_id = Ticket(request.POST,status=status)
        ticket_id.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def delTicket(request):
    ticket_id = Ticket(request.POST['ticketid'])
    if(ticket_id.is_valid()):
        res = Ticket.objects.get(ticketid='ticket_id')
        res.delete()
        res.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

