# Generated by Django 3.2.4 on 2021-06-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='email',
            field=models.EmailField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
