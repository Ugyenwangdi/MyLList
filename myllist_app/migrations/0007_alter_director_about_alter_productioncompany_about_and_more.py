# Generated by Django 4.0.6 on 2022-08-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myllist_app', '0006_alter_actor_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='about',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='productioncompany',
            name='about',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='streamingplatform',
            name='about',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='about',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
