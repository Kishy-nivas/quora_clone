from django.conf.urls import url,include 
from .import views

urlpatterns =[
	url(r'^$',views.index,name='index'),
	url(r'^signup/$',views.signup,name='signup'),
	url(r'^profile/(?P<pk>\d+)/$',views.profiledetail.as_view(),name = 'profile-detail'),
	url(r'^ask/$',views.ask, name='ask'),
	url(r'^question/$',views.question_list.as_view(),name='question-list'),
	 
]