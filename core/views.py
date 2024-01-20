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
def common_view(request, template_name):
    # Make a GET request to the local development URL
    url = 'https://django-chat-app-btvj.onrender.com'  # Use the correct URL for your local development server
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        content = response.text
    else:
        content = f'Request failed with status code {response.status_code}'

    return render(request, template_name, {'content': content})

