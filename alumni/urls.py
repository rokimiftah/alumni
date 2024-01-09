from django.urls import path

from alumni.views import add_alumni, delete_alumni, edit_alumni, index, view_alumni

urlpatterns = [
    path("", index, name="index"),
    path("<int:id>/", view_alumni, name="view_alumni"),
    path("add/", add_alumni, name="add_alumni"),
    path("edit/<int:id>/", edit_alumni, name="edit_alumni"),
    path("delete/<int:id>/", delete_alumni, name="delete_alumni"),
]
