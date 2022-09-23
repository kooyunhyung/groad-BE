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

class pedometer(models.Model):
    gp_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gp_step = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)],
                                   verbose_name='걸음수', default=0, null=True)
    gp_gu_seq = models.ForeignKey(user, verbose_name='순례자', on_delete=models.CASCADE, related_name='gp_gu_seq')

class review(models.Model):
    gr_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gr_nickname = models.CharField(max_length=10, verbose_name='닉네임', null=True)
    gr_place = models.CharField(max_length=20, verbose_name='장소', null=True)
    gr_comment = models.CharField(max_length=100, verbose_name='코멘트', null=True)
    gr_grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],
                                   verbose_name='평점', default=0, null=True)
    gr_gu_seq = models.ForeignKey(user, verbose_name='리뷰어', on_delete=models.CASCADE, related_name='gr_gu_seq')

class alarm(models.Model):
    ga_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    ga_onoff1 = models.BooleanField(default=False)
    ga_onoff2 = models.BooleanField(default=False)
    ga_onoff3 = models.BooleanField(default=False)
    ga_gu_seq = models.ForeignKey(user, verbose_name='알리머', on_delete=models.CASCADE, related_name='ga_gu_seq')

class qrcode(models.Model):
    gq_seq = models.AutoField(primary_key=True, verbose_name='시퀀스',
                              validators=[MinValueValidator(0), MaxValueValidator(9999)])
    gq_qrcode = models.CharField(max_length=100, verbose_name='qrcode', null=True)
    gq_gu_seq = models.ForeignKey(user, verbose_name='순례자', on_delete=models.CASCADE, related_name='gq_gu_seq')

