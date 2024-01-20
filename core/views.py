from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.shortcuts import render
import requests

from .forms import SignUpForm

def frontpage(requests):
    return render(requests, 'core/frontpage.html')

def signup(requests):
    if requests.method == 'POST':
        form = SignUpForm(requests.POST)

        if form.is_valid():
            user = form.save()

            login(requests, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(requests, 'core/signup.html', {'form': form})
def view1(requests):
    r = requests.get("http://google.com")
    print(r.status_code)

    context = {'status_code': r.status_code}
    return render(requests, 'base.html', context)

def view2(requests):
    # Code for the second view
    context = {}  # Update context as needed
    return render(requests, 'frontpage.html', context)

def view3(requests):
    # Code for the third view
    context = {}  # Update context as needed
    return render(requests, 'login.html', context)

def view4(requests):
    # Code for the fourth view
    context = {}  # Update context as needed
    return render(requests, 'signup.html', context)
def common_view(requests, template_name):
    # Make a GET request to the local development URL
    url = 'https://django-chat-app-btvj.onrender.com'  # Use the correct URL for your local development server
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        content = response.text
    else:
        content = f'Request failed with status code {response.status_code}'

    return render(requests, template_name, {'content': content})

