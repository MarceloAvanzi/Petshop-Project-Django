# Generated by Django 4.1 on 2023-03-07 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planos', '0002_remove_dadospagamentos_plano_dadospagamentos_planos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadospagamentos',
            name='Banhos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dadospagamentos',
            name='Tosas',
            field=models.IntegerField(default=0),
        ),
    ]