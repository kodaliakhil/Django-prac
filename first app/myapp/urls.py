from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('sayhello',views.say_hello),
    path('get_HTML_with_data',views.get_HTML_with_data),
    path('dishes/<str:dish>',views.menuitems)
]