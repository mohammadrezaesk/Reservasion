from django.urls import path , include
from Dashboard import views
urlpatterns = [
    path('',views.Home,name="dashboard_home"),
    path('advices/',views.advices,name="dashboard_show_total"),
    path('newadvice/',views.newadvices,name="dashboard_show_new"),
    path('newadvice/showtime/',views.showtime,name="dashboard_show_time"),
    path('times/',views.times,name="dashboard_show_times"),
    path('timeline/',views.timeline,name="dashboard_show_timeline"),
]
