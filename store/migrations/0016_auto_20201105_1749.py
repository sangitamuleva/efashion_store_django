# Generated by Django 3.1.2 on 2020-11-05 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20201105_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Pending', 'Pending'), ('On Hold', 'On Hold'), ('Open', 'Open'), ('Complete', 'Complete'), ('Closed', 'Closed'), ('Canceled', 'Canceled')], default='Processing', max_length=20),
        ),
    ]
