from django.urls import path
from .views import RagAskView
from django.views.generic import TemplateView

urlpatterns = [
    path("ask/", RagAskView.as_view(), name="rag-ask"),
    path("", TemplateView.as_view(template_name="rag_chat.html"), name="rag-chat"),
]
