# Generated by Django 2.2.3 on 2019-07-27 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_plans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal_plans.Time')),
            ],
        ),
    ]
