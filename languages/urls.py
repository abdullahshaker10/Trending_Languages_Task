from django.urls import path
from . import views

app_name = "languages"

urlpatterns = [
    path(
        "<slug:languages_number>/",
        views.TrandingLanguageAPIView.as_view(),
        name="get_trending_languages",
    ),
]
