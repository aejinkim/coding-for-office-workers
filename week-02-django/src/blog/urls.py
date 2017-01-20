from django.conf.urls import url

from . import views #from 뒤에 .(점)을 찍으면 같은 폴더로 찾아간다는 의미이다. 

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
