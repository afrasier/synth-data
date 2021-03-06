# Generated by Django 2.0.5 on 2018-05-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The family name', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='GivenName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The given name', max_length=120)),
                ('sex', models.CharField(help_text='A flag indicating the general sex of the name', max_length=1)),
            ],
        ),
    ]
