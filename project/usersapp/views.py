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
            context = {'error': '아이디 또는 비밀번호가 일치하지 않습니다.'}
            return render(request,'login.html',context)
        else:
            user_name=user.username
            print(user_name)
            if check_password(password, user.password):
                request.session['user'] = user_name
                return redirect('/mainapp/home/')
            else:
                context = {'error': '아이디 또는 비밀번호가 일치하지 않습니다.'}
                return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)



def register(request):
    if request.method =='GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        useremail = request.POST.get('email', None)
        username = request.POST.get('name', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        res_data={}
        if password != re_password:
            res_data['error']='비밀번호가 다릅니다.'
            return render(request, 'register.html', res_data)
        else:
            users = Users(
                useremail=useremail,
                username=username,
                password=make_password(password)
            )
            users.save()
            return render(request,'login.html')


def forgot(request):
    if request.method == "POST":
        useremail=request.POST.get("email")
        try:
            user = Users.objects.get(useremail=useremail)
        except Users.DoesNotExist:
            context = {'error': '없는 이메일 주소입니다.'}
            return render(request,'forgot.html',context)
        else:
            request.session['email']=useremail
            return redirect('/usersapp/pwreset/?email='+useremail)
    else:
        return render(request, 'forgot.html')

def pwreset(request):
    if request.method == "POST":
        password=request.POST.get("password")
        re_password=request.POST.get("re-password")
        if password != re_password:
            render(request,'pwreset.html',context={"error":"비밀번호가 일치하지 않습니다."})
        else:
            e=request.GET.get('email',"NotFound")
            if e == "NotFound": return render(request,'forgot.html',{'error':"변경할 이메일을 입력해 주세요."})
            user=Users.objects.get(useremail=e)
            user.password=make_password(password)
            user.save()
            return redirect("usersapp:login")
    else:
        e=request.GET.get('email',"NotFound")
        if e == "NotFound": return render(request, 'forgot.html', {'error': "변경할 이메일을 입력해 주세요."})
        return render(request, 'pwreset.html',{'email':request.GET['email']})
