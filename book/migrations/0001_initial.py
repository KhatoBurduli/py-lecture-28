# Generated by Django 5.2.3 on 2025-07-05 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Book', max_length=100)),
                ('author', models.CharField(default='Auhtor', max_length=100)),
                ('pages_count', models.IntegerField(default=0)),
            ],
        ),
    ]
