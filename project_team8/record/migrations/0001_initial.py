# Generated by Django 3.2.19 on 2023-06-13 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_name', models.CharField(max_length=20)),
                ('leader', models.BooleanField(default=False)),
            ],
        ),
    ]
