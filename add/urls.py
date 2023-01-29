from django.urls import path
from .views import add ,delete_data,see_data,edit_data
urlpatterns = [
    path('add/',add,name='addnew'),
    path('add/de/<id>',delete_data,name='delete'),
    path('add/se/<id>',see_data,name='see'),
    path('add/ed/<id>',edit_data,name='edit'),
]