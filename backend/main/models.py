from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator


User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=200,
                            unique=True,
                            blank=False,
                            verbose_name='Название тега')
    color = models.CharField(max_length=7,
                             default='#a33900',
                             verbose_name='Цвет тега')
    slug = models.SlugField(max_length=200,
                            unique=True,
                            verbose_name='Слаг тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Ингредиент',
                            )
    measurement_unit = models.CharField(
        max_length=200,
        verbose_name='Единица измерения',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name} {self.measurement_unit}'


class Recipe(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='recipes',
                               verbose_name='Автор рецепта')
    name = models.CharField(max_length=200,
                            verbose_name='Название рецепта')
    image = models.ImageField(upload_to='',
                              verbose_name='Изображение')
    text = models.TextField(verbose_name='Описание рецепта')

    ingredients = models.ManyToManyField(Ingredient,
                                         through='IngredientAmount',
                                         related_name='ingredients',
                                         verbose_name='Ингредиент',)
    tags = models.ManyToManyField(Tag,
                                  related_name='tags',
                                  verbose_name='Тег',)

    cooking_time = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Время приготовления, мин'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент в рецепте',
        related_name='ingredients_in_recipe'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='recipes_ingredients_list'
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество в рецепте',
        default=1,
        validators=[MinValueValidator(1), ]
    )

    class Meta:
        verbose_name = 'Количество игредиентов в рецепте'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ingredient} в {self.recipe}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
    )

    class Meta:
        verbose_name = 'Избранный'
        verbose_name_plural = 'Избранные'
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique_favorites_recipes')
        ]

    def __str__(self):
        return (f'Пользователь: {self.user}, '
                f'избранные рецепты: {self.recipe.name}')


class ShoppingList(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_shopping_lists',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        related_name='purchases',
        on_delete=models.CASCADE,
        verbose_name='Покупка'
    )
    when_added = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата добавления'
    )

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Список покупок'

    def __str__(self):
        return f'Пользователь: {self.user}, покупает:{self.recipe}'
