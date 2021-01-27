from django.contrib import admin
from .models import Fcuser

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email',) # 콤마를 꼭 넣어줘야 함, 튜플로 인식시키기 위해 


admin.site.register(Fcuser, FcuserAdmin)
