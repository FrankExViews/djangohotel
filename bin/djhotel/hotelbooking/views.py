from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'hotelbooking/home.html')

def about(request):
    return render(request,'hotelbooking/about.html')

def faq(request):
    return render(request,'hotelbooking/faq.html')