from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from equipamentos import views as equipamentos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    # dashboard como página inicial
    path("", equipamentos_views.dashboard, name="home"),
    path('', include('equipamentos.urls')),
]
