from django.db import models

# Create your models here.
class Board(models.Model): 

  title = models.CharField(max_length= 10)
  # 글자 제한이 20자인 제목 필드
  # 필드 ? - 열 
  # title 은 왜 TextField 를 쓰지 않고, CharField를 쓸까 ? 
  content = models.TextField() 
  # 텍스트 필드, 마땅한 제약 조건이 없는 

  # 처음 생성 시간 필드 : 객체가 처음 생성된 시간 
  created_at = models.DateTimeField(auto_now_add=True) 
  # 수정 시간 필드 : 객체가 저장될 때마다의 시간 
  updated_at = models.DateTimeField(auto_now=True)

  xx_at = models.DateTimeField(null= True, blank=True)

  # 클래스 안의 함수 정의 -> 메서드 
  def __str__(self):
    return self.title # admin-board 화면에 title 표시 