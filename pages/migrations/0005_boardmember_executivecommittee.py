# Generated by Django 3.1.7 on 2021-03-12 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('title', models.CharField(default=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='ExecutiveCommittee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('title', models.CharField(default=True, max_length=120)),
                ('subtitle', models.CharField(default=None, max_length=120)),
            ],
        ),
    ]
