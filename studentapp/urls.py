from django.urls import path,include
from .import views
urlpatterns = [
   path('',views.index,name='index'),
  path('addcourse',views.addcourse,name='addcourse'),
  path('add_course',views.add_course,name='add_course'),
  path('add_student',views.add_student,name='add_student'),
  path('add_studentdetails',views.add_studentdetails,name='add_studentdetails'),  
 path('show_details',views.show_details,name='show_details'), 
 path('edit/<int:pk>',views.edit,name='edit'),  
 path('edit_studentdetails/<int:pk>',views.edit_studentdetails,name='edit_studentdetails'), 
  path('delete1/<int:pk>',views.delete1,name='delete1'), 
]
 