from django.shortcuts import redirect 
from .models import Fcuser

def login_required(function):
    def wrap(request, *args, **kwargs): #wrapping한 함수와 기존 함수의 인자값을 맞춰줘야 함
        user = request.session.get('user')
        if user is None or not user: # 유저가 none이거나 비어있거나 -> 빈문자일떄도 예외처리 가능
            return redirect('/login')
        return function(request, *args, **kwargs) # 원래 함수에 그대로 전달해줘야 정상적으로 동작 
    
    return wrap
   
# @method_decorator(login_required, name='dispatch')여기에 이렇게 또 데코레이터 할 수 있는데 이렇게 하지 않고
# wrap 안에 if로 넣어줬음
def admin_required(function):
    def wrap(request, *args, **kwargs): #wrapping한 함수와 기존 함수의 인자값을 맞춰줘야 함
        user = request.session.get('user')
        if user is None or not user: # 유저가 none이거나 비어있거나 -> 빈문자일떄도 예외처리 가능
            return redirect('/login')

        user = Fcuser.objects.get(email=user)
        if user.level != 'admin':
            return redirect('/')
        return function(request, *args, **kwargs) # 원래 함수에 그대로 전달해줘야 정상적으로 동작 
    
    return wrap