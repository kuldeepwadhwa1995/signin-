from .views import signup_view
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'signup/', views.signup_view, name='signup'),
]