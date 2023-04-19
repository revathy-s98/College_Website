from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemberCreationForm
from .models import Member, Course


def demo(request):
    return render(request,"index.html")







    #     if password == cpassword:
    #         if User.objects.filter(username=username).exists():
    #             messages.info(request,"Username Taken")
    #             return redirect('register')
    #         elif User.objects.filter(password=password).exists():
    #             messages.info(request,"password Taken")
    #             return redirect('register')
    #         else:
    #             user = User.objects.create_user(username=username,password=password)
    #             user.save();
    #             return redirect('login')
    #     else:
    #         messages.info(request,"password not matching")
    #         return redirect('register')
    #     return redirect('/')
    # return render(request,"register.html")
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('form')
#         else:
#             messages.info(request,"invalid credentials")
#             return redirect('login')
#     return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('create_view')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def create_view(request):
    # form = MemberCreationForm()
    if request.method == 'POST':
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            return redirect('message')
    else:
        form = MemberCreationForm()
    return render(request, 'home.html', {'form':form})


def update_view(request, pk):
    member = get_object_or_404(Member, pk=pk)
    form = MemberCreationForm(instance=member)
    if request.method == 'POST':
        form = MemberCreationForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('change', pk=pk)
    return render(request, 'home.html', {'form': form})


# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})
def message(request):
    return render(request,"message.html")

