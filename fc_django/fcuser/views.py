from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, LoginForm
from .models import Fcuser

def index(request):
    return render(request, 'index.html', {'email': request.session.get('user') })
     



class RegisterView(FormView): # 폼 뷰를 상속받아서 사용
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/' # root page로 이동 

    def form_valid(self, form): # 유효성검사가 끝났을 떄 호출되므로 여기서 저장 해줘야함
        fcuser = Fcuser(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
            level='user'
        )
        fcuser.save()
    
        return super().form_valid(form)



class LoginView(FormView):
    template_name ='login.html'
    form_class =LoginForm
    success_url='/'

    def form_valid(self, form):
        # 로그인이 정상적으로 되었을 때(유효성검사 끝) 세션에 저장
        self.request.session['user'] = form.data.get('email') # 사용자가 로그인한 이메일 정보를 세션에 저장

        return super().form_valid(form) # 기존의 form_valid 함수 호출 

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')