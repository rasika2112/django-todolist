# Generated by Django 3.0.3 on 2020-05-14 09:52

from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_remove_todolistitem_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistitem',
            name='date',
            field=models.DateField(default=datetime.date.today()),
            preserve_default=False,
        ),
    ]