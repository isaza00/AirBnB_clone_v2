#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models.user import User
from models.place import Place


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        place = Place()
        new = self.value(place_id=place.id)
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        user = User()
        new = self.value(user_id=user.id)
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value(text="bad place")
        self.assertEqual(type(new.text), str)
