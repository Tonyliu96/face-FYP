# Generated by Django 3.1.8 on 2023-02-03 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20230203_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workschedule',
            name='WorkDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
