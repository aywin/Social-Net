from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('n/logout/', views.logout_view, name='logout'),
    path('n/register/', views.register, name='register'),
    path('n/profiles/', views.profile_view, name='profile_view'),
    path('login/', views.login_view, name='login'),
    path('goto-admin/', views.goto_admin, name='goto_admin'),
    path('', views.indexx, name='indexx'),
    
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/', views.user_profile_ajax, name='full_profile'),
    path('ajax/profile/<str:username>/', views.user_profile_ajax, name='user_profile_ajax'),
    path('profile/<str:username>/', views.profile, name='profile'),
    
    path('full_profile/<str:username>/', views.full_profile, name='full_profile'),
    path('ajax/blog_content/', views.load_blog_content, name='blog_content'),
    path('profile/load/<str:username>/', views.load_profile, name='profile_load'),
    path('users/', views.users_list, name='users_list'),
    path('overview/', views.overview, name='overview'),
    path('user/edit/<str:username>/', views.edit_user, name='edit_user'),
    path('user/delete/<str:username>/', views.delete_user, name='delete_user'),
    path('chat/', views.chatbot_response, name='chatbot_response'),
    path('login/', auth_views.LoginView.as_view(template_name='network/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('stage/add/', views.add_stage, name='add_stage'),
    path('stage/update/<int:stage_id>/', views.update_stage, name='update_stage'),
    path('stage/delete/<int:stage_id>/', views.delete_stage, name='delete_stage'),
    path('poste/add/', views.add_poste, name='add_poste'),
    path('poste/update/<int:poste_id>/', views.update_poste, name='update_poste'),
    path('poste/delete/<int:poste_id>/', views.delete_poste, name='delete_poste'),
    path('mobilite/add/', views.add_mobilite, name='add_mobilite'),
    path('mobilite/update/<int:mobilite_id>/', views.update_mobilite, name='update_mobilite'),
    path('mobilite/delete/<int:mobilite_id>/', views.delete_mobilite, name='delete_mobilite'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('domaines-utilisateurs/', views.domaines_utilisateurs, name='domaines_utilisateurs'),
   
    path('search/', views.search, name='search'),
    path('search_profiles/', views.search_profiles, name='search_profiles'),
    path('mentoring/', views.mentoring, name='mentoring'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
