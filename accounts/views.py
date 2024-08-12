from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(email=email).exists():
            return render(request, 'accounts/register.html', {'error': 'Такой почтовый ящик уже есть!'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'Пользователь с таким никнеймом уже есть'})
        
        user = User(email=email, username=username)
        user.set_password(password)  # Хешируем пароль
        user.save()
        return redirect('login')
    
    return render(request, 'accounts/register.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'accounts/login.html', {'error': 'Неверный email или пароль'})
    
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

            
        
    
