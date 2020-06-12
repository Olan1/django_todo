from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):
    
    
    def test_item_name_is_required(self):
        # Test if empty name field in form is valid
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        # When form is invalid, it sends back dict of fields
        # on which errors + associated error messages appear.
        # Test to see if 'name' key appears in this dict
        self.assertIn('name', form.errors.keys())
        # Test if error message is correct
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        
        
    def test_done_field_is_not_required(self):
        # Create form only filling in the name field.
        # This should be valid since only the name field is required
        form = ItemForm({'name':'Test Todo Item'})
        self.assertTrue(form.is_valid())
        
    
    # Test that the only fields displayed in the form are the name and done fields
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
        
