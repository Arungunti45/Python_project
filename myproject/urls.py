from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

def redirect_to_signup(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    return redirect('home')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_signup),  # Handles root URL '/'
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
