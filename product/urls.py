from django.urls import path
from . views import Index,Signup,Login
from . import views

urlpatterns = [
    path('', Index.as_view(),name='homepage'),
    path('s/',views.search),
    path('signup',Signup.as_view(), name = 'signup'),
    path('login/',Login.as_view(), name = 'login'),
    path('details/',views.get_details),
    path('logout/',views.logout),
]
