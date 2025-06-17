from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from .models import MenuItem, Booking

class MenuItemTest(TestCase):
    def test_create_item(self):
        item = MenuItem.objects.create(name="Pizza", price=9.99, description="Cheesy")
        self.assertEqual(item.name, "Pizza")

class BookingTest(TestCase):
    def test_create_booking(self):
        user = User.objects.create_user(username='john', password='pass')
        booking = Booking.objects.create(user=user, date='2025-01-01', time='18:00', guests=2)
        self.assertEqual(booking.guests, 2)
