# Generated by Django 3.1.8 on 2023-02-03 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20230202_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workschedule',
            old_name='Employee_ID',
            new_name='Employee_No',
        ),
        migrations.RenameField(
            model_name='workschedule',
            old_name='DateTimeNow',
            new_name='EndTime',
        ),
        migrations.RenameField(
            model_name='workschedule',
            old_name='status',
            new_name='Mark',
        ),
        migrations.RenameField(
            model_name='workschedule',
            old_name='InTime',
            new_name='StartDate',
        ),
        migrations.RenameField(
            model_name='workschedule',
            old_name='OutTime',
            new_name='WorkDate',
        ),
        migrations.AlterModelTable(
            name='workschedule',
            table='WorkSchedule',
        ),
    ]
