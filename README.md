# 프로젝트 이름

  한림대학교 캡스톤 디자인 춘천 관광 앱 (GROAD) -> django framework 이용한 python 코드 (백엔드)

# 설치

  python 코드를 작성할 수 있는 개발환경 툴을 열고 Django를 설치합니다.

    pip install django

  DJANGO REST FRAMEWORK로 API 를 만들기 위해 django restframework를 설치합니다.

    pip install djangorestframework

# 파일 구조

    mysite/
    ├── .idea
    ├── mysite
    ├── polls
    ├── templates/admin
    ├── db.sqlite3
    ├── manage.py
    └── groad
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations
        │   └── __init__.py
        ├── models.py
        ├── serializer.py
        ├── tests.py
        ├── urls.py
        └── views.py
    

# 시작하기
  로컬 환경에 깃을 설치하고 원하는 디렉토리에 다음 명령어를 입력하여 코드를 다운 받습니다.

    git clone https://github.com/kooyunhyung/groad-BE.git

  mysite/settings.py 파일에 HOST와 DATABASE 설정을 해야합니다.

    ALLOWED_HOSTS = ['{HOST_IP_ADDRESS}']
    

    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'groad',
          'USER': '{DATABASE_ID}',
          'PASSWORD': '{DATABASE_PASSWORD}',
          'HOST': '{HOST_IP_ADDRESS}',
          'PORT': '{DATABASE_PORT}',
      }

  manage.py 파일이 존재하는 디렉토리로 이동한 후 다음 명령어를 입력하여 models.py에 작성해둔 django ORM 코드가 실제 DB에 반영되도록 합니다.

    python manage.py makemigrations [app_name]

    python manage.py migrate [app_name] [migration_name]

  manage.py 파일이 존재하는 디렉토리로 이동한 후 다음 명령어를 입력하여 서버를 구동합니다.

    python manage.py runserver
    
# 클라이언트와의 통신 구현 위한 API 정보

▶ 유저정보, 로그인 (GET, POST, UPDATE, DELETE)
  
▶ 사용자 후기 (GET, POST, UPDATE, DELETE)

▶ 사용자 후기 댓글 (GET, POST, UPDATE, DELETE)

▶ 설정 알림 (GET, POST, UPDATE)

▶ 코스 거점 정보 (GET)

▶ 카페 리스트 정보 (GET)

▶ 맛집 리스트 정보 (GET)

▶ 숙소 리스트 정보 (GET)

