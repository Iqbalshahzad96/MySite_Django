from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello', 'number':100}
    return render(request,'learn_templates/index.html', context_dict)

def base(request):
    return render(request,'learn_templates/base.html')

def other(request):
    return render(request,'learn_templates/other.html')

def relative(request):
    return render(request,'learn_templates/relative_url_templates.html')