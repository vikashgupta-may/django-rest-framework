# Generated by Django 2.2.2 on 2019-06-07 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0006_auto_20181228_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='artproject',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