# 데이터베이스 구조 (mariadb)

  db: graoddb
  
      table: user
             column: gu_seq, gu_id, gu_pw, gu_name, gu_gender, gu_birth_date, gu_email, gu_phone_number, gu_point_number, gu_profile_image, gu_step_number
             
      table: review
             column: gr_seq, gr_name, gr_place, gr_content_text, gr_grade, gr_date, gr_content_image, gr_profile_image, gr_gu_seq
      
      table: review_comment
             column: grc_seq, grc_name, grc_profile_image, grc_comment, grc_gr_seq
             
      table: tavelcourse
             column: gt_seq, gt_course_title, gt_course_name1, gt_course_name2, gt_course_name3, gt_course_name4, gt_course_name5, gt_course_Id1, gt_course_Id2,
             gt_course_Id3, gt_course_Id4, gt_course_Id5, gt_course_lat1, gt_course_lat2, gt_course_lat3, gt_course_lat4, gt_course_lat5, gt_course_lng1, 
             gt_course_lng2, gt_course_lng3, gt_course_lng4, gt_course_lng5, gt_camera_lat, gt_camera_lng, gt_zoom, gt_course_key, gt_distance, gt_time, 
             gt_title_image
       
      table: course1Position
             column: gc_seq, gc_main_image, gc_sub_image1, gc_sub_image2, gc_sub_image3, gc_text, gc_traffic12, gc_traffic23, gc_traffic34, gc_traffic45

      table: course2Position
             column: gc_seq, gc_main_image, gc_sub_image1, gc_sub_image2, gc_sub_image3, gc_text, gc_traffic12, gc_traffic23, gc_traffic34, gc_traffic45
             
      table: course3Position
             column: gc_seq, gc_main_image, gc_sub_image1, gc_sub_image2, gc_sub_image3, gc_text, gc_traffic12, gc_traffic23, gc_traffic34, gc_traffic45
             
      table: course4Position
             column: gc_seq, gc_main_image, gc_sub_image1, gc_sub_image2, gc_sub_image3, gc_text, gc_traffic12, gc_traffic23, gc_traffic34, gc_traffic45
             
      table: course5Position
             column: gc_seq, gc_main_image, gc_sub_image1, gc_sub_image2, gc_sub_image3, gc_text, gc_traffic12, gc_traffic23, gc_traffic34, gc_traffic45
             
      table: course6Position
             column: gc_seq, gc_main_image, gc_sub_image1, gc_sub_image2, gc_sub_image3, gc_text, gc_traffic12, gc_traffic23, gc_traffic34, gc_traffic45
             
      table: course7Position
             column: gc_seq, gc_main_image, gc_sub_image1, gc_sub_image2, gc_sub_image3, gc_text, gc_traffic12, gc_traffic23, gc_traffic34, gc_traffic45
             
      table: course8Position
             column: gc_seq, gc_main_image, gc_sub_image1, gc_sub_image2, gc_sub_image3, gc_text, gc_traffic12, gc_traffic23, gc_traffic34, gc_traffic45
             
      table: course9Position
             column: gc_seq, gc_main_image, gc_sub_image1, gc_sub_image2, gc_sub_image3, gc_text, gc_traffic12, gc_traffic23, gc_traffic34, gc_traffic45
             
      table: cafe_list
             column: gcl_seq, gcl_main_image, gcl_name, gcl_lat, gcl_lng, gcl_info, gcl_course
             
      table: photo_list
             column: gpl_seq, gpl_main_image, gpl_name, gpl_lat, gpl_lng, gpl_info, gpl_course
             
      table: restaurant_list
             column: grl_seq, grl_main_image, grl_name, grl_lat, grl_lng, grl_info, grl_course
             
      table: lodging_list
             column: gll_seq, gll_main_image, gll_name, gll_lat, gll_lng, gll_info, gll_course
             
      table: inquiry
             column: gi_seq, gi_title, gi_contents, gi_gu_seq
             
      table: setting
             column: gs_seq, gs_map, gs_theme, gs_onoff1, gs_onoff2, gs_onoff3, gs_gu_seq
             
# REST API 문서

![스크린샷 2023-06-27 213633](https://github.com/kooyunhyung/groad-BE/assets/77048218/2562a356-8821-4779-b0fb-986724e2b188)

![스크린샷 2023-06-27 213705](https://github.com/kooyunhyung/groad-BE/assets/77048218/aebd63e6-c0b1-4d74-91fa-f73427c62a44)

![스크린샷 2023-06-27 213735](https://github.com/kooyunhyung/groad-BE/assets/77048218/0ba31063-fd74-4266-a0c7-c7d9c7ed9a00)

![스크린샷 2023-06-27 213751](https://github.com/kooyunhyung/groad-BE/assets/77048218/493983c5-45b7-4f76-b5a4-5b8000dc689e)

![스크린샷 2023-06-27 213833](https://github.com/kooyunhyung/groad-BE/assets/77048218/a16fc456-df3e-4510-8fac-6153fd54ec87)

![스크린샷 2023-06-27 213852](https://github.com/kooyunhyung/groad-BE/assets/77048218/93696e6b-ef5a-46c5-9b9f-98d56f15cc7c)

![스크린샷 2023-06-27 213906](https://github.com/kooyunhyung/groad-BE/assets/77048218/11c18981-34d7-4f63-8a2c-70a55ef44756)


    
