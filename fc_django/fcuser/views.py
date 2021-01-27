from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm

def index(request):
    return render(request, 'index.html')



class RegisterView(FormView): # 폼 뷰를 상속받아서 사용
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/' # root page로 이동 

