# Generated by Django 2.0.7 on 2020-10-07 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
