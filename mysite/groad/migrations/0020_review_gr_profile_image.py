# Generated by Django 4.0.6 on 2022-11-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groad', '0019_remove_review_comment_grc_comment_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='gr_profile_image',
            field=models.CharField(max_length=500, null=True, verbose_name='프로필사진'),
        ),
    ]