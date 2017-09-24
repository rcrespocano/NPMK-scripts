# -*- coding: utf-8 -*-
"""Multi-electrode-array (MEA) utilities."""

index_relationship = {1: 90,
                      2: 91,
                      3: 92,
                      4: 93,
                      5: 94,
                      6: 95,
                      7: 96,
                      8: 97,
                      9: 98,
                      10: 99,
                      11: 80,
                      12: 81,
                      13: 82,
                      14: 83,
                      15: 84,
                      16: 85,
                      17: 86,
                      18: 87,
                      19: 88,
                      20: 89,
                      21: 70,
                      22: 71,
                      23: 72,
                      24: 73,
                      25: 74,
                      26: 75,
                      27: 76,
                      28: 77,
                      29: 78,
                      30: 79,
                      31: 60,
                      32: 61,
                      33: 62,
                      34: 63,
                      35: 64,
                      36: 65,
                      37: 66,
                      38: 67,
                      39: 68,
                      40: 69,
                      41: 50,
                      42: 51,
                      43: 52,
                      44: 53,
                      45: 54,
                      46: 55,
                      47: 56,
                      48: 57,
                      49: 58,
                      50: 59,
                      51: 40,
                      52: 41,
                      53: 42,
                      54: 43,
                      55: 44,
                      56: 45,
                      57: 46,
                      58: 47,
                      59: 48,
                      60: 49,
                      61: 30,
                      62: 31,
                      63: 32,
                      64: 33,
                      65: 34,
                      66: 35,
                      67: 36,
                      68: 37,
                      69: 38,
                      70: 39,
                      71: 20,
                      72: 21,
                      73: 22,
                      74: 23,
                      75: 24,
                      76: 25,
                      77: 26,
                      78: 27,
                      79: 28,
                      80: 29,
                      81: 10,
                      82: 11,
                      83: 12,
                      84: 13,
                      85: 14,
                      86: 15,
                      87: 16,
                      88: 17,
                      89: 18,
                      90: 19,
                      91: 0,
                      92: 1,
                      93: 2,
                      94: 3,
                      95: 4,
                      96: 5,
                      97: 6,
                      98: 7,
                      99: 8,
                      100: 9, }


def get_soft_index_from_mea_index(index):
    return index_relationship.get(index, 0)