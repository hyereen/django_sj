from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator # decorators import 주의! 
from fcuser.decorators import admin_required # decorators import 주의! 
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm

class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'

@method_decorator(admin_required, name='dispatch') # 사실 로그인만이 아니라 관리자가 로그인했을 때 상품 등록이 가능해야 함
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    # all()은 모든 제품 중에서 하나씩 꺼내서 디테일을 보여줌
    # 상세보기 페이지에서 조건에 맞는 상품만 보여주고 싶으면 필터로 조건 지정 가능
    # 디테일 뷰로 들어왔을 때 조건에 안맞으면 디테일 뷰를 볼 수 없도록
    context_object_name = 'product' # 실제 템플릿에서 사용할 변수명 지정 가능 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # 먼저 디테일뷰가 전달해주는 데이터를 이용해서 만들고

        context['form'] = OrderForm(self.request) # 기존에 생성된 데이터에 주문하기라는 새로운 폼을 추가함
        return context