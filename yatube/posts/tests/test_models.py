from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовая группа',
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        post = PostModelTest.post
        post_text = post.text[:15]
        self.assertEqual(post_text, str(post))

    def test_verbose_name(self):
        """verbose_name поля text и author совпадает с ожидаемым."""
        post = PostModelTest.post
        verbose_text = post._meta.get_field('text').verbose_name
        verbose_author = post._meta.get_field('author').verbose_name
        self.assertEqual(verbose_text, 'Текст')
        self.assertEqual(verbose_author, 'Автор')

    def test_help_text(self):
        """help_text поля text и author совпадает с ожидаемым."""
        post = PostModelTest.post
        help_text_text = post._meta.get_field('text').help_text
        help_text_author = post._meta.get_field('author').help_text
        self.assertEqual(help_text_text, 'Введите текст поста')
        self.assertEqual(help_text_author, 'Введите имя автора')


class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        group = GroupModelTest.group
        group_title = group.title
        self.assertEqual(group_title, str(group))

    def test_verbose_name(self):
        """verbose_name поля text и author совпадает с ожидаемым."""
        group = GroupModelTest.group
        verbose_title = group._meta.get_field('title').verbose_name
        verbose_slug = group._meta.get_field('slug').verbose_name
        verbose_description = group._meta.get_field('description').verbose_name
        self.assertEqual(verbose_title, 'Имя')
        self.assertEqual(verbose_slug, 'Адрес')
        self.assertEqual(verbose_description, 'Описание')

    def test_help_text(self):
        """help_text поля text и author совпадает с ожидаемым."""
        group = GroupModelTest.group
        help_text_title = group._meta.get_field('title').help_text
        help_text_slug = group._meta.get_field('slug').help_text
        help_text_description = group._meta.get_field('description').help_text
        self.assertEqual(help_text_title, 'Введите имя сообщества')
        self.assertEqual(help_text_slug, 'Введите адрес')
        self.assertEqual(help_text_description, 'Описание сообщества')
