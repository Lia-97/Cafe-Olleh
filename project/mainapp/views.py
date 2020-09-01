from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from mainapp.models import Product, Price_Bybrand, Product_Bybrand
from mainapp.models import Brand,Location
from mainapp.models import Post,recommend
from usersapp.models import Users

enToko={ "Americano":"아메리카노",
         "Coffee Latte":"카페라떼",
         "Cappuccino":"카푸치노",
         "Vanilla Latte":"바닐라라떼",
         "Cafe Mocha":"카페모카",
         "Caramel Macchiato":"카라멜마끼아또",
         "Cold Brew":"콜드브루",
         "Green Tea Latte":"그린티라떼",
         "Chocolate Latte":"초콜릿라떼",
         "Starbucks":"스타벅스",
         "Twosome":"투썸플레이스",
         "TomandToms":"탐앤탐스",
         "Ediya":"이디야",
         "Mega":"메가커피",
         "Hollys":"할리스",
         "Coffeebean":"커피빈",
         "Coffeebay":"커피베이",
         "Angelinus":"엔제리너스",
         "Pascucci":"파스쿠찌"}

def home(request):
    context={}
    comments={"Americano":"아메리카노의 쓴맛을 즐기는 것, 어른이 됐다는 것.",
             "Coffee Latte":"라떼는 말야, 라떼를 마셨어.",
             "Cappuccino":"부드러운 거품, 고소한 시나몬, 인생은 카푸치노처럼.",
             "Vanilla Latte":"당 떨어지는 오후3시, 바닐라라떼.",
             "Cafe Mocha":"일상에 초콜릿 한 스푼, 카페모카.",
             "Caramel Macchiato":"마끼아또, 마셔봐또?",
             "Cold Brew":"시간을 마시다, 콜드브루.",
             "Green Tea Latte":"그린티라떼가 녹차라떼고, 녹차라떼가 그린티라떼야.",
             "Chocolate Latte":"어리다고 놀리지 말아요. 달달한 초콜릿라떼."}
    context["comments"]=comments
    if 'user' in request.session:
        context['user_name']=request.session.get('user')
        return render(request,'home.html',context)
    else:
        return render(request,'home.html',context)

def logout(request):
    if 'user' in request.session:
        del request.session['email']
        del request.session['user']
        return redirect(request.GET['next'])

def best9(request):
    context={}
    context["product"]=request.GET['product']
    ## global enToko
    ko_name=enToko[request.GET['product']]
    product=Product.objects.filter(products=ko_name)
    price=Price_Bybrand.objects.get(pk=product[0].id)
    name=Product_Bybrand.objects.get(pk=product[0].id)
    coffee_list={}
    for i,(brand,coffee,cost) in enumerate(zip(price.__dict__,name.__dict__.values(),price.__dict__.values())):
        if i>=2 and coffee != None:
            coffee_list[brand]=str(coffee)+"/"+str(cost)+"원"
    context["coffee_list"]=coffee_list

    if 'user' in request.session:
        context['user_name']=request.session.get('user')

    return render(request,'bestmenu.html',context)

def cafemap(request):
    context={}
    # 영문 이름 받기
    context['store']=request.GET['store']
    store=enToko[request.GET['store']]
    brand=Brand.objects.filter(brand=store)
    location=Location.objects.filter(brand_id=brand[0].id)
    context['Location']=location

    if 'user' in request.session:
        context['user_name']=request.session.get('user')
    return render(request,'cafemap.html',context)

def brandmenu(request):
    context={}
    menu_list=["Starbucks","TwosomePlace","TomnToms","Ediya","MegaCoffee","Hollys",
               "CoffeeBean","CoffeeBay","Angelinus","Pascucci"]
    context['menu_list']=menu_list

    if 'user' in request.session:
        context['user_name']=request.session.get('user')
    return render(request,'brandmenu.html',context)

def post(request):
    context={}

    if 'user' in request.session:
        context['user_name']=request.session.get('user')

    context["error"]=request.GET.get('err',None)
    if request.method == "POST":
        title=request.POST['title']
        content=request.POST['content']
        if 'user' in request.session:
            writer=request.session['email']
            post=Post(writer_id=writer,title=title,content=content)
            post.save()
            return redirect('post')
        else:
            return redirect('/mainapp/post/?err='+"먼저 로그인을 해주세요.")
    else:
        post=Post.objects.all()
        context["Post"]=post
        return render(request,'post.html',context)

def write(request):
    context={}
    if 'user' in request.session:
        context['user_name']=request.session.get('user')
        return render(request,'write.html',context)
    else:
        return redirect("/mainapp/post/?err="+"먼저 로그인을 해주세요.")

def view(request):
    context={}
    id = request.GET['view']
    context["error"]=request.GET.get("err",None)
    if 'user' in request.session:
        context['user_name']=request.session.get('user')
        context['user_email']=request.session.get('email')
        try:
            like=recommend.objects.filter(useremail_id=request.session.get('email'))
        except recommend.DoesNotExist:
            pass
        else:
            print(list(map(lambda x:x.post_id,like)),id)
            if int(id) in list(map(lambda x:x.post_id,like)):
                print("참참참참참참")
                context['islike']=True
            else:
                print("거짓거짓")
                context['islike']=False

    view=Post.objects.get(pk=id)
    context['view']=view
    return render(request,'view.html',context)

def notlike(request):
    post_id=request.GET['post_id']
    user_id=request.GET['user_id']

    if 'user' not in request.session:
        return redirect("/mainapp/view/?view="+str(post_id)+"&err=먼저 로그인을 해주세요.")


    view = Post.objects.get(pk=post_id)
    view.up_like
    recom=recommend(post_id=post_id,useremail_id=user_id)
    recom.save()
    return redirect('/mainapp/view/?view='+str(post_id))

def islike(request):
    post_id = request.GET['post_id']
    user_id = request.GET['user_id']
    view=Post.objects.get(pk=post_id)
    view.down_like
    recom=recommend.objects.filter(post_id=post_id,useremail_id=user_id)
    recom.delete()
    return redirect('/mainapp/view/?view='+str(post_id))