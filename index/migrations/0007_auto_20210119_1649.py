# Generated by Django 3.1.5 on 2021-01-19 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20210119_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdetail',
            name='app_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.appindex'),
        ),
    ]
