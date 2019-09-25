# Generated by Django 2.2.5 on 2019-09-25 12:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=255, verbose_name='Sobrenome')),
                ('data_de_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('item_de_doacao', models.CharField(max_length=255, verbose_name='Item de doação')),
                ('ativo', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de criação')),
            ],
        ),
    ]