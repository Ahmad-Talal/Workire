# Generated by Django 3.2.3 on 2021-05-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0005_auto_20210517_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='AdditionalClassification1',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='AdditionalClassification2',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='AdditionalClassification3',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='AdditionalClassification4',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='AdvertiserName',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='AdvertiserType',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='Area',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='Classification',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='ContactName',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='Country',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='Description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='DescriptionURL',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='DisplayReference',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='Duration',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='EmploymentType',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='JobSource',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='JobSourceURL',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='JobType',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='Language',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='Location',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='LogoURL',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='Position',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='PostDate',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='PostalCode',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='SalaryAdditional',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='SalaryCurrency',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='SalaryMaximum',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='SalaryMinimum',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='SalaryPeriod',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='SenderReference',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='StartDate',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='SubClassification',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='VideoLinkURL',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='WorkHours',
            field=models.TextField(null=True),
        ),
    ]
