from django.test import TestCase
import factory
from .models import User, Tweet
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = 'testuser'
    password = 'testpass'


class TweetFactory(DjangoModelFactory):
    class Meta:
        model = Tweet

    user = factory.SubFactory(UserFactory)
    content = 'Teste de tweet'


class TweetTestCase(TestCase):
    def test_tweet_creation(self):
        tweet = TweetFactory()
        self.assertEqual(tweet.content, 'Teste de tweet')
        self.assertIsNotNone(tweet.user)
