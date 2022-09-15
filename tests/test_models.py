from django.contrib.auth.models import User
from django.test import TestCase

from property.models import Complaint, Flat, Owner

USERNAME = 'Test_username'
FULL_NAME = 'Test Name'
PHONENUMBER = '+79999452343'
PRICE = 10000000
TOWN = 'Щельяюр'
ADDRESS = 'ул. Просвещения, д. 38'
FLOOR = 2
ROOMS_NUMBER = 3
HAS_BALCONY = True
ACTIVE = True
CONSTRUCTION_YEAR = 2005
TEXT_COMPLAINT = 'Текст для теста'


class TestPropertyModel(TestCase):
    """
    Создаем фикстуры Квартиры, Жалобы и Владельца.
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username=USERNAME)
        cls.flat = Flat.objects.create(
            owner=FULL_NAME,
            owners_phonenumber=PHONENUMBER,
            price=PRICE,
            town=TOWN,
            address=ADDRESS,
            floor=FLOOR,
            rooms_number=ROOMS_NUMBER,
            has_balcony=HAS_BALCONY,
            active=ACTIVE,
            construction_year=CONSTRUCTION_YEAR,
        )
        cls.flat.likes.add(cls.user)
        cls.complaint = Complaint.objects.create(
            author=cls.user,
            flat=cls.flat,
            text=TEXT_COMPLAINT,
        )
        cls.owner = Owner.objects.create(
            full_name=FULL_NAME,
            owners_phonenumber=PHONENUMBER,
        )
        cls.owner.flats.add(cls.flat)

    def test_flat_values(self):
        """
        Проверяем значения полей модели квартиры.
        """
        flat_fields_values = {
            'owner': FULL_NAME,
            'owners_phonenumber': PHONENUMBER,
            'price': PRICE,
            'town': TOWN,
            'address': ADDRESS,
            'floor': FLOOR,
            'rooms_number': ROOMS_NUMBER,
            'has_balcony': HAS_BALCONY,
            'active': ACTIVE,
            'construction_year': CONSTRUCTION_YEAR,
        }
        flat = TestPropertyModel.flat
        user = TestPropertyModel.user
        for field, expected_value in flat_fields_values.items():
            with self.subTest(field=field):
                self.assertEqual(
                    getattr(
                        flat,
                        field,
                    ),
                    expected_value,
                )
        self.assertIn(
            user,
            flat.likes.all(),
        )

    def test_owner_values(self):
        """
        Проверяем значения полей модели владельца.
        """
        owner = TestPropertyModel.owner
        flat = TestPropertyModel.flat
        self.assertEqual(
            owner.full_name,
            FULL_NAME,
        )
        self.assertEqual(
            owner.owners_phonenumber,
            PHONENUMBER
        )
        self.assertIn(
            flat,
            owner.flats.all(),
        )

    def test_complaint_values(self):
        """
        Проверяем значения полей модели жалобы.
        """
        user = TestPropertyModel.user
        complaint = TestPropertyModel.complaint
        flat = TestPropertyModel.flat
        complaint_fields_values = {
            'author': user,
            'flat': flat,
            'text': TEXT_COMPLAINT,
        }
        for field, excpected_value in complaint_fields_values.items():
            with self.subTest(field=field):
                self.assertEqual(
                    getattr(
                        complaint,
                        field,
                    ),
                    excpected_value,
                )
