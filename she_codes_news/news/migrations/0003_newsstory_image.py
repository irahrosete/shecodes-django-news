# Generated by Django 4.1.3 on 2022-12-10 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_newsstory_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]