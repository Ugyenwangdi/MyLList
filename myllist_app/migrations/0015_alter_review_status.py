# Generated by Django 4.0.6 on 2022-09-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myllist_app', '0014_show_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='status',
            field=models.CharField(blank=True, choices=[('None', 'none'), ('Plan', 'plan'), ('Watching', 'watching'), ('Completed', 'completed')], default='none', max_length=50, null=True),
        ),
    ]
