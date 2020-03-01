from django.urls import path , include
from Dashboard import views
urlpatterns = [
    path('',views.Home,name="dashboard_home"),
    path('advices/',views.advices,name="dashboard_show_total"),
]
