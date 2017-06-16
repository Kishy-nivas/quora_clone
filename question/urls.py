from django.conf.urls import url,include 
from .import views

urlpatterns =[
	url(r'^home/$',views.index,name='index'),
	url(r'^signup/$',views.signup,name='signup'),
	url(r'^profile/(?P<pk>\d+)/$',views.profiledetail.as_view(),name = 'profile-detail'),
	url(r'^ask/$',views.ask, name='ask'),
	url(r'^$',views.question_list.as_view(),name='question-list'),
	url(r'^questiondetail/(?P<pk>\d+)/$',views.question_detail ,name ='question-detail'),
	url(r'answer/$',views.answer ,name ='answer'),	 
]