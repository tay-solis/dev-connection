# Generated by Django 2.1.2 on 2018-10-29 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev_connect', '0003_auto_20181029_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='image',
            field=models.ImageField(blank=True, default='media/default.jpg', upload_to='profile_pics'),
        ),
    ]