# Generated by Django 3.2.6 on 2022-04-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendnotification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]