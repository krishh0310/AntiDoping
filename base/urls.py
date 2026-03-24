from django.urls import path
from . import views

urlpatterns = [
    path('',                                          views.home,          name='home'),
    path('modules/',                                  views.modules_list,  name='modules'),
    path('module/<int:module_id>/',                   views.module_detail, name='module_detail'),
    path('module/<int:module_id>/part/<int:part_order>/', views.module_part, name='module_part'),
    path('module/<int:module_id>/quiz/',              views.module_quiz,   name='module_quiz'),
    path('quiz/',                                     views.final_quiz,    name='quiz'),
    path('chatbot/',                                  views.chatbot,       name='chatbot'),
    path('updates/',                                  views.updates,       name='updates'),
    path('certificate/<int:result_id>/',              views.certificate,   name='certificate'),
    path('api/chat/',                                 views.chat_api,      name='chat_api'),
]