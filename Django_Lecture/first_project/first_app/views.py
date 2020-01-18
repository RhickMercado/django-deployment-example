from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, User
# Create your views here.

def index(request):
    # return HttpResponse("Hello World!")
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    #my_dict = {'insert_me': "Now I am coming from first_app"}
    #return render(request, 'first_app/index.html', context=my_dict)
    return render(request, 'first_app/index.html', context=date_dict)

def users(request):
    # return HttpResponse("Hello World!")
    user_list = User.objects.order_by('firstName')
    user_dict = {'user_records':user_list}
    #my_dict = {'insert_me': "Now I am coming from first_app"}
    #return render(request, 'first_app/index.html', context=my_dict)
    return render(request, 'first_app/user.html', context=user_dict)
