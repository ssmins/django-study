from django.contrib import admin

# Register your models here.

from .models import Board
# 현재 디렉토리의 models.py 에서 Board 모델을 가져오겠다. 

admin.site.register(Board)
# 앱 이름은 articles인데?   
# 상관 없다. Board 모델을 Django 관리자 사이트(admin)에 등록 
