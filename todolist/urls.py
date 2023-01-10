from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name='index'),
    path("datapost",views.datapost,name='datapost'),    
    path("delete",views.delete,name='delete'),    
    path("edit",views.edit,name='edit'),    
    path("fileupload",views.fileupload,name='fileupload'),      
    path("commentpost",views.commentpost,name='commentpost'),      
    path("detail",views.detail,name='detail'),      

]