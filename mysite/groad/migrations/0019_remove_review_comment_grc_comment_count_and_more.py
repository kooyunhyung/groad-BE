# Generated by Django 4.0.6 on 2022-11-09 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groad', '0018_rename_grc_auth_count_review_share_grs_auth_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review_comment',
            name='grc_comment_count',
        ),
        migrations.DeleteModel(
            name='review_share',
        ),
    ]