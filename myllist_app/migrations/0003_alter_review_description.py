# Generated by Django 4.0.6 on 2022-07-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myllist_app', '0002_alter_review_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]