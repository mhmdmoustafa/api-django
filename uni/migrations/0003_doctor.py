# Generated by Django 3.0.3 on 2020-02-11 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0002_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('dept_id', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]