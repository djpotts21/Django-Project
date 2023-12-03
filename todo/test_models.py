from django.test import TestCase
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d71dbfc (Initialise for Heroku)
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
<<<<<<< HEAD
<<<<<<< HEAD
        self.assertEqual(str(item), 'Test Todo Item')
=======


>>>>>>> 6e6f3ff (Build Test Views and Models)
=======
        self.assertEqual(str(item), 'Test Todo Item')
>>>>>>> 9fb4afc (Updated test models and views to get 100% coverage)
=======
        self.assertEqual(str(item), 'Test Todo Item')
>>>>>>> d71dbfc (Initialise for Heroku)
