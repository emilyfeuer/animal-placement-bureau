from django.urls import path

from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
# ]

urlpatterns = [
    path("", views.index, name="index"),
    path("about.html", views.about, name="about"),
    path("gallery.html", views.gallery, name="gallery"),
    # ex: /pages/5/
    path("<int:option_id>/", views.detail, name="detail"),
]