# Generated by Django 3.1 on 2021-07-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp_app', '0006_solution_verdict'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='points',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
