import unittest
from unittest.mock import MagicMock
from colorchanger import colorchanger


class MyTestCase(unittest.TestCase):

    @staticmethod
    def test_set_hue_color():
        # Given
        hue_light_id = 1
        rgb_color = (0, 255, 0)
        colorchanger.hue_bridge.set_light = MagicMock(return_value=None)
        xy = colorchanger.converter.rgb_to_xy(0, 255, 0)

        # When
        colorchanger.set_hue_color(hue_light_id, rgb_color)

        # Then
        colorchanger.hue_bridge.set_light.assert_called_with(hue_light_id, 'xy', xy)


if __name__ == '__main__':
    unittest.main()
