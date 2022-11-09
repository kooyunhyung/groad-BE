# Generated by Django 4.0.6 on 2022-11-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groad', '0015_rename_grc_flag_review_share_grs_flag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='gr_auth_count',
        ),
        migrations.RemoveField(
            model_name='review',
            name='gr_comment_count',
        ),
        migrations.AddField(
            model_name='review_comment',
            name='grc_comment_count',
            field=models.IntegerField(default=0, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='review_share',
            name='grc_auth_count',
            field=models.IntegerField(default=0, max_length=2000, null=True),
        ),
    ]