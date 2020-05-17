from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('test/', views.TestPage.as_view(), name="test"),
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('', include("post_questions.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
