from django.test import TestCase

from playground.items.models import Item


# Create your tests here.


class TestItem(TestCase):
    def test_create_item(self):
        i = Item.objects.create(name="foo")
        assert i.name == "foo"
        self.assertIn("Item (id=", str(i))
