from django.test import TestCase, Client
from django.contrib.auth.models import User
from restaurant import views
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(id=8,title="Panacota", price=77, inventory=100)
    
   
    def test_getall(self):
        user = User.objects.create_user(username='newuser', password='mypassword')
        client = Client()
        client.force_login(user)
        response = client.get("http://127.0.0.1:8000/restaurant/menu/")
        serialized_menus = 200
        self.assertEqual(response.status_code, serialized_menus)

