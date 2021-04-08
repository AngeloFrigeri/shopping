# Generated by Django 3.2 on 2021-04-08 13:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('price', models.FloatField(verbose_name='Preço')),
                ('image', models.ImageField(upload_to='', verbose_name='Imagem')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.brand', verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.datetime(2021, 4, 8, 13, 54, 3, 6194), verbose_name='Data')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
        migrations.CreateModel(
            name='ProductExit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(verbose_name='Quantidade')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product', verbose_name='Produto')),
                ('sell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.sell', verbose_name='Venda')),
            ],
            options={
                'verbose_name': 'Item de Venda',
                'verbose_name_plural': 'Itens de Venda',
            },
        ),
        migrations.CreateModel(
            name='ProductEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(verbose_name='Quantidade')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Entrada de Produto',
                'verbose_name_plural': 'Entradas de Produtos',
            },
        ),
    ]