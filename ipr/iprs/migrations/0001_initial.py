# Generated by Django 4.2 on 2024-01-24 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ipr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название ИПР')),
                ('description', models.TextField(max_length=200, verbose_name='Описание ИПР')),
                ('status', models.CharField(choices=[('Not started', 'Не начат'), ('In progress', 'В работе'), ('Done', 'Выполнен'), ('Canceled', 'Отменен'), ('No status', 'Отсутствует')], default='No status', max_length=11, verbose_name='Статус ИПР')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания ИПР')),
                ('end_date', models.DateTimeField(verbose_name='Дата завершения ИПР')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ipr_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор ИПР')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ipr_employee', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'ИПР',
                'verbose_name_plural': 'ИПР',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('none', 'Отсутствует'), ('in_progress', 'В работе'), ('done', 'Выполнен'), ('not_done', 'Не выполнен'), ('canceled', 'Отменен')], default='none', max_length=20, verbose_name='Статус')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='Дедлайн')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('ipr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_ipr', to='iprs.ipr', verbose_name='ИПР')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ('-author',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='iprs.comment')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='iprs.task')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
                'ordering': ('id',),
            },
        ),
        migrations.AddConstraint(
            model_name='ipr',
            constraint=models.UniqueConstraint(fields=('title', 'employee'), name='unique_title_employee_iprs'),
        ),
    ]
