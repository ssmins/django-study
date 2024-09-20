from django.shortcuts import render

# Create your views here.
def index(request): 
  # context는 딕셔너리 구조 
  # templates 에서 {{ name }} 이라고 이중 괄호를 사용하면, 
  # context key의 value 값을 사용할 수 있다. 
  context = {
    'name' : 'Minsu', 
    'num' : 1
  }

  # 항상 render 함수의 3번째 항목에는 매개변수(context)가 들어간다. 
  # render 함수는 항상 
  return render(request, 'articles/index.html', context) 

import random 
def dinner(request): 
  foods = ['족발', '보쌈', '치킨', '피자']
  picked = random.choice(foods)
  context = {
    # 중요한 건 key 아니고 value, key 값은 바뀌어도 상관 X, 헷갈리니까 같게 설정한거 
    'foods' : foods, 
    'picked' : picked
  }
  return render(request, 'articles/dinner.html', context)

# form 넣을 함수. context 없으니까 필요 X 
def search(request): 
  return render(request, 'articles/search.html')

def throw(request): 
  return render(request, 'articles/throw.html')

def catch(request): 
  # message = request.GET 
  text = request.GET.get('throw')
  # 와 같이 그냥 파이썬 메소드 사용한 거 
  print(text) # 확인차 추가한 부분 
  # throw로부터 받은 걸 보여줄 context가 필요한 catch 
  context = {
    'message' : text
  }
  return render(request, 'articles/catch.html', context)

def detail(request, num): 

  context = { 
    'num' : num
  }
  return render(request, 'articles/detail.html', context)


