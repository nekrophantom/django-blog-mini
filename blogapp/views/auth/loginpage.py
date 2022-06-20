from django.shortcuts import render, redirect
from ...models.user.user import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def loginPage(request):
    title = 'Login'

    if request.user.is_authenticated:
            return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email = email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email does not exist')


    context = {
        'title': title,
    }

    return render(request, 'auth/login.html', context)

