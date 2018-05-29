# Generated by Django 2.0.5 on 2018-05-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
            ],
        ),
    ]
