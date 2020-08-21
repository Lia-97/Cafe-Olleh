from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect

# Create your views here.
from usersapp.models import Users


def login(request):
    context = None
    if request.method == 'POST':
        useremail = request.POST.get('email', None)
        password = request.POST.get('password', None)
        try:
            user = Users.objects.get(useremail=useremail)
        except Users.DoesNotExist:
            context = {'error': '계정을 확인하세요'}
        else:
            if check_password(password, user.password):
                request.session['user'] = useremail
                return redirect('/mainapp/home/')
            else:
                context = {'error': '패스워드를 확인하세요'}
    else:
        if 'user' in request.session:
            context = {'msg': '이미 %s 로그인 하셨습니다.' % request.session['user']}
    return render(request, 'login.html', context)

def register(request):
    if request.method =='GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        useremail = request.POST.get('email', None)
        username = request.POST.get('name', None)
        password = request.POST.get('password', None)
        users = Users(
            useremail=useremail,
            username=username,
            password=make_password(password)
        )
        users.save()
        return render(request, 'register.html')

def forgot(request):
    return render(request, 'forgot.html')

def pwreset(request):
    return render(request, 'pwreset.html')
