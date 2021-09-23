from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import Topic,Webpage,AccessRecord,User
from . import forms

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'acces_records': webpages_list}
    if date_dict['acces_records']:
        return render(request, 'firstApp/index.html', context=date_dict)
    return HttpResponse('helloworld')

def user(request):
    users_list = User.objects.all()
    user_dict = {'users': users_list}
    return render(request, 'firstApp/user.html', context=user_dict)

def help(request):
    return render(request, 'firstApp/help.html')

def signUp (request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            print("validation Succes")
        else:
            print("not valid")
    return render (request, 'firstApp/form_page.html', {'form':form})