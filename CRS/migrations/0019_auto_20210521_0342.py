# Generated by Django 3.1.5 on 2021-05-20 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0018_auto_20210521_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyapplicant',
            name='CV',
            field=models.FileField(blank=True, upload_to='facultyApplicant/'),
        ),
    ]
