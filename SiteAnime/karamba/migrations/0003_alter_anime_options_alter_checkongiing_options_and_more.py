# Generated by Django 4.2.3 on 2023-07-08 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karamba', '0002_checkongiing_anime_check_ongoing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anime',
            options={'verbose_name': 'Аниме', 'verbose_name_plural': 'Аниме'},
        ),
        migrations.AlterModelOptions(
            name='checkongiing',
            options={'verbose_name': 'Статус Аниме', 'verbose_name_plural': 'Статусы Аниме'},
        ),
        migrations.AlterModelOptions(
            name='ganres',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='studios',
            options={'verbose_name': 'Студия', 'verbose_name_plural': 'Студии'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AlterField(
            model_name='anime',
            name='check_Ongoing',
            field=models.ManyToManyField(blank=True, default='Вышел', related_name='anime_status', to='karamba.checkongiing'),
        ),
    ]
