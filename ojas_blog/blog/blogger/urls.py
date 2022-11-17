from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('hom', views.home),
    path('contact', views.contact),
    path('login/', views.user_login),
    path('logout', views.user_logout),
    path('signup', views.user_signup),
    path('blog', views.add_blog),
    path('delete_blog/<id>', views.delete_blog),
    path('delete_blog_dash/<id>', views.delete_blog_dash),
    path('edit_blog/<id>', views.edit_blog),
    path('dashboard', views.dashboard)
]