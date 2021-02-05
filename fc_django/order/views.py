from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator # 장고에서 데코레이터를 넣을 수 있게끔 제공해주는 함수
from fcuser.decorators import login_required
from django.db import transaction
from .forms import RegisterForm
from .models import Order
from product.models import Product
from fcuser.models import Fcuser

# Create your views here.
@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    # template_name은 필요가 없다 왜냐하면 폼뷰를 화면을 보여주는 용도로 사용하는게 아니기때문에! 화면은 product_detail에 있어서
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        with transaction.atomic(): # 트랜잭션으로 처리가 됨
            prod = Product.objects.get(pk=form.data.get('product'))
            order = Order(
                quantity = form.data.get('quantity'),
                product = prod,
                fcuser = Fcuser.objects.get(email=self.request.session.get('user'))
            )
            order.save()
            prod.stock -= int(form.data.get('quantity'))
            prod.save()
        
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))

    # 클래스 기반 뷰 안에 기본적으로 이 함수가 있음
    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request # request 인자값 추가
        })
        return kw
    #폼을 생성할 떄 어떤 인자값을 전달해서 만들건지 결정하는 함수 


@method_decorator(login_required, name='dispatch') # 실제로 dispatch함수가 실행되는 것 
class OrderList(ListView):
    model = Order
    template_name= 'order.html'
    context_object_name = 'order_list'
    
    # queryset 직접 오버라이딩 
    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(fcuser__email=self.request.session.get('user'))
        return queryset