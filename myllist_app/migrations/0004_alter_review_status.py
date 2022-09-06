# Generated by Django 4.0.6 on 2022-07-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myllist_app', '0003_alter_review_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='status',
            field=models.CharField(blank=True, choices=[('none', 'None'), ('plan', 'Plan'), ('watching', 'Watching'), ('completed', 'Completed')], default='none', max_length=50, null=True),
        ),
    ]
