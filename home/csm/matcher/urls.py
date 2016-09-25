from django.conf.urls import url

from . import views

urlpatterns = [
	#eg: /matcher/
    url(r'^$', views.index, name='index'),
    #eg /matcher/choose
    url(r'^choose/$', views.choose, name='choose')
]