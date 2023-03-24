# Generated by Django 3.2.6 on 2023-03-24 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=64)),
                ('link', models.CharField(max_length=64)),
                ('pdf', models.FileField(upload_to='')),
            ],
        ),
    ]