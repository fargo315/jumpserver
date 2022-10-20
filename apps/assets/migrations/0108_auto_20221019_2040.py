# Generated by Django 3.2.14 on 2022-10-19 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0107_auto_20221019_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='web',
            name='script',
            field=models.JSONField(blank=True, default=list, verbose_name='Script'),
        ),
        migrations.AddField(
            model_name='historicalaccount',
            name='version',
            field=models.IntegerField(default=0, verbose_name='Version'),
        ),
    ]
