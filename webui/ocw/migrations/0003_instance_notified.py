# Generated by Django 2.1.7 on 2019-04-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocw', '0002_auto_20190401_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='notified',
            field=models.BooleanField(default=False),
        ),
    ]
