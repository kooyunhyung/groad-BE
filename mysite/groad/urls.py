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
                  path('alarm/', views.Groad_alarm_List.as_view()),  # alarm의 목록
                  path('alarm/<int:fk>/', views.Groad_alarm_Detail.as_view()),  # alarm의 Detail 목록
                  path('course1position/', views.Groad_course1position_List.as_view()),
                  path('course2position/', views.Groad_course2position_List.as_view()),
                  path('course3position/', views.Groad_course3position_List.as_view()),
                  path('course4position/', views.Groad_course4position_List.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
