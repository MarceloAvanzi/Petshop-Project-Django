# Generated by Django 4.1 on 2023-02-15 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0027_alter_agendamento_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='data',
            field=models.DateField(),
        ),
    ]
