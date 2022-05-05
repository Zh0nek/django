# Generated by Django 2.2.13 on 2022-05-04 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220504_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_img',
        ),
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(null=True),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]