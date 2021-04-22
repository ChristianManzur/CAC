# Generated by Django 3.1.7 on 2021-03-12 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20210311_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_image', models.ImageField(upload_to='pics')),
                ('event_image', models.ImageField(upload_to='pics')),
                ('date', models.DateField()),
                ('event_title', models.CharField(default=None, max_length=120)),
                ('event_description', models.TextField()),
                ('position_to_right', models.BooleanField()),
            ],
        ),
    ]
