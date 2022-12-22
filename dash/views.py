from django.shortcuts import render

# Create your views here.
def survey(request):
    return render(request, 'dash\survey.html', {})

def home(request, district="Cox's Bazar"):
    return render(request, 'dash\home.html', {})

