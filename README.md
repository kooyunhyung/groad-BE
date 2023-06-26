# 프로젝트 이름

  한림대학교 캡스톤 디자인 춘천 관광 앱 (GROAD) -> django framework 이용한 python 코드 (백엔드)

3. groad_app 서버와의 통신 구현 위한 API

▶ 유저정보, 로그인 (GET, POST, UPDATE, DELETE)
  
▶ 사용자 후기 (GET, POST, UPDATE, DELETE)

▶ 사용자 후기 댓글 (GET, POST, UPDATE, DELETE)

▶ 설정 알림 (GET, POST, UPDATE)

▶ 코스 거점 정보 (GET)

▶ 카페 리스트 정보 (GET)

▶ 맛집 리스트 정보 (GET)

▶ 숙소 리스트 정보 (GET)

4. 데이터베이스 구조 (mariadb)

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
