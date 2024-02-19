from django.urls import path
from . import views
from .views import MyLoginView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="index"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile_with_forms, name="profile"),
    path("update/", views.profile, name="update"),
    path("imageupload/", views.imageupload, name="upload"),
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("image/<int:image_id>/delete/", views.delete_image_view, name="delete_image"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
