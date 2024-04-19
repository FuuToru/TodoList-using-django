from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'home'),
    path('todo1/', views.todo1, name='todo1'),
    path('del1/<str:item_id>', views.remove1, name="del1"),
    path('cv/', views.cv, name = 'cv'), 
    path('save/', views.save_resume, name = 'save'),
    path('fake_data/', views.fake_data, name='fake_data'),


]

