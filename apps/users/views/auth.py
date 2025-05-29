from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.users.forms.login_form import CustomLoginForm
from apps.users.services.user_service import get_user_role

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            role = get_user_role(user)
            if role == 'Coordinador':
                return redirect('dashboard:coordinator_home')
            elif role == 'Docente':
                return redirect('dashboard:teacher_home')
            return redirect('/')
        else:
            messages.error(request, 'Credenciales inválidas.')
    else:
        form = CustomLoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente.')
    return redirect('users:login')
