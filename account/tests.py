from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CustomUser, CustomUserRating

class CustomUserModelTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='adminuser',
            email='admin@example.com',
            password='adminpassword'
        )
        self.assertEqual(admin_user.username, 'adminuser')
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class CustomUserRatingModelTest(TestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create_user(username='user1', password='testpass1')
        self.user2 = CustomUser.objects.create_user(username='user2', password='testpass2')

    def test_create_custom_user_rating(self):
        rating = CustomUserRating.objects.create(user=self.user1, rated_by=self.user2, rating=4)
        self.assertEqual(rating.user, self.user1)
        self.assertEqual(rating.rated_by, self.user2)
        self.assertEqual(rating.rating, 4)

    def test_unique_together_constraint(self):
        # Attempt to create duplicate CustomUserRating
        CustomUserRating.objects.create(user=self.user1, rated_by=self.user2, rating=4)
        with self.assertRaises(Exception):
            CustomUserRating.objects.create(user=self.user1, rated_by=self.user2, rating=5)
