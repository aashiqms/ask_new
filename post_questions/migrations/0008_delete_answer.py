# Generated by Django 3.0.5 on 2020-05-14 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_questions', '0007_answer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
    ]