from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.shortcuts import render
import requests

from .forms import SignUpForm

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})
def view1(request):
    r = requests.get("http://google.com")
    print(r.status_code)

    context = {'status_code': r.status_code}
    return render(request, 'base.html', context)

def view2(request):
    # Code for the second view
    context = {}  # Update context as needed
    return render(request, 'frontpage.html', context)

def view3(request):
    # Code for the third view
    context = {}  # Update context as needed
    return render(request, 'login.html', context)

def view4(request):
    # Code for the fourth view
    context = {}  # Update context as needed
    return render(request, 'signup.html', context)
