from django.urls import path
from .views import TaskList , TaskDetail,TaskCreate,TaskUpdate ,DeleteView,UserLogin,LogoutView,UserRegister

urlpatterns = [
    path('', TaskList.as_view() ,name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view() ,name='task'),
    path('task-create/', TaskCreate.as_view() ,name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view() ,name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view() ,name='task-delete'),
    path('login/',UserLogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',UserRegister.as_view(),name='register'),
] 