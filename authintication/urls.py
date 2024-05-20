from django.urls import path, include
import authintication.views as views
urlpatterns = [
     path('login/', views.login_view, name='login'),
     path('logout/', views.logout_view, name='logout'),
     path('register', views.register_view, name='register'),
     path('profile/', views.profile_viewu, name='profile'),
     path('profile/edit/', views.edit_profile, name='edit_profile'),
]