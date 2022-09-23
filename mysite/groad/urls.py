from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'groad'

urlpatterns = [
    path('user/', views.Groad_user_List.as_view()),               # user의 목록
    path('user/login/', views.Groad_user_login.as_view()),          # user의 login
    path('user/<int:pk>/', views.Groad_user_Detail.as_view()),    # user의 Detail 목록
    path('pedometer/', views.Groad_pedometer_List.as_view()),        # pedometer 목록
    path('pedometer/<int:fk>/', views.Groad_pedometer_Detail.as_view()),   # pedometer의 Detail 목록
    path('review/', views.Groad_review_List.as_view()),            # review의 목록
    path('review/<int:fk>/', views.Groad_review_Detial.as_view()),  # review의 Detail 목록
    path('alarm/', views.Groad_alarm_List.as_view()),               # alarm의 목록
    path('alarm/<int:fk>/', views.Groad_alarm_Detail.as_view()),    # alarm의 Detail 목록
    path('qrcode/', views.Groad_qrcode_List.as_view()),             # qrcode의 목록
    path('qrcode/<int:fk>/', views.Groad_qrcode_Detail.as_view()),  # qrcode의 Detail 목록
]

urlpatterns = format_suffix_patterns(urlpatterns)