# Generated by Django 3.2.6 on 2022-04-17 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_upload', '0002_exampaper_created_by'),
        ('user', '0004_user_img_alter_user_created_by_alter_user_update_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='assigned_course',
            field=models.ManyToManyField(to='data_upload.Course'),
        ),
        migrations.AddField(
            model_name='user',
            name='assigned_semester',
            field=models.ManyToManyField(to='data_upload.Semester'),
        ),
    ]