# Generated by Django 3.0.5 on 2020-05-08 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]