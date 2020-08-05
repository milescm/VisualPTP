from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('showdata/', views.showdata, name='showdata'),
    path('readcsv/', views.readcsv, name='readcsv'),
    path('deletedata/', views.deletedata, name='deletedata'),
    path('showgraph/', views.showgraph, name='showgraph'),
    path('showstock/', views.showstock, name='showstock'),
   

]