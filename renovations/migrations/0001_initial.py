# Generated by Django 2.2.1 on 2019-05-24 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[(1, 'Armature'), (2, 'Tiles'), (3, 'Paint'), (4, 'Other')])),
            ],
        ),
    ]
