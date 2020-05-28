# Generated by Django 2.0 on 2020-05-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=128, unique=True)),
                ('Password', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'Users',
                'ordering': ['UserID'],
            },
        ),
    ]
