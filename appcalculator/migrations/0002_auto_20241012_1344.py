# Generated by Django 3.1.2 on 2024-10-12 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appcalculator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appcalculator',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='appcalculator',
            name='hours',
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=100)),
                ('hours', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcalculator.appcalculator')),
            ],
            options={
                'db_table': 'feature',
            },
        ),
    ]
