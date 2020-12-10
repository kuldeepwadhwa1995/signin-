from .views import signup_view,signin_view
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'signup/', views.signup_view, name='signup'),
    url(r'signin/', views. signin_view, name='signin'),
]