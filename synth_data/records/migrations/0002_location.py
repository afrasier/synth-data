# Generated by Django 2.0.5 on 2018-05-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(help_text='The city name', max_length=120)),
                ('state', models.CharField(help_text='The state (or province) name', max_length=120)),
                ('postal_code', models.CharField(help_text='The 5-digit postal code', max_length=5)),
                ('postal_code_type', models.CharField(help_text='The postal code type', max_length=120)),
                ('latitude', models.FloatField(help_text='The latitude of the location', null=True)),
                ('longitude', models.FloatField(help_text='The longitude of the location', null=True)),
            ],
        ),
    ]
