from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [

    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('hi/',views.hi,name='hi'),
    path('new_blog/',views.new_blog,name='new_blog'),
    path('blogdetail/<int:pk>',views.BlogDetail.as_view(),name='blogdetail'),
    path('blogupdate/<int:pk>',views.BlogUpdate.as_view(),name='blogupdate'),
    path('blogdelete/<int:pk>',views.BlogDelete.as_view(),name='blogdelete'),


    path('logout/', LogoutView.as_view(next_page= 'login'), name='logout'),


]