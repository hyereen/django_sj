from django import forms
from .models import Order
from product.models import Product
from fcuser.models import Fcuser
from django.db import transaction

class RegisterForm(forms.Form):

    # 생성자 함수
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        
    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요.'
        },
         label='수량'
    )

    product = forms.IntegerField(
        error_messages={
            'required': '상품설명을 입력해주세요.'
        },
        label='상품설명', widget=forms.HiddenInput # 실제로 사용자에게 보여지지 않도록 
    )
    def clean(self):
        cleaned_data =super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        # 사용자 정보를 가져오기위해 session을 이용해야 함
        fcuser = self.request.session.get('user') # 이메일을 가져올 것

        if quantity and product and fcuser:
            with transaction.atomic(): # 트랜잭션으로 처리가 됨
                prod = Product.objects.get(pk=product)
                order = Order(
                    quantity = quantity,
                    product = prod,
                    fcuser = Fcuser.objects.get(email=fcuser)
                )
                order.save()
                prod.stock -= quantity
                prod.save()
        else:
            self.product = product
            self.add_error('quantity', '값이 없습니다.')
            self.add_error('product', '값이 없습니다.')
