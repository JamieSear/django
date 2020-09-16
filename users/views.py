from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .forms import UserSignupForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def signup(req):
    if req.method == 'POST':
        form = UserSignupForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Welcome, {username}!')
            return redirect('tennis-index')
    else:
        form = UserSignupForm()
    data = {'form': form}
    return render(req, 'users/signup.html', data)

# @login_required
# def profile(req):
#     return HttpResponse(f'<h1>{user.username}\'s profile</h1>')