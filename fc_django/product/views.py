from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm

class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'

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