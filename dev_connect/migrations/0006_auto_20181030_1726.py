# Generated by Django 2.1.2 on 2018-10-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev_connect', '0005_auto_20181029_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]