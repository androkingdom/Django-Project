from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "apps/index.html")

def about(request):
    return render(request, "apps/about.html")

def contact(request):
    return render(request, "apps/contact.html")