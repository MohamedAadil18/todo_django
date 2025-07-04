from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('signin', views.home_page, name='signin'),
    path('signup', views.signup_page, name='signup'),
    path('logout', views.logout_page, name='logout'),
    path('add-task', views.add_todo, name='add_todo'),
    path('delete/<int:id>', views.remove_task, name='delete'),
    path('update/<int:id>', views.update_task, name='update'),
    path('update-task/<int:id>', views.update_todo, name='update_todo'),
]
