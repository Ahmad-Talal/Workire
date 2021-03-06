# Generated by Django 3.2.3 on 2021-05-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0008_delete_xmlfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='AdvertiserName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='AdvertiserType',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='ApplicationURL',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='DescriptionURL',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='JobSourceURL',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='VideoLinkURL',
            field=models.URLField(null=True),
        ),
    ]
