# Generated by Django 3.0.8 on 2020-10-30 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.CharField(default='project type', max_length=75),
            preserve_default=False,
        ),
    ]
