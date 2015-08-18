# -*- encoding: utf-8 -*-
from django.test import TestCase
from apps.hello.models import Person
from django.core.urlresolvers import reverse


class HomepageTest(TestCase):
    def setUp(self):
        Person.objects.create(first_name='victor',
                              last_name='yanukovych',
                              birth_date='1950-07-09',
                              con_email='still_legetimnіy@mail.ru',
                              con_jabbber='found_dead_or_alive@interpol.com',
                              con_skype='afraid_the_eggs',
                              bio="""
                              Place of birth : Yenakievo of Ukraine.
                              He studied at 'PTU Єnakіvsky gіrnichy tehnіkum'.
                              Time teaching: from 1966-09-01 to 1967-05-05.
                              Work in "Moscow psychiatric hospital № 1"
                              in position 'Legetimniy'.
                              Hobbies:
                              -licking golden loaf
                              -ride ostriches
                              -plunder the country
                              -stealing hats  """)

    def test_verifying_output_name(self):
        """Verifying the output Firstname, Lastname. Name should be displayed properly sensitive"""
        response = self.client.get(reverse('mainpage'))
        self.assertEqual(response.status_code, 200)
        page_str = response.content.decode('utf-8')
        self.assertTrue(page_str.find('Victor') != -1)
        self.assertTrue(page_str.find('Yanukovych') != -1)

    def test_verifying_output_other_comtacts(self):
        """
        Verifying the output 'Other contacts'.
        Block 'Other contacts' contacts should not be displayed if all fields are empty
        """
        response = self.client.get(reverse('mainpage'))
        self.assertEqual(response.status_code, 200)
        page_str = response.content.decode('utf-8')
        self.assertTrue(page_str.find('Other contacts') == -1)
