from django.db import models

class Order(models.Model):
    fcuser = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='사용자')
    # fcuser 앱 안에 있는 Fcuser 모델을 이용하겠다
    # foreignKey 쓸 때는 on_delete 속성 꼭 써줘야 함, 사용자가 삭제 됐을 때 order을 어떻게 관리할지
    # CASCADE -> 유저가 삭제되면 유저도 삭제하겠다
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return str(self.fcuser) + ' ' + str(self.product)
    class Meta:
        db_table = 'fastcampus_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'