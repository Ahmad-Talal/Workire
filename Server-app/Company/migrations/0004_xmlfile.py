# Generated by Django 3.2.3 on 2021-05-17 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0003_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='xmlFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
