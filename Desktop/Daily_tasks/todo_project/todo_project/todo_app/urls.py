from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('delete/<list_id>',views.delete,name='delete'),
    path('cross/<list_id>',views.cross,name='cross'),
    path('uncross/<list_id>',views.uncross,name='uncross'),
    path('edit/<list_id>',views.edit,name='edit'),
    path('deleted/',views.deleted,name='deleted'),
    path('restore/<list_id>',views.restore,name='restore'),
    path('delete1/<list_id>',views.delete1,name='delete1'),
    path('delete1_all/',views.delete1_all,name='delete1_all'),
    path('delete_all/',views.delete_all,name='delete_all'),
    path('complete_all/',views.complete_all,name='complete_all'),
    path('restore_all',views.restore_all,name='restore_all'),
]