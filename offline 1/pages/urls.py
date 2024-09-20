# articles의 urls.py 파일을 복사해 왔다. 

from django.contrib import admin
from django.urls import path
from . import views

# URL 네임스페이스 - 다른 앱과 혼동하지 않기 위해 사용
app_name = "pages" 

urlpatterns = [
  path('index/', views.index , name= "index") , 
]
