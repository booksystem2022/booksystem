# Generated by Django 4.0.3 on 2022-05-20 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0014_alter_emprestimos_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='avaliacao',
            field=models.CharField(blank=True, choices=[('P', 'Péssimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Ótimo')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 20, 14, 41, 31, 572895)),
        ),
    ]
