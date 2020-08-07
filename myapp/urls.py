from django.urls import path
from . import views
from . import tests
app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('showdata/', views.showdata, name='showdata'),
    path('deletedata/', views.deletedata, name='deletedata'),
    path('showgraph/', views.showgraph, name='showgraph'),
    path('showstock/', views.showstock, name='showstock'),
    path('userform/', views.userform, name='userform'),
    path('filecheck/', views.filecheck, name='filecheck'),
    

    
   

]