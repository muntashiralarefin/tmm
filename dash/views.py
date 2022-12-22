from django.shortcuts import render

# Create your views here.
def home(request, district="Cox's Bazar"):
    return render(request, 'dash\home.html', {})
