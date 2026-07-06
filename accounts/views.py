from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Akkaunt muvaffaqiyatli yaratildi! {username}, tizimga kirish mumkin.")
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

