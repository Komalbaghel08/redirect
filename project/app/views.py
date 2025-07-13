from django.shortcuts import render,redirect
from django.urls import reverse
from  urllib.parse import urlencode

# Create your views here.
# def home(request):
#     # create external url....
#     return redirect("https://www.facebook.com/your")

# def home(request):
#     return redirect('redirect1')
 
# def redirect1(request):
#     return render(request,'redirect1.html')

# def home(request):
#     url =reverse('redirect2',kwargs = {'name':'komal','age':20})
#     return redirect(url)



# def redirect2(request,name,age):
#     return render(request,'redirect2.html')

def home(request):
    url = reverse('redirect3')
    data = urlencode({'name':'komal','age':20})
    return redirect (f'{url}?{data}')

def redirect3(request):
    print("hello")
    n = request.GET.get('name')
    a = request.GET['age']
    print(n,a,sep=',')
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.method)