# Generated by Django 3.1.8 on 2023-02-02 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employee_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Full_Name', models.CharField(max_length=100)),
                ('Job_Title', models.CharField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=100)),
                ('Email_Address', models.EmailField(max_length=254)),
                ('Profile_Image', models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')),
                ('Password', models.CharField(max_length=256)),
                ('Start_Date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('Role_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Role_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('WorkSchedule_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('DateTimeNow', models.DateTimeField()),
                ('status', models.CharField(max_length=256)),
                ('InTime', models.DateTimeField()),
                ('OutTime', models.DateTimeField()),
                ('Employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='index.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='Role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.role'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('Attendance_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('DateNow', models.DateField(null=True)),
                ('InTime', models.CharField(blank=True, max_length=256, null=True)),
                ('OutTime', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Present'), (2, 'Absent')], default=0)),
                ('Employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='index.employee')),
            ],
            options={
                'db_table': 'Attendance',
            },
        ),
    ]
