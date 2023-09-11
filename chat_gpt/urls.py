from django.urls import path
from chat_gpt.views import ChatBotView

urlpatterns = [
    path('', ChatBotView.as_view(), name='chatbot'),
]