# Generated by Django 5.2 on 2025-04-07 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSeriesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('sensor1', models.FloatField()),
                ('sensor2', models.FloatField()),
                ('sensor3', models.FloatField()),
                ('correlation_s1_s2', models.FloatField(blank=True, null=True)),
                ('correlation_s2_s3', models.FloatField(blank=True, null=True)),
                ('correlation_s1_s3', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
