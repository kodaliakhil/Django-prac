from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello,world')
def say_hello(request):
    return HttpResponse('Hello, This is Akhil')
def menuitems(request,dish):
    return HttpResponse(f'Hello, This is {dish}')
def get_HTML_with_data(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    # address = request.META('REMOTE_ADDR')
    # user_agent = request.META('HTTP_USER_AGENT')
    path_info= request.path_info
    msg = f"""<br>
    <br> path = {path}
    <br> scheme = {scheme}
    <br> method = {method}
    
   
    <br> path_info= {path_info}
    <br>
    
    """
    respone = HttpResponse(msg,content_type="text/html",charset='utf-8')
    return respone
