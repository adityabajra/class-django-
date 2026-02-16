from django.test import TestCase
from .utils import add
from django.urls import reverse

class AddFunctionTestCase(TestCase):
    def test_add(self): 
        # method test batai suru huna parxa name

        self.assertEqual(add(2, 3), 5) # assertEqual chai expected result ra actual result compare garna use hunxa
        
# Create your tests here.

class RegistrationFormPageTestCase(TestCase):
    def test_registration_contains_input_text(self):
        response = self.client.get(reverse('registration:form')) # reverse function le url name lai url ma convert garxa
        self.assertEqual(response.status_code, 200) # status code 200 chai page load bhayo ki bhayena bhanne kura check garna use hunxa
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Password:')
