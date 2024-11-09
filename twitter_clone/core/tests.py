from django.test import TestCase
from .models import User, Tweet
from factory import DjangoModelFactory
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = 'testuser'
    password = 'testpass'


class TweetFactory(DjangoModelFactory):
    class Meta:
        model = Tweet

    user = UserFactory()
    content = 'Teste de tweet'


class TweetTestCase(TestCase):
    def test_tweet_creation(self):
        tweet = TweetFactory()
        self.assertEqual(tweet.content, 'Teste de tweet')

