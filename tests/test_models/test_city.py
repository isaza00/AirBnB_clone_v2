#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        state = State(name="Arizona")
        new = self.value(state_id=state.id)
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value(name="San Francisco")
        self.assertEqual(type(new.name), str)

    def test_any1(self):
        """Test"""
        pass

    def test_any2(self):
        """Test"""
        pass

    def test_any3(self):
        """Test"""
        pass
