# Generated by Django 4.0.6 on 2022-07-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myllist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='status',
            field=models.CharField(choices=[('none', 'None'), ('plan', 'Plan'), ('watching', 'Watching'), ('completed', 'Completed')], default='none', max_length=50),
        ),
    ]
