# Generated by Django 5.1.7 on 2025-03-28 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_rename_metin_post_body_rename_baslik_post_title_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="title",
            new_name="baslik",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="body",
            new_name="metin",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="author",
            new_name="yazar",
        ),
    ]
