from django.urls import path
from .views import *

urlpatterns = [
    path("project/create", ProjectViewSet.as_view({"post": "create_project"}), name="createProject"),
    path("project/get", ProjectViewSet.as_view({"get": "get_projects"}), name="getProjects"),
    path("project/get/<str:project_id>", ProjectViewSet.as_view({"get": "get_project"}), name="getProject"),
    path("project/delete/<str:project_id>", ProjectViewSet.as_view({"delete": "delete_project"}), name="deleteProject"),
    path("language/get", LanguageViewSet.as_view({"get": "get_languages"}), name="getLanguage"),
    path("sentence/update", SentenceViewSet.as_view({"post": "update_sentence"}), name="updateSentence"),
    path("sentence/bulkupdate", SentenceViewSet.as_view({"post": "bulk_update_sentence"}), name="bulkUpdateSentence"),
]
