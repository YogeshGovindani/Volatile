# Generated by Django 3.1 on 2021-07-02 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comp_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contest',
            old_name='user_id',
            new_name='creator',
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=500)),
                ('input_cases', models.CharField(max_length=500)),
                ('output_cases', models.CharField(max_length=500)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comp_app.contest')),
            ],
        ),
    ]
