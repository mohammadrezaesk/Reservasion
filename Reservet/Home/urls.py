from django.urls import path , include
from Home import views
urlpatterns = [
    path('',views.Home,name="Home_select"),
    path('login/',views.Login,name="Home_login"),
    path('logout/',views.Logout,name="Home_logout"),

]
