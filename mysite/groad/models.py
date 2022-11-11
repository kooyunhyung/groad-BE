from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class user(models.Model):
    gu_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gu_id = models.CharField(max_length=20, verbose_name='아이디', null=True)
    gu_pw = models.CharField(max_length=16, verbose_name='비밀번호', null=True)
    gu_name = models.CharField(max_length=6, verbose_name='이름', null=True)
    gu_gender = models.CharField(max_length=1, null=True, verbose_name='성별', default='M')
    gu_birth_date = models.CharField(max_length=20, verbose_name='생년월일', null=True)
    gu_email = models.CharField(max_length=40, verbose_name='이메일', null=True)
    gu_phone_number = models.CharField(max_length=11, verbose_name='핸드폰번호', null=True)
    gu_point_number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)],
                                   verbose_name='포인트', default=0, null=True)
    gu_profile_image = models.CharField(max_length=500,null=True)

class review(models.Model):
    gr_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gr_name = models.CharField(max_length=10, verbose_name='닉네임', null=True)
    gr_place = models.CharField(max_length=20, verbose_name='장소', null=True)
    gr_content_text = models.CharField(max_length=100, verbose_name='코멘트', null=True)
    gr_grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],
                                   verbose_name='평점', default=0, null=True)
    gr_date = models.DateTimeField(null=True, default=0, verbose_name='게시 시간')
    gr_content_image = models.CharField(max_length=500, verbose_name='장소', null=True)
    gr_profile_image = models.CharField(max_length=500, verbose_name='프로필사진', null=True)
    gr_gu_seq = models.ForeignKey(user, verbose_name='리뷰어', on_delete=models.CASCADE, related_name='gr_gu_seq')

class review_comment(models.Model):
    grc_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    grc_name = models.CharField(max_length=20, null=True)
    grc_profile_image = models.CharField(max_length=500, null=True)
    grc_comment = models.CharField(max_length=300,null=True)
    grc_gr_seq = models.ForeignKey(review, on_delete=models.CASCADE, related_name='grc_gr_seq')

class travelcourse(models.Model):
    gt_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gt_course_title = models.CharField(max_length=100, null=True)
    gt_course_name1 = models.CharField(max_length=100, null=True)
    gt_course_name2 = models.CharField(max_length=100, null=True)
    gt_course_name3 = models.CharField(max_length=100, null=True)
    gt_course_name4 = models.CharField(max_length=100, null=True)
    gt_course_name5 = models.CharField(max_length=100, null=True)
    gt_course_Id1 = models.CharField(max_length=100, null=True)
    gt_course_Id2 = models.CharField(max_length=100, null=True)
    gt_course_Id3 = models.CharField(max_length=100, null=True)
    gt_course_Id4 = models.CharField(max_length=100, null=True)
    gt_course_Id5 = models.CharField(max_length=100, null=True)
    gt_course_lat1 = models.FloatField(null=True)
    gt_course_lat2 = models.FloatField(null=True)
    gt_course_lat3 = models.FloatField(null=True)
    gt_course_lat4 = models.FloatField(null=True)
    gt_course_lat5 = models.FloatField(null=True)
    gt_course_lng1 = models.FloatField(null=True)
    gt_course_lng2 = models.FloatField(null=True)
    gt_course_lng3 = models.FloatField(null=True)
    gt_course_lng4 = models.FloatField(null=True)
    gt_course_lng5 = models.FloatField(null=True)
    gt_camera_lat = models.FloatField(null=True)
    gt_camera_lng = models.FloatField(null=True)
    gt_zoom = models.FloatField(null=True)
    gt_course_key = models.IntegerField(null=True)
    gt_distance = models.FloatField(null=True)
    gt_time = models.CharField(max_length=20,null=True)
    gt_title_image = models.CharField(max_length=100,null=True)

class course1Position(models.Model):
    gc_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gc_main_image = models.CharField(max_length=500, null=True)
    gc_sub_image1 = models.CharField(max_length=500, null=True)
    gc_sub_image2 = models.CharField(max_length=500, null=True)
    gc_sub_image3 = models.CharField(max_length=500, null=True)
    gc_text = models.CharField(max_length=2000, null=True)
    gc_traffic12 = models.CharField(max_length=1000, null=True)
    gc_traffic23 = models.CharField(max_length=1000, null=True)
    gc_traffic34 = models.CharField(max_length=1000, null=True)
    gc_traffic45 = models.CharField(max_length=1000, null=True)

class course2Position(models.Model):
    gc_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gc_main_image = models.CharField(max_length=500, null=True)
    gc_sub_image1 = models.CharField(max_length=500, null=True)
    gc_sub_image2 = models.CharField(max_length=500, null=True)
    gc_sub_image3 = models.CharField(max_length=500, null=True)
    gc_text = models.CharField(max_length=2000, null=True)
    gc_traffic12 = models.CharField(max_length=1000, null=True)
    gc_traffic23 = models.CharField(max_length=1000, null=True)
    gc_traffic34 = models.CharField(max_length=1000, null=True)
    gc_traffic45 = models.CharField(max_length=1000, null=True)

