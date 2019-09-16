from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'profile',)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else :
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

def login(request):
    return redirect('login')

def popup(request):
    return render(request, 'registration/popup.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('insta.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('popup/', popup, name='popup'),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)