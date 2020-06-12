from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModels(TestCase):
    
    
    def test_done_defaults_to_false(self):
        # Create instance of Item to test
        item = Item.objects.create(name='Test Todo Item')
        # Test Item instance done field defaults to False
        self.assertFalse(item.done)
        
        
    def test_items_str_method_returns_name(self):
        item = Item.objects.create(name = 'Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
