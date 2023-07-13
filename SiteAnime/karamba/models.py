from django.db import models
from django.urls import reverse
from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import *
from django.contrib.auth.models import User


class Anime(models.Model):
    check_True = models.PositiveIntegerField(default='1')
    check_Ongoing = models.ManyToManyField(
        'CheckOngiing',
        default='Вышел',
        related_name='anime_status',
        blank=True,
    )
    title = models.CharField(max_length=100)
    original_anime = models.CharField(max_length=200)
    descriptions = models.TextField()
    grade = models.FloatField(blank=True, default='0')
    grade_time = models.PositiveIntegerField(blank=True, default='0')
    objects = models.Manager()
    Number_episodes = models.CharField(max_length=100, blank=True)
    Number_seasons = models.CharField(max_length=100, blank=True)
    Number_films = models.CharField(max_length=100, blank=True)
    year = models.PositiveIntegerField()
    views = models.PositiveIntegerField(blank=True, default='0')
    Plot_Grade = models.PositiveIntegerField(default='0')
    Animation_Grade = models.PositiveIntegerField(default='0')
    Characters_Grade = models.PositiveIntegerField(default='0')
    World_Grade = models.PositiveIntegerField(default='0')
    IMHO_Grade = models.PositiveIntegerField(default='0')
    ganre = models.ManyToManyField(
        'Ganres',
        related_name='anime_ganres',
        blank=True,
    )
    photo = models.ImageField(upload_to='articles/')
    studio = models.ForeignKey(
        'Studios',
        related_name='anime_studios',
        on_delete=models.CASCADE,
        null=True,
    )
    url = models.SlugField(max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse("AnimeDetailPage", kwargs={"slug": self.url})

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Аниме"
        verbose_name_plural = "Аниме"


class CheckOngiing(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slag = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Статус Аниме"
        verbose_name_plural = "Статусы Аниме"


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField("Значение", default=0)

    def ___str___(self):
        return self.value


    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Звезда")
    anime = models.ForeignKey(Anime, on_delete=models.CharField, verbose_name="Аниме")

    def __str__(self):
        return f"{self.star} - {self.anime}"


    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class AnimeShots(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    descriptions = models.TextField("Описание")
    image = models.ImageField("", upload_to="shots/")
    anime = models.ForeignKey(Anime, verbose_name="Аниме", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Скриншот"
        verbose_name_plural = "Скриншоты"


class Ganres(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slag = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slag = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Studios(models.Model):
    name = models.CharField(max_length=100)
    slag = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Студия"
        verbose_name_plural = "Студии"


class Post(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=100)
    parent = models.ForeignKey(
        "self", verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    anime = models.ForeignKey(Anime, verbose_name="Аниме", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.anime}"


    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
