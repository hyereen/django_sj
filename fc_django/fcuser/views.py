from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm

def index(request):
    return render(request, 'index.html', {'email': request.session.get('user') })
     



class RegisterView(FormView): # 폼 뷰를 상속받아서 사용
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/' # root page로 이동 


class LoginView(FormView):
    template_name ='login.html'
    form_class =LoginForm
    success_url='/'

    def form_valid(self, form):
        # 로그인이 정상적으로 되었을 때(유효성검사 끝) 세션에 저장
        self.request.session['user'] = form.email # 사용자가 로그인한 이메일 정보를 세션에 저장

        return super().form_valid(form) # 기존의 form_valid 함수 호출 
