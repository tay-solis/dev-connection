# Generated by Django 2.1.2 on 2018-10-29 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev_connect', '0002_auto_20181029_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='image',
            field=models.ImageField(blank=True, default='../static/images/default.jpg', upload_to='profile_pics'),
        ),
    ]