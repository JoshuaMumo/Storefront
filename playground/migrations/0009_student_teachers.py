# Generated by Django 5.0.6 on 2024-06-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0008_teacher_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(blank=True, to='playground.teacher'),
        ),
    ]
