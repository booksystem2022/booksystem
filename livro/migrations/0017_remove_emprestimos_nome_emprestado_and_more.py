# Generated by Django 4.0.3 on 2022-05-29 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0016_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimos',
            name='nome_emprestado',
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 9, 35, 25, 617698)),
        ),
    ]
