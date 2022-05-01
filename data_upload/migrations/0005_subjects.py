# Generated by Django 3.2.6 on 2022-05-01 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_upload', '0004_exampaper_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=100, null=True)),
                ('subject_code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
    ]
