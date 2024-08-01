from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm


def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('home')  # Redirect to a home page or dashboard
	else:
		form = UserRegistrationForm()
	return render(request, 'register.html', {'form': form})

def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(request, data=request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request, email=email, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')  # Redirect to a home page or dashboard
	else:
		form = UserLoginForm()
	return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
	logout(request)
	return redirect('login')  # Redirect to the login page
