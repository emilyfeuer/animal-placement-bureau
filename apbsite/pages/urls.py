from django.urls import path

from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
# ]

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /pages/5/
    path("<int:option_id>/", views.detail, name="detail"),
]