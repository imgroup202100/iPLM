# Generated by Django 3.1.5 on 2021-05-20 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0007_auto_20210518_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultyapplicant',
            name='TOR',
            field=models.FileField(null=True, upload_to='facultyApplicant/'),
        ),
        migrations.AddField(
            model_name='facultyapplicant',
            name='certificates',
            field=models.FileField(null=True, upload_to='facultyApplicant/'),
        ),
        migrations.AddField(
            model_name='facultyapplicant',
            name='credentials',
            field=models.FileField(null=True, upload_to='facultyApplicant/'),
        ),
    ]
