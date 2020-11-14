# Generated by Django 3.1.3 on 2020-11-14 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample1', models.IntegerField(blank=True, null=True, verbose_name='sample1')),
                ('sample2', models.CharField(blank=True, max_length=255, null=True, verbose_name='sample2')),
            ],
            options={
                'verbose_name_plural': 'sample_table',
                'db_table': 'sample_table',
            },
        ),
    ]
