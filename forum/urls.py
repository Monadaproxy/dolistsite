from django.urls import path
from .views import forum_view, MessageDeleteView, MessageDetailView


urlpatterns = [
    path('', forum_view, name='forum'),
    path('<int:pk>', MessageDetailView.as_view(), name='forum-detail'),
    path('<int:pk>/delete', MessageDeleteView.as_view(), name='forum-delete'),
]
