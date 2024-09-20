# project의 urls.py 파일을 복사해 왔다. 

from django.contrib import admin
from django.urls import path
from . import views

# URL 네임스페이스 - 다른 앱과 혼동하지 않기 위해 사용
# 웬만하면 directory 명과 같게 해야 안 헷갈린다. 
# {% url 'articles:index' %}
app_name = "articles" 

# name = "index" -> naming url 패턴이라고 한다. 
# 왜 하나 ? 
# 이걸 안 하면 직접 href ="/index/" 해서 url 주소를 일일이 적어줘야겠지만 
# 이렇게 하드코딩하지 않기 위해서 name으로 참조하기 위함 
# naming url 패턴과 name이 같을 필요는 없지만, 헷갈리니까 

urlpatterns = [
  path('index/', views.index , name= "index") , 
  path('dinner/', views.dinner, name= "dinner") , 
  path('search/', views.search, name= "search") , 
  path('throw/', views.throw, name= "throw") , 
  path('catch/', views.catch, name= "catch") , 
  # <데이터타입 : 변수명> : variable routing 왜 쓸까 ? 일일이 숫자들에 따라 다 url로 path로 만들 수 없으니까 
  path('<int:num>', views.detail, name="detail"), 
]
