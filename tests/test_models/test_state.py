#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value(name="California")
        self.assertEqual(type(new.name), str)

    def test_name(self):
        """Test"""
        new = State(name="California")
        self.assertEqual(new.name, "California")

    def test_any2(self):
        """Test"""
        pass

    def test_any3(self):
        """Test"""
        pass
