# Generated by Django 4.2 on 2024-02-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iprs', '0009_remove_comment_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('In progress', 'В работе'), ('Done', 'Выполнен'), ('Failed', 'Не выполнен'), ('Canceled', 'Отменен'), ('No status', 'Отсутствует')], default='no_status', max_length=20, verbose_name='Статус'),
        ),
    ]