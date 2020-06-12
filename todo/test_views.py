from django.test import TestCase
from .models import Item

# Create your tests here.


class TestViews(TestCase):
    
    # Test get todo list
    def test_get_todo_list(self):
        # Built in HTTP client from Django to test HTTP responses
        # Test homepage http response
        response = self.client.get('/')
        # 200 is a successful http response
        self.assertEqual(response.status_code, 200)
        # Check view renders correct template
        self.assertTemplateUsed(response, 'todo/todo_list.html')
        
    # Test get add item page
    def test_get_add_item_page(self):
        # Built in HTTP client from Django to test HTTP responses
        # Test http response
        response = self.client.get('/add')
        # 200 is a successful http response
        self.assertEqual(response.status_code, 200)
        # Check view renders correct template
        self.assertTemplateUsed(response, 'todo/add_item.html')
        
    # # Test get edit item page
    def test_get_edit_item_page(self):
        # Create Item instance
        item = Item.objects.create(name='Test Todo Item')
        # Built in HTTP client from Django to test HTTP responses
        # Test http response passing the Item instance id into URL
        response = self.client.get(f'/edit/{item.id}')
        # 200 is a successful http response
        self.assertEqual(response.status_code, 200)
        # Check view renders correct template
        self.assertTemplateUsed(response, 'todo/edit_item.html')
        
        
    # # Test if can add item
    def test_can_add_item(self):
        # Create Item can be created by posting to the add url
        response = self.client.post('/add', {'name':'Test Add Item'})
        # Test site redirects to homepage once item is added
        self.assertRedirects(response, '/')
        
        
    # # Test if can delete item
    def test_can_delete_item(self):
        # Create instance of Item
        item = Item.objects.create(name='Test Todo Item')
        # Test item delete url
        response = self.client.get(f'/delete/{item.id}')
        # Test site redirects to homepage
        self.assertRedirects(response, '/')
        # Check if item is still in DB
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)
        
        
    # # Test if can toggle item
    def test_can_toggle_item(self):
        # Create instance of Item
        item = Item.objects.create(name='Test Todo Item', done='True')
        # Test item delete url
        response = self.client.get(f'/toggle/{item.id}')
        # Test site redirects to homepage
        self.assertRedirects(response, '/')
        # Test toggle now = False
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
        
        
    def test_can_edit_item(self):
        # Create Item instance
        item = Item.objects.create(name='Test Todo Item', done=True)
        # Test POST response when updating item in DB
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        # Test redirects to homepage
        self.assertRedirects(response, '/')
        # Get updated item name
        updated_item = Item.objects.get(id=item.id)
        # Check name in DB = updated name
        self.assertEqual(updated_item.name, 'Updated Name')