# Generated by Django 3.0.7 on 2020-06-14 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flash_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=3000)),
                ('answer', models.CharField(max_length=3000)),
            ],
        ),
    ]