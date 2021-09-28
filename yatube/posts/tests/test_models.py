from django.contrib.auth import get_user_model
from django.test import TestCase
from ..models import Group, Post, Comment, Follow

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
        self.assertEqual(verbose_text, 'Текст поста')
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


class CommentModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовая группа',
        )
        cls.comment = Comment.objects.create(
            post=cls.post,
            text='text',
            author=cls.user
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        comment = CommentModelTest.comment
        comment_text = comment.text[:15]
        self.assertEqual(comment_text, str(comment))

    def test_verbose_name(self):
        """verbose_name поля text совпадает с ожидаемым."""
        comment = CommentModelTest.comment
        verbose_text = comment._meta.get_field('text').verbose_name
        self.assertEqual(verbose_text, 'Текст комментария')

    def test_help_text(self):
        """help_text поля text совпадает с ожидаемым."""
        comment = CommentModelTest.comment
        help_text_text = comment._meta.get_field('text').help_text
        self.assertEqual(help_text_text, 'Добавьте комментарий')


class FollowModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.username = User.objects.create_user(username='auth')
        cls.author = User.objects.create_user(username='author')
        cls.follow = Follow.objects.create(
            author=cls.username,
            user=cls.author
        )

    def test_verbose_name(self):
        """verbose_name поля text и user совпадает с ожидаемым."""
        follow = FollowModelTest.follow
        verbose_author = follow._meta.get_field('author').verbose_name
        self.assertEqual(verbose_author, 'Автор')
        follow = FollowModelTest.follow
        verbose_user = follow._meta.get_field('user').verbose_name
        self.assertEqual(verbose_user, 'Фолловер')

    def test_help_text(self):
        """help_text поля text и user совпадает с ожидаемым."""
        follow = FollowModelTest.follow
        help_text_author = follow._meta.get_field('author').help_text
        self.assertEqual(help_text_author, 'Подпишитесь на меня')
        follow = FollowModelTest.follow
        help_text_user = follow._meta.get_field('user').help_text
        self.assertEqual(help_text_user, 'Подпишитесь на автора')
