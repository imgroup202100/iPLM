# Generated by Django 3.1.5 on 2021-05-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0012_auto_20210521_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyapplicant',
            name='CV',
            field=models.FileField(default=None, upload_to='facultyApplicant/'),
        ),
        migrations.AlterField(
            model_name='facultyapplicant',
            name='TOR',
            field=models.FileField(default=None, upload_to='facultyApplicant/'),
        ),
        migrations.AlterField(
            model_name='facultyapplicant',
            name='certificates',
            field=models.FileField(default=None, upload_to='facultyApplicant/'),
        ),
        migrations.AlterField(
            model_name='facultyapplicant',
            name='credentials',
            field=models.FileField(default=None, upload_to='facultyApplicant/'),
        ),
    ]
