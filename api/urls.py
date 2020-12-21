from .views import signup_view,signin_view,Change_view
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'signup/', views.signup_view, name='signup'),
    url(r'signin/', views.signin_view, name='signin'),
    url(r'forgot/', views.forgot_view, name='forgot'),
    url(r'forgot1/', views.forgot, name='forgot1'),
    url(r'Change/', views.Change_view, name='Change'),
    
]