from django.urls import path

from . import views

urlpatterns = [
    #문자열이 비어있따?? == 아무것도 없다.됨
    # 아무것도 없는 문자열이 됬을때 view에 있는 index가 실행 _ 이유는 아직 모름 개념이 없어서
    # 그냥 외워
    path('', views.index, name='index'),
]