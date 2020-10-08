# Generated by Django 2.0.7 on 2020-10-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('course', models.CharField(max_length=40)),
                ('Stream', models.CharField(max_length=40)),
                ('admission_id', models.IntegerField()),
            ],
        ),
    ]
