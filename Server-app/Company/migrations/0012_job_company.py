# Generated by Django 3.2.3 on 2021-05-17 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0011_alter_job_logourl'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.company'),
        ),
    ]
