# Generated by Django 3.0.8 on 2020-07-22 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('cover', models.ImageField(upload_to='covers')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=50)),
                ('employer', models.CharField(max_length=100)),
                ('location', models.TextField(default=None)),
                ('image', models.ImageField(upload_to='job_cover')),
                ('badges', models.TextField(default=None)),
            ],
        ),
    ]
