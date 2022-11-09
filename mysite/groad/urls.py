from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'groad'

urlpatterns = [
    path('user/', views.Groad_user_List.as_view()),  # user의 목록
    path('user/login/', views.Groad_user_login.as_view()),  # user의 login
    path('user/<int:pk>/', views.Groad_user_Detail.as_view()),  # user의 Detail 목록
    path('review/', views.Groad_review_List.as_view()),  # review의 목록
    path('review/<int:fk>/', views.Groad_review_Detial.as_view()),  # review의 Detail 목록
    path('review_comment/', views.Groad_review_comment_List.as_view()),
    path('review_comment/<int:fk>', views.Groad_review_comment_Detial.as_view()),
    path('review_share/', views.Groad_review_share_List.as_view()),
    path('review_share/<int:fk>', views.Groad_review_share_Detial.as_view()),
    path('inquiry/', views.Groad_inquiry_List.as_view()),
    path('inquiry/<int:fk>', views.Groad_inquiry_Detial.as_view()),
    path('setting/', views.Groad_setting_List.as_view()),
    path('setting/<int:fk>', views.Groad_setting_Detail.as_view()),
    path('travelcourse/', views.Groad_travelcourse_List.as_view()),
    path('course1position/', views.Groad_course1position_List.as_view()),
    path('course2position/', views.Groad_course2position_List.as_view()),
    path('course3position/', views.Groad_course3position_List.as_view()),
    path('course4position/', views.Groad_course4position_List.as_view()),
    path('course5position/', views.Groad_course5position_List.as_view()),
    path('course6position/', views.Groad_course6position_List.as_view()),
    path('course7position/', views.Groad_course7position_List.as_view()),
    path('course8position/', views.Groad_course8position_List.as_view()),
    path('course9position/', views.Groad_course9position_List.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
