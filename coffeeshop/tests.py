from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Coffee, Review

# Create your tests here.

class CoffeeshopTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()
        test_coffee = Coffee.objects.create(
            author=testuser1, name='test coffee', producer='test producer', origin='test origin', package=1)
        test_coffee.save()

        test_review = Review.objects.create(
            coffee=test_coffee, author = testuser1, review='test review', rating=1)
        test_review.save()

    def test_coffee_content(self):
        coffee = Coffee.objects.get(id=1)
        author = f'{coffee.author}'
        name = f'{coffee.name}'
        producer = f'{coffee.producer}'
        origin = f'{coffee.origin}'
        package = coffee.package
        self.assertEqual(author, 'testuser1')
        self.assertEqual(name, 'test coffee')
        self.assertEqual(producer, 'test producer')
        self.assertEqual(origin, 'test origin')
        self.assertEqual(package, 1)


    def test_review_content(self):
        review = Review.objects.get(id=1)
        coffee = f'{review.coffee}'
        author = f'{review.author}'
        rating = review.rating
        review_text = f'{review.review}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(coffee, 'test coffee')
        self.assertEqual(review_text, 'test review')
        self.assertEqual(rating, 1)

    def test_coffee_list_view(self):
        response = self.client.get('')
        # response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coffeeshop/coffee_list.html')

    def test_coffee_detail_view(self):
        response = self.client.get('/1/')
        no_response = self.client.get('/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test coffee')
        self.assertTemplateUsed(response, 'coffeeshop/coffee_detail.html')
    