class course3Position(models.Model):
    gc_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gc_main_image = models.CharField(max_length=500, null=True)
    gc_sub_image1 = models.CharField(max_length=500, null=True)
    gc_sub_image2 = models.CharField(max_length=500, null=True)
    gc_sub_image3 = models.CharField(max_length=500, null=True)
    gc_text = models.CharField(max_length=2000, null=True)
    gc_traffic12 = models.CharField(max_length=1000, null=True)
    gc_traffic23 = models.CharField(max_length=1000, null=True)
    gc_traffic34 = models.CharField(max_length=1000, null=True)
    gc_traffic45 = models.CharField(max_length=1000, null=True)

class course4Position(models.Model):
    gc_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gc_main_image = models.CharField(max_length=500, null=True)
    gc_sub_image1 = models.CharField(max_length=500, null=True)
    gc_sub_image2 = models.CharField(max_length=500, null=True)
    gc_sub_image3 = models.CharField(max_length=500, null=True)
    gc_text = models.CharField(max_length=2000, null=True)
    gc_traffic12 = models.CharField(max_length=1000, null=True)
    gc_traffic23 = models.CharField(max_length=1000, null=True)
    gc_traffic34 = models.CharField(max_length=1000, null=True)
    gc_traffic45 = models.CharField(max_length=1000, null=True)

class course5Position(models.Model):
    gc_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gc_main_image = models.CharField(max_length=500, null=True)
    gc_sub_image1 = models.CharField(max_length=500, null=True)
    gc_sub_image2 = models.CharField(max_length=500, null=True)
    gc_sub_image3 = models.CharField(max_length=500, null=True)
    gc_text = models.CharField(max_length=2000, null=True)
    gc_traffic12 = models.CharField(max_length=1000, null=True)
    gc_traffic23 = models.CharField(max_length=1000, null=True)
    gc_traffic34 = models.CharField(max_length=1000, null=True)
    gc_traffic45 = models.CharField(max_length=1000, null=True)

class course6Position(models.Model):
    gc_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gc_main_image = models.CharField(max_length=500, null=True)
    gc_sub_image1 = models.CharField(max_length=500, null=True)
    gc_sub_image2 = models.CharField(max_length=500, null=True)
    gc_sub_image3 = models.CharField(max_length=500, null=True)
    gc_text = models.CharField(max_length=2000, null=True)
    gc_traffic12 = models.CharField(max_length=1000, null=True)
    gc_traffic23 = models.CharField(max_length=1000, null=True)
    gc_traffic34 = models.CharField(max_length=1000, null=True)
    gc_traffic45 = models.CharField(max_length=1000, null=True)

class course7Position(models.Model):
    gc_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gc_main_image = models.CharField(max_length=500, null=True)
    gc_sub_image1 = models.CharField(max_length=500, null=True)
    gc_sub_image2 = models.CharField(max_length=500, null=True)
    gc_sub_image3 = models.CharField(max_length=500, null=True)
    gc_text = models.CharField(max_length=2000, null=True)
    gc_traffic12 = models.CharField(max_length=1000, null=True)
    gc_traffic23 = models.CharField(max_length=1000, null=True)
    gc_traffic34 = models.CharField(max_length=1000, null=True)
    gc_traffic45 = models.CharField(max_length=1000, null=True)

class course8Position(models.Model):
    gc_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gc_main_image = models.CharField(max_length=500, null=True)
    gc_sub_image1 = models.CharField(max_length=500, null=True)
    gc_sub_image2 = models.CharField(max_length=500, null=True)
    gc_sub_image3 = models.CharField(max_length=500, null=True)
    gc_text = models.CharField(max_length=2000, null=True)
    gc_traffic12 = models.CharField(max_length=1000, null=True)
    gc_traffic23 = models.CharField(max_length=1000, null=True)
    gc_traffic34 = models.CharField(max_length=1000, null=True)
    gc_traffic45 = models.CharField(max_length=1000, null=True)

class course9Position(models.Model):
    gc_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gc_main_image = models.CharField(max_length=500, null=True)
    gc_sub_image1 = models.CharField(max_length=500, null=True)
    gc_sub_image2 = models.CharField(max_length=500, null=True)
    gc_sub_image3 = models.CharField(max_length=500, null=True)
    gc_text = models.CharField(max_length=2000, null=True)
    gc_traffic12 = models.CharField(max_length=1000, null=True)
    gc_traffic23 = models.CharField(max_length=1000, null=True)
    gc_traffic34 = models.CharField(max_length=1000, null=True)
    gc_traffic45 = models.CharField(max_length=1000, null=True)

class inquiry(models.Model):
    gi_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gi_title = models.CharField(max_length=30, null=True)
    gi_contents = models.CharField(max_length=200, null=True)
    gi_gu_seq = models.ForeignKey(user, on_delete=models.CASCADE, related_name='gi_gu_seq')

class setting(models.Model):
    gs_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gs_map = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],
                                        default=0, null=True)
    gs_theme = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],
                                        default=0, null=True)
    gs_onoff1 = models.BooleanField(default=False)
    gs_onoff2 = models.BooleanField(default=False)
    gs_onoff3 = models.BooleanField(default=False)
    gs_gu_seq = models.ForeignKey(user, on_delete=models.CASCADE, related_name='gs_gu_seq')
