# Generated by Django 3.0.7 on 2020-07-13 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.DecimalField(decimal_places=0, max_digits=5)),
                ('cart', models.TextField()),
                ('user', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
