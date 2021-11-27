"""Metric (SI) prefixes.
"""
import math
from typing import Optional

class Units:
    """Provides an interface to metric prefixes.

    See https://en.wikipedia.org/wiki/Metric_prefix#List_of_SI_prefixes

    Adapted from https://stackoverflow.com/a/20427577

    Args:
        overrides (Optional[dict]): Manual overrides.
            Might be helpful for disabling certain prefixes.
            For example, overrides={1:{'multiplier':1e-0,'prefix':''}}

    Returns:

    Raises:
    """
    def __init__(self,overrides:Optional[dict]=None) -> None:
        """
        """
        self.si = {-24: {'multiplier': 1e-24, 'prefix': 'y'},
                   -23: {'multiplier': 1e-24, 'prefix': 'y'},
                   -22: {'multiplier': 1e-24, 'prefix': 'y'},
                   -21: {'multiplier': 1e-21, 'prefix': 'z'},
                   -20: {'multiplier': 1e-21, 'prefix': 'z'},
                   -19: {'multiplier': 1e-21, 'prefix': 'z'},
                   -18: {'multiplier': 1e-18, 'prefix': 'a'},
                   -17: {'multiplier': 1e-18, 'prefix': 'a'},
                   -16: {'multiplier': 1e-18, 'prefix': 'a'},
                   -15: {'multiplier': 1e-15, 'prefix': 'f'},
                   -14: {'multiplier': 1e-15, 'prefix': 'f'},
                   -13: {'multiplier': 1e-15, 'prefix': 'f'},
                   -12: {'multiplier': 1e-12, 'prefix': 'p'},
                   -11: {'multiplier': 1e-12, 'prefix': 'p'},
                   -10: {'multiplier': 1e-12, 'prefix': 'p'},
                   -9: {'multiplier': 1e-9, 'prefix': 'n'},
                   -8: {'multiplier': 1e-9, 'prefix': 'n'},
                   -7: {'multiplier': 1e-9, 'prefix': 'n'},
                   -6: {'multiplier': 1e-6, 'prefix': 'u'},
                   -5: {'multiplier': 1e-6, 'prefix': 'u'},
                   -4: {'multiplier': 1e-6, 'prefix': 'u'},
                   -3: {'multiplier': 1e-3, 'prefix': 'm'},
                   -2: {'multiplier': 1e-2, 'prefix': 'c'},
                   -1: {'multiplier': 1e-1, 'prefix': 'd'},
                    0: {'multiplier': 1e0, 'prefix': ''},
                    1: {'multiplier': 1e1, 'prefix': 'da'},
                    2: {'multiplier': 1e2, 'prefix': 'h'},
                    3: {'multiplier': 1e3, 'prefix': 'k'},
                    4: {'multiplier': 1e3, 'prefix': 'k'},
                    5: {'multiplier': 1e3, 'prefix': 'k'},
                    6: {'multiplier': 1e6, 'prefix': 'M'},
                    7: {'multiplier': 1e6, 'prefix': 'M'},
                    8: {'multiplier': 1e6, 'prefix': 'M'},
                    9: {'multiplier': 1e9, 'prefix': 'G'},
                   10: {'multiplier': 1e9, 'prefix': 'G'},
                   11: {'multiplier': 1e9, 'prefix': 'G'},
                   12: {'multiplier': 1e12, 'prefix': 'T'},
                   13: {'multiplier': 1e12, 'prefix': 'T'},
                   14: {'multiplier': 1e12, 'prefix': 'T'},
                   15: {'multiplier': 1e15, 'prefix': 'P'},
                   16: {'multiplier': 1e15, 'prefix': 'P'},
                   17: {'multiplier': 1e15, 'prefix': 'P'},
                   18: {'multiplier': 1e18, 'prefix': 'E'},
                   19: {'multiplier': 1e18, 'prefix': 'E'},
                   20: {'multiplier': 1e18, 'prefix': 'E'},
                   21: {'multiplier': 1e21, 'prefix': 'Z'},
                   22: {'multiplier': 1e21, 'prefix': 'Z'},
                   23: {'multiplier': 1e21, 'prefix': 'Z'},
                   24: {'multiplier': 1e24, 'prefix': 'Y'},
                   25: {'multiplier': 1e24, 'prefix': 'Y'},
                   26: {'multiplier': 1e24, 'prefix': 'Y'}}

        if overrides is not None:
            for override in overrides:
                self.si[override] = overrides[override]

    def convert(self,number:float) -> tuple[int,str]:
        """Returns multiplier and prefix.

        Args:
            number (float): Metric (SI) prefixes.

        Returns:
            tuple[int,str]: Multiplier and prefix.

        Raises:
        """
        exponent = math.floor(math.log10(abs(number)))

        if exponent < min(self.si.keys()):
            exponent = min(self.si.keys())
        elif exponent > max(self.si.keys()):
            exponent = max(self.si.keys())
        return (number/self.si[exponent]['multiplier'],
                self.si[exponent]['prefix'])
