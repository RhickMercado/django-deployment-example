from django.shortcuts import render
#from django.http import HttpResponse

#from appTwo.models import users
from appTwo.forms import newUserForm
# Create your views here.

def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    form = newUserForm()

    if request.method =="POST":
        form = newUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'appTwo/users.html', {'form':form})
