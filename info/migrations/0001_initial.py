# Generated by Django 2.1.3 on 2019-08-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_htno', models.CharField(max_length=20)),
                ('student_email', models.EmailField(max_length=100)),
                ('student_gemder', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=8)),
            ],
        ),
    ]
