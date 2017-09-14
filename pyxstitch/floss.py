#!/usr/env/python
"""
DMC floss mapping.

Sourced from csv:
    https://github.com/adrianj/CrossStitchCreator
"""
import math


def _to_rgb_string(rgb):
    """Convert to rgb string."""
    return ('%02x%02x%02x' % rgb).lower()


class FlossException(Exception):
    """Floss exception."""


class FlossType(object):
    """Floss type."""

    def __init__(self, dmc):
        """Init the instance."""
        self.floss_number = dmc[0]
        self.name = dmc[1]
        self.rgb = _to_rgb_string(dmc[2])


class Floss(object):
    """Floss definitions."""

    def __init__(self):
        """Init the instance."""
        self._colors = {}
        self._cache = {}
        self._load()
        self._map = {}

    def _key_rgb(self, red, green, blue):
        """Create a cache key."""
        return "{}.{}.{}".format(red, green, blue)

    def _create_floss(self, dmc):
        """Create floss, handle any mappings."""
        floss_type = FlossType(dmc)
        if floss_type.rgb in self._map:
            floss_type = FlossType(self._map[floss_type.rgb])
        return floss_type

    def lookup(self, rgb):
        """Lookup a code."""
        rgb_str = self._key_rgb(rgb[0], rgb[1], rgb[2])
        if rgb_str in self._cache:
            return self._create_floss(self._cache[rgb_str])
        # try harder...
        close = None
        closest = -1
        for tries in self._colors.keys():
            t = self._colors[tries][2]
            check = self._close(rgb[0], rgb[1], rgb[2], t[0], t[1], t[2])
            if closest == -1 or check < closest:
                closest = check
                close = self._colors[tries]
        self._cache[rgb_str] = close
        return self._create_floss(close)

    def map(self, from_color, to_color):
        """Map one floss rgb to another."""
        if to_color in self._colors or to_color is None:
            if to_color is None:
                self._colors.pop(from_color, None)
            else:
                self._map[from_color] = self._colors[to_color]
            self._cache = {}
            return True
        raise FlossException("Unknown color(s): {} -> {}".format(from_color,
                                                                 to_color))

    def _close(self, r1, g1, b1, r2, g2, b2):
        """Closest rgb check."""
        return math.sqrt(pow((r1 - r2) * 0.299, 2) +
                         pow((g1 - g2) * 0.587, 2) +
                         pow((b1 - b2) * 0.114, 2))

    def _add(self, number, desc, red, green, blue, code, row):
        """Add a color."""
        rgb = (red, green, blue)
        self._colors[code.lower()] = (number, desc, rgb)

    def _load(self):
        """Load all colors."""
        self._add('3713',
                  'Salmon Very Light',
                  255,
                  226,
                  226,
                  'FFE2E2',
                  'row 01-01')

        self._add('761',
                  'Salmon Light',
                  255,
                  201,
                  201,
                  'FFC9C9',
                  'row 01-02')

        self._add('760',
                  'Salmon',
                  245,
                  173,
                  173,
                  'F5ADAD',
                  'row 01-03')

        self._add('3712',
                  'Salmon Medium',
                  241,
                  135,
                  135,
                  'F18787',
                  'row 01-04')

        self._add('3328',
                  'Salmon Dark',
                  227,
                  109,
                  109,
                  'E36D6D',
                  'row 01-05')

        self._add('347',
                  'Salmon Very Dark',
                  191,
                  45,
                  45,
                  'BF2D2D',
                  'row 01-06')

        self._add('353',
                  'Peach',
                  254,
                  215,
                  204,
                  'FED7CC',
                  'row 01-07')

        self._add('352',
                  'Coral Light',
                  253,
                  156,
                  151,
                  'FD9C97',
                  'row 01-08')

        self._add('351',
                  'Coral',
                  233,
                  106,
                  103,
                  'E96A67',
                  'row 01-09')

        self._add('350',
                  'Coral Medium',
                  224,
                  72,
                  72,
                  'E04848',
                  'row 01-10')

        self._add('349',
                  'Coral Dark',
                  210,
                  16,
                  53,
                  'D21035',
                  'row 01-11')

        self._add('817',
                  'Coral Red Very Dark',
                  187,
                  5,
                  31,
                  'BB051F',
                  'row 01-12')

        self._add('3708',
                  'Melon Light',
                  255,
                  203,
                  213,
                  'FFCBD5',
                  'row 01-13')

        self._add('3706',
                  'Melon Medium',
                  255,
                  173,
                  188,
                  'FFADBC',
                  'row 01-14')

        self._add('3705',
                  'Melon Dark',
                  255,
                  121,
                  146,
                  'FF7992',
                  'row 01-15')

        self._add('3801',
                  'Melon Very Dark',
                  231,
                  73,
                  103,
                  'E74967',
                  'row 01-16')

        self._add('666',
                  'Bright Red',
                  227,
                  29,
                  66,
                  'E31D42',
                  'row 01-17')

        self._add('321',
                  'Red',
                  199,
                  43,
                  59,
                  'C72B3B',
                  'row 01-18')

        self._add('304',
                  'Red Medium',
                  183,
                  31,
                  51,
                  'B71F33',
                  'row 01-19')

        self._add('498',
                  'Red Dark',
                  167,
                  19,
                  43,
                  'A7132B',
                  'row 01-20')

        self._add('816',
                  'Garnet',
                  151,
                  11,
                  35,
                  '970B23',
                  'row 01-21')

        self._add('815',
                  'Garnet Medium',
                  135,
                  7,
                  31,
                  '87071F',
                  'row 01-22')

        self._add('814',
                  'Garnet Dark',
                  123,
                  0,
                  27,
                  '7B001B',
                  'row 01-23')

        self._add('894',
                  'Carnation Very Light',
                  255,
                  178,
                  187,
                  'FFB2BB',
                  'row 02-01')

        self._add('893',
                  'Carnation Light',
                  252,
                  144,
                  162,
                  'FC90A2',
                  'row 02-02')

        self._add('892',
                  'Carnation Medium',
                  255,
                  121,
                  140,
                  'FF798C',
                  'row 02-03')

        self._add('891',
                  'Carnation Dark',
                  255,
                  87,
                  115,
                  'FF5773',
                  'row 02-04')

        self._add('818',
                  'Baby Pink',
                  255,
                  223,
                  217,
                  'FFDFD9',
                  'row 02-05')

        self._add('957',
                  'Geranium Pale',
                  253,
                  181,
                  181,
                  'FDB5B5',
                  'row 02-06')

        self._add('956',
                  'Geranium',
                  255,
                  145,
                  145,
                  'FF9191',
                  'row 02-07')

        self._add('309',
                  'Rose Dark',
                  86,
                  74,
                  74,
                  'BA4A4A',
                  'row 02-08')

        self._add('963',
                  'Dusty Rose Ult Vy Lt',
                  255,
                  215,
                  215,
                  'FFD7D7',
                  'row 02-09')

        self._add('3716',
                  'Dusty Rose Med Vy Lt',
                  255,
                  189,
                  189,
                  'FFBDBD',
                  'row 02-10')

        self._add('962',
                  'Dusty Rose Medium',
                  230,
                  138,
                  138,
                  'E68A8A',
                  'row 02-11')

        self._add('961',
                  'Dusty Rose Dark',
                  207,
                  115,
                  115,
                  'CF7373',
                  'row 02-12')

        self._add('3833',
                  'Raspberry Light',
                  234,
                  134,
                  153,
                  'EA8699',
                  'row 02-13')

        self._add('3832',
                  'Raspberry Medium',
                  219,
                  85,
                  110,
                  'DB556E',
                  'row 02-14')

        self._add('3831',
                  'Raspberry Dark',
                  179,
                  47,
                  72,
                  'B32F48',
                  'row 02-15')

        self._add('777',
                  'Raspberry Very Dark',
                  145,
                  53,
                  70,
                  '913546',
                  'row 02-16')

        self._add('819',
                  'Baby Pink Light',
                  255,
                  238,
                  235,
                  'FFEEEB',
                  'row 02-17')

        self._add('3326',
                  'Rose Light',
                  251,
                  173,
                  180,
                  'FBADB4',
                  'row 02-18')

        self._add('776',
                  'Pink Medium',
                  252,
                  176,
                  185,
                  'FCB0B9',
                  'row 02-19')

        self._add('899',
                  'Rose Medium',
                  242,
                  118,
                  136,
                  'F27688',
                  'row 02-20')

        self._add('335',
                  'Rose',
                  238,
                  84,
                  110,
                  'EE546E',
                  'row 02-21')

        self._add('326',
                  'Rose Very Dark',
                  179,
                  59,
                  75,
                  'B33B4B',
                  'row 02-22')

        self._add('151',
                  'Dusty Rose Vry Lt',
                  240,
                  206,
                  212,
                  'F0CED4',
                  'row 03-01')

        self._add('3354',
                  'Dusty Rose Light',
                  228,
                  166,
                  172,
                  'E4A6AC',
                  'row 03-02')

        self._add('3733',
                  'Dusty Rose',
                  232,
                  135,
                  155,
                  'E8879B',
                  'row 03-03')

        self._add('3731',
                  'Dusty Rose Very Dark',
                  218,
                  103,
                  131,
                  'DA6783',
                  'row 03-04')

        self._add('3350',
                  'Dusty Rose Ultra Dark',
                  188,
                  67,
                  101,
                  'BC4365',
                  'row 03-05')

        self._add('150',
                  'Dusty Rose Ult Vy Dk',
                  171,
                  2,
                  73,
                  'AB0249',
                  'row 03-06')

        self._add('3689',
                  'Mauve Light',
                  251,
                  191,
                  194,
                  'FBBFC2',
                  'row 03-07')

        self._add('3688',
                  'Mauve Medium',
                  231,
                  169,
                  172,
                  'E7A9AC',
                  'row 03-08')

        self._add('3687',
                  'Mauve',
                  201,
                  107,
                  112,
                  'C96B70',
                  'row 03-09')

        self._add('3803',
                  'Mauve Dark',
                  171,
                  51,
                  87,
                  'AB3357',
                  'row 03-10')

        self._add('3685',
                  'Mauve Very Dark',
                  136,
                  21,
                  49,
                  '881531',
                  'row 03-11')

        self._add('605',
                  'Cranberry Very Light',
                  255,
                  192,
                  205,
                  'FFC0CD',
                  'row 03-12')

        self._add('604',
                  'Cranberry Light',
                  255,
                  176,
                  190,
                  'FFB0BE',
                  'row 03-13')

        self._add('603',
                  'Cranberry',
                  255,
                  164,
                  190,
                  'FFA4BE',
                  'row 03-14')

        self._add('602',
                  'Cranberry Medium',
                  226,
                  72,
                  116,
                  'E24874',
                  'row 03-15')

        self._add('601',
                  'Cranberry Dark',
                  209,
                  40,
                  106,
                  'D1286A',
                  'row 03-16')

        self._add('600',
                  'Cranberry Very Dark',
                  205,
                  47,
                  99,
                  'CD2F63',
                  'row 03-17')

        self._add('3806',
                  'Cyclamen Pink Light',
                  255,
                  140,
                  174,
                  'FF8CAE',
                  'row 03-18')

        self._add('3805',
                  'Cyclamen Pink',
                  243,
                  71,
                  139,
                  'F3478B',
                  'row 03-19')

        self._add('3804',
                  'Cyclamen Pink Dark',
                  224,
                  40,
                  118,
                  'E02876',
                  'row 03-20')

        self._add('3609',
                  'Plum Ultra Light',
                  244,
                  174,
                  213,
                  'F4AED7',
                  'row 03-21')

        self._add('3608',
                  'Plum Very Light',
                  234,
                  156,
                  196,
                  'EA9CC4',
                  'row 03-22')

        self._add('3607',
                  'Plum Light',
                  197,
                  73,
                  137,
                  'C54989',
                  'row 03-23')

        self._add('718',
                  'Plum',
                  156,
                  36,
                  98,
                  '9C2462',
                  'row 03-24')

        self._add('917',
                  'Plum Medium',
                  155,
                  19,
                  89,
                  '9B1359',
                  'row 03-25')

        self._add('915',
                  'Plum Dark',
                  130,
                  0,
                  67,
                  '820043',
                  'row 03-26')

        self._add('225',
                  'Shell Pink Ult Vy Lt',
                  255,
                  223,
                  213,
                  'FFDFD7',
                  'row 04-01')

        self._add('224',
                  'Shell Pink Very Light',
                  235,
                  183,
                  175,
                  'EBB7AF',
                  'row 04-02')

        self._add('152',
                  'Shell Pink Med Light',
                  226,
                  160,
                  153,
                  'E2A099',
                  'row 04-03')

        self._add('223',
                  'Shell Pink Light',
                  204,
                  132,
                  124,
                  'CC847C',
                  'row 04-04')

        self._add('3722',
                  'Shell Pink Med',
                  188,
                  108,
                  100,
                  'BC6C64',
                  'row 04-05')

        self._add('3721',
                  'Shell Pink Dark',
                  161,
                  75,
                  81,
                  'A14B51',
                  'row 04-06')

        self._add('221',
                  'Shell Pink Vy Dk',
                  136,
                  62,
                  67,
                  '883E43',
                  'row 04-07')

        self._add('778',
                  'Antique Mauve Vy Lt',
                  223,
                  179,
                  187,
                  'DFB3BB',
                  'row 04-08')

        self._add('3727',
                  'Antique Mauve Light',
                  219,
                  169,
                  178,
                  'DBA9B2',
                  'row 04-09')

        self._add('316',
                  'Antique Mauve Med',
                  183,
                  115,
                  127,
                  'B7737F',
                  'row 04-10')

        self._add('3726',
                  'Antique Mauve Dark',
                  155,
                  91,
                  102,
                  '9B5B66',
                  'row 04-11')

        self._add('315',
                  'Antique Mauve Md Dk',
                  129,
                  73,
                  82,
                  '814952',
                  'row 04-12')

        self._add('3802',
                  'Antique Mauve Vy Dk',
                  113,
                  65,
                  73,
                  '714149',
                  'row 04-13')

        self._add('902',
                  'Garnet Very Dark',
                  130,
                  38,
                  55,
                  '822637',
                  'row 04-14')

        self._add('3743',
                  'Antique Violet Vy Lt',
                  215,
                  203,
                  211,
                  'D7CBD3',
                  'row 04-15')

        self._add('3042',
                  'Antique Violet Light',
                  183,
                  157,
                  167,
                  'B79DA7',
                  'row 04-16')

        self._add('3041',
                  'Antique Violet Medium',
                  149,
                  111,
                  124,
                  '956F7C',
                  'row 04-17')

        self._add('3740',
                  'Antique Violet Dark',
                  120,
                  87,
                  98,
                  '785762',
                  'row 04-18')

        self._add('3836',
                  'Grape Light',
                  186,
                  145,
                  170,
                  'BA91AA',
                  'row 04-19')

        self._add('3835',
                  'Grape Medium',
                  148,
                  96,
                  131,
                  '946083',
                  'row 04-20')

        self._add('3834',
                  'Grape Dark',
                  114,
                  55,
                  93,
                  '72375D',
                  'row 04-21')

        self._add('154',
                  'Grape Very Dark',
                  87,
                  36,
                  51,
                  '572433',
                  'row 04-22')

        self._add('211',
                  'Lavender Light',
                  227,
                  203,
                  227,
                  'E3CBE3',
                  'row 05-01')

        self._add('210',
                  'Lavender Medium',
                  195,
                  159,
                  195,
                  'D29FC3',
                  'row 05-02')

        self._add('209',
                  'Lavender Dark',
                  163,
                  123,
                  167,
                  'A37BA7',
                  'row 05-03')

        self._add('208',
                  'Lavender Very Dark',
                  131,
                  91,
                  139,
                  '835B8B',
                  'row 05-04')

        self._add('3837',
                  'Lavender Ultra Dark',
                  108,
                  58,
                  110,
                  '6C3A6E',
                  'row 05-05')

        self._add('327',
                  'Violet Dark',
                  99,
                  54,
                  102,
                  '633666',
                  'row 05-06')

        self._add('153',
                  'Violet Very Light',
                  230,
                  204,
                  217,
                  'E6CCD9',
                  'row 05-07')

        self._add('554',
                  'Violet Light',
                  219,
                  179,
                  203,
                  'DBB3CB',
                  'row 05-08')

        self._add('553',
                  'Violet',
                  163,
                  99,
                  139,
                  'A3638B',
                  'row 05-09')

        self._add('552',
                  'Violet  Medium',
                  128,
                  58,
                  107,
                  '803A6B',
                  'row 05-10')

        self._add('550',
                  'Violet Very Dark',
                  92,
                  24,
                  78,
                  '5C184E',
                  'row 05-11')

        self._add('3747',
                  'Blue Violet Vy Lt',
                  211,
                  215,
                  237,
                  'D3D7ED',
                  'row 05-12')

        self._add('341',
                  'Blue Violet Light',
                  183,
                  191,
                  221,
                  'B7BFDD',
                  'row 05-13')

        self._add('156',
                  'Blue Violet Med Lt',
                  163,
                  174,
                  209,
                  'A3AED1',
                  'row 05-14')

        self._add('340',
                  'Blue Violet Medium',
                  173,
                  167,
                  199,
                  'ADA7C7',
                  'row 05-15')

        self._add('155',
                  'Blue Violet Med Dark',
                  152,
                  145,
                  182,
                  '9891B6',
                  'row 05-16')

        self._add('3746',
                  'Blue Violet Dark',
                  119,
                  107,
                  152,
                  '776B98',
                  'row 05-17')

        self._add('333',
                  'Blue Violet Very Dark',
                  92,
                  84,
                  120,
                  '5C5478',
                  'row 05-18')

        self._add('157',
                  'Cornflower Blue Vy Lt',
                  187,
                  195,
                  217,
                  'BBC3D9',
                  'row 05-19')

        self._add('794',
                  'Cornflower Blue Light',
                  143,
                  156,
                  193,
                  '8F9CC1',
                  'row 05-20')

        self._add('793',
                  'Cornflower Blue Med',
                  112,
                  125,
                  162,
                  '707DA2',
                  'row 05-21')

        self._add('3807',
                  'Cornflower Blue',
                  96,
                  103,
                  140,
                  '60678C',
                  'row 05-22')

        self._add('792',
                  'Cornflower Blue Dark',
                  85,
                  91,
                  123,
                  '555B7B',
                  'row 05-23')

        self._add('158',
                  'Cornflower Blu M V D',
                  76,
                  82,
                  110,
                  '4C526E',
                  'row 05-24')

        self._add('791',
                  'Cornflower Blue V D',
                  70,
                  69,
                  99,
                  '464563',
                  'row 05-25')

        self._add('3840',
                  'Lavender Blue Light',
                  176,
                  192,
                  218,
                  'B0C0DA',
                  'row 06-01')

        self._add('3839',
                  'Lavender Blue Med',
                  123,
                  142,
                  171,
                  '7B8EAB',
                  'row 06-02')

        self._add('3838',
                  'Lavender Blue Dark',
                  92,
                  114,
                  148,
                  '5C7294',
                  'row 06-03')

        self._add('800',
                  'Delft Blue Pale',
                  192,
                  204,
                  222,
                  'C0CCDE',
                  'row 06-04')

        self._add('809',
                  'Delft Blue',
                  148,
                  168,
                  198,
                  '94A8C6',
                  'row 06-05')

        self._add('799',
                  'Delft Blue Medium',
                  116,
                  142,
                  182,
                  '748EB6',
                  'row 06-06')

        self._add('798',
                  'Delft Blue Dark',
                  70,
                  106,
                  142,
                  '466A8E',
                  'row 06-07')

        self._add('797',
                  'Royal Blue',
                  19,
                  71,
                  125,
                  '13477D',
                  'row 06-08')

        self._add('796',
                  'Royal Blue Dark',
                  17,
                  65,
                  109,
                  '11416D',
                  'row 06-09')

        self._add('820',
                  'Royal Blue Very Dark',
                  14,
                  54,
                  92,
                  '0E365C',
                  'row 06-10')

        self._add('162',
                  'Blue Ultra Very Light',
                  219,
                  236,
                  245,
                  'DBECF5',
                  'row 06-11')

        self._add('827',
                  'Blue Very Light',
                  189,
                  221,
                  237,
                  'BDDDED',
                  'row 06-12')

        self._add('813',
                  'Blue Light',
                  161,
                  194,
                  215,
                  'A1C2D7',
                  'row 06-13')

        self._add('826',
                  'Blue Medium',
                  107,
                  158,
                  191,
                  '6B9EBF',
                  'row 06-14')

        self._add('825',
                  'Blue Dark',
                  71,
                  129,
                  165,
                  '4781A5',
                  'row 06-15')

        self._add('824',
                  'Blue Very Dark',
                  57,
                  105,
                  135,
                  '396987',
                  'row 06-16')

        self._add('996',
                  'Electric Blue Medium',
                  48,
                  194,
                  236,
                  '30C2EC',
                  'row 06-17')

        self._add('3843',
                  'Electric Blue',
                  20,
                  170,
                  208,
                  '14AAD0',
                  'row 06-18')

        self._add('995',
                  'Electric Blue Dark',
                  38,
                  150,
                  182,
                  '2696B6',
                  'row 06-19')

        self._add('3846',
                  'Turquoise Bright Light',
                  6,
                  227,
                  230,
                  '06E3E6',
                  'row 06-20')

        self._add('3845',
                  'Turquoise Bright Med',
                  4,
                  196,
                  202,
                  '04C4CA',
                  'row 06-21')

        self._add('3844',
                  'Turquoise Bright Dark',
                  18,
                  174,
                  186,
                  '12AEBA',
                  'row 06-22')

        self._add('159',
                  'Blue Gray Light',
                  199,
                  202,
                  215,
                  'C7CAD7',
                  'row 07-01')

        self._add('160',
                  'Blue Gray Medium',
                  153,
                  159,
                  183,
                  '999FB7',
                  'row 07-02')

        self._add('161',
                  'Blue Gray',
                  120,
                  128,
                  164,
                  '7880A4',
                  'row 07-03')

        self._add('3756',
                  'Baby Blue Ult Vy Lt',
                  238,
                  252,
                  252,
                  'EEFCFC',
                  'row 07-04')

        self._add('775',
                  'Baby Blue Very Light',
                  217,
                  235,
                  241,
                  'D9EBF1',
                  'row 07-05')

        self._add('3841',
                  'Baby Blue Pale',
                  205,
                  223,
                  237,
                  'CDDFED',
                  'row 07-06')

        self._add('3325',
                  'Baby Blue Light',
                  184,
                  210,
                  230,
                  'B8D2E6',
                  'row 07-07')

        self._add('3755',
                  'Baby Blue',
                  147,
                  180,
                  206,
                  '92B4CE',
                  'row 07-08')

        self._add('334',
                  'Baby Blue Medium',
                  115,
                  159,
                  193,
                  '739FC1',
                  'row 07-09')

        self._add('322',
                  'Baby Blue Dark',
                  90,
                  143,
                  184,
                  '5A8FB8',
                  'row 07-10')

        self._add('312',
                  'Baby Blue Very Dark',
                  53,
                  102,
                  139,
                  '35668B',
                  'row 07-11')

        self._add('803',
                  'Baby Blue Ult Vy Dk',
                  44,
                  89,
                  124,
                  '2C597C',
                  'row 07-12')

        self._add('336',
                  'Navy Blue',
                  37,
                  59,
                  115,
                  '253B73',
                  'row 07-13')

        self._add('823',
                  'Navy Blue Dark',
                  33,
                  48,
                  99,
                  '213063',
                  'row 07-14')

        self._add('939',
                  'Navy Blue Very Dark',
                  27,
                  40,
                  83,
                  '1B2853',
                  'row 07-15')

        self._add('3753',
                  'Antique Blue Ult Vy Lt',
                  219,
                  226,
                  233,
                  'DBE2E9',
                  'row 07-16')

        self._add('3752',
                  'Antique Blue Very Lt',
                  199,
                  209,
                  219,
                  'C7D1DB',
                  'row 07-17')

        self._add('932',
                  'Antique Blue Light',
                  162,
                  181,
                  198,
                  'A2B5C6',
                  'row 07-18')

        self._add('931',
                  'Antique Blue Medium',
                  106,
                  133,
                  158,
                  '6A859E',
                  'row 07-19')

        self._add('930',
                  'Antique Blue Dark',
                  69,
                  92,
                  113,
                  '455C71',
                  'row 07-20')

        self._add('3750',
                  'Antique Blue Very Dk',
                  56,
                  76,
                  94,
                  '384C5E',
                  'row 07-21')

        self._add('828',
                  'Sky Blue Vy Lt',
                  197,
                  232,
                  237,
                  'C5E8ED',
                  'row 08-01')

        self._add('3761',
                  'Sky Blue Light',
                  172,
                  216,
                  226,
                  'ACD8E2',
                  'row 08-02')

        self._add('519',
                  'Sky Blue',
                  126,
                  177,
                  200,
                  '7EB1C8',
                  'row 08-03')

        self._add('518',
                  'Wedgewood Light',
                  79,
                  147,
                  167,
                  '4F93A7',
                  'row 08-04')

        self._add('3760',
                  'Wedgewood Med',
                  62,
                  133,
                  162,
                  '3E85A2',
                  'row 08-05')

        self._add('517',
                  'Wedgewood Dark',
                  59,
                  118,
                  143,
                  '3B768F',
                  'row 08-06')

        self._add('3842',
                  'Wedgewood Vry Dk',
                  50,
                  102,
                  124,
                  '32667C',
                  'row 08-07')

        self._add('311',
                  'Wedgewood Ult VyDk',
                  28,
                  80,
                  102,
                  '1C5066',
                  'row 08-08')

        self._add('747',
                  'Peacock Blue Vy Lt',
                  229,
                  252,
                  253,
                  'E5FCFD',
                  'row 08-09')

        self._add('3766',
                  'Peacock Blue Light',
                  153,
                  207,
                  217,
                  '99CFD9',
                  'row 08-10')

        self._add('807',
                  'Peacock Blue',
                  100,
                  171,
                  186,
                  '64ABBA',
                  'row 08-11')

        self._add('806',
                  'Peacock Blue Dark',
                  61,
                  149,
                  165,
                  '3D95A5',
                  'row 08-12')

        self._add('3765',
                  'Peacock Blue Vy Dk',
                  52,
                  127,
                  140,
                  '347F8C',
                  'row 08-13')

        self._add('3811',
                  'Turquoise Very Light',
                  188,
                  227,
                  230,
                  'BCE3E6',
                  'row 08-14')

        self._add('598',
                  'Turquoise Light',
                  144,
                  195,
                  204,
                  '90C3CC',
                  'row 08-15')

        self._add('597',
                  'Turquoise',
                  91,
                  163,
                  179,
                  '5BA3B3',
                  'row 08-16')

        self._add('3810',
                  'Turquoise Dark',
                  72,
                  142,
                  154,
                  '488E9A',
                  'row 08-17')

        self._add('3809',
                  'Turquoise Vy Dark',
                  63,
                  124,
                  133,
                  '3F7C85',
                  'row 08-18')

        self._add('3808',
                  'Turquoise Ult Vy Dk',
                  54,
                  105,
                  112,
                  '366970',
                  'row 08-19')

        self._add('928',
                  'Gray Green Vy Lt',
                  221,
                  227,
                  227,
                  'DDE3E3',
                  'row 08-20')

        self._add('927',
                  'Gray Green Light',
                  189,
                  203,
                  203,
                  'BDCBCB',
                  'row 08-21')

        self._add('926',
                  'Gray Green Med',
                  152,
                  174,
                  174,
                  '98AEAE',
                  'row 08-22')

        self._add('3768',
                  'Gray Green Dark',
                  101,
                  127,
                  127,
                  '657F7F',
                  'row 08-23')

        self._add('924',
                  'Gray Green Vy Dark',
                  86,
                  106,
                  106,
                  '566A6A',
                  'row 08-24')

        self._add('3849',
                  'Teal Green Light',
                  82,
                  179,
                  164,
                  '52B3AE',
                  'row 08-25')

        self._add('3848',
                  'Teal Green Med',
                  85,
                  147,
                  146,
                  '419392',
                  'row 08-26')

        self._add('3847',
                  'Teal Green Dark',
                  52,
                  125,
                  117,
                  '347D75',
                  'row 08-27')

        self._add('964',
                  'Sea Green Light',
                  169,
                  226,
                  216,
                  'A9E2D8',
                  'row 09-01')

        self._add('959',
                  'Sea Green Med',
                  89,
                  199,
                  180,
                  '59C7B4',
                  'row 09-02')

        self._add('958',
                  'Sea Green Dark',
                  62,
                  182,
                  161,
                  '3EB6A1',
                  'row 09-03')

        self._add('3812',
                  'Sea Green Vy Dk',
                  47,
                  140,
                  132,
                  '2F8C84',
                  'row 09-04')

        self._add('3851',
                  'Green Bright Lt',
                  73,
                  179,
                  161,
                  '49B3A1',
                  'row 09-05')

        self._add('943',
                  'Green Bright Md',
                  61,
                  147,
                  132,
                  '3D9384',
                  'row 09-06')

        self._add('3850',
                  'Green Bright Dk',
                  55,
                  132,
                  119,
                  '378477',
                  'row 09-07')

        self._add('993',
                  'Aquamarine Vy Lt',
                  144,
                  192,
                  180,
                  '90C0B4',
                  'row 09-08')

        self._add('992',
                  'Aquamarine Lt',
                  111,
                  174,
                  159,
                  '6FAE9F',
                  'row 09-09')

        self._add('3814',
                  'Aquamarine',
                  80,
                  139,
                  125,
                  '508B7D',
                  'row 09-10')

        self._add('991',
                  'Aquamarine Dk',
                  71,
                  123,
                  110,
                  '477B6E',
                  'row 09-11')

        self._add('966',
                  'Jade Ultra Vy Lt',
                  185,
                  215,
                  192,
                  'B9D7C0',
                  'row 09-12')

        self._add('564',
                  'Jade Very Light',
                  167,
                  205,
                  175,
                  'A7CDAF',
                  'row 09-13')

        self._add('563',
                  'Jade Light',
                  143,
                  192,
                  152,
                  '8FC098',
                  'row 09-14')

        self._add('562',
                  'Jade Medium',
                  83,
                  151,
                  106,
                  '53976A',
                  'row 09-15')

        self._add('505',
                  'Jade Green',
                  51,
                  131,
                  98,
                  '338362',
                  'row 09-16')

        self._add('3817',
                  'Celadon Green Lt',
                  153,
                  195,
                  170,
                  '99C3AA',
                  'row 09-17')

        self._add('3816',
                  'Celadon Green',
                  101,
                  165,
                  125,
                  '65A57D',
                  'row 09-18')

        self._add('163',
                  'Celadon Green Md',
                  77,
                  131,
                  97,
                  '4D8361',
                  'row 09-19')

        self._add('3815',
                  'Celadon Green Dk',
                  71,
                  119,
                  89,
                  '477759',
                  'row 09-20')

        self._add('561',
                  'Celadon Green VD',
                  44,
                  106,
                  69,
                  '2C6A45',
                  'row 09-21')

        self._add('504',
                  'Blue Green Vy Lt',
                  196,
                  222,
                  204,
                  'C4DECC',
                  'row 09-22')

        self._add('3813',
                  'Blue Green Lt',
                  178,
                  212,
                  189,
                  'B2D4BD',
                  'row 09-23')

        self._add('503',
                  'Blue Green Med',
                  123,
                  172,
                  148,
                  '7BAC94',
                  'row 09-24')

        self._add('502',
                  'Blue Green',
                  91,
                  144,
                  113,
                  '5B9071',
                  'row 09-25')

        self._add('501',
                  'Blue Green Dark',
                  57,
                  111,
                  82,
                  '396F52',
                  'row 09-26')

        self._add('500',
                  'Blue Green Vy Dk',
                  4,
                  77,
                  51,
                  '044D33',
                  'row 09-27')

        self._add('955',
                  'Nile Green Light',
                  162,
                  214,
                  173,
                  'A2D6AD',
                  'row 10-01')

        self._add('954',
                  'Nile Green',
                  136,
                  186,
                  145,
                  '88BA91',
                  'row 10-02')

        self._add('913',
                  'Nile Green Med',
                  109,
                  171,
                  119,
                  '6DAB77',
                  'row 10-03')

        self._add('912',
                  'Emerald Green Lt',
                  27,
                  157,
                  107,
                  '1B9D6B',
                  'row 10-04')

        self._add('911',
                  'Emerald Green Med',
                  24,
                  144,
                  101,
                  '189065',
                  'row 10-05')

        self._add('910',
                  'Emerald Green Dark',
                  24,
                  126,
                  86,
                  '187E58',
                  'row 10-06')

        self._add('909',
                  'Emerald Green Vy Dk',
                  21,
                  111,
                  73,
                  '156F49',
                  'row 10-07')

        self._add('3818',
                  'Emerald Grn Ult V Dk',
                  17,
                  90,
                  59,
                  '115A3B',
                  'row 10-08')

        self._add('369',
                  'Pistachio Green Vy Lt',
                  215,
                  237,
                  204,
                  'D7EDCC',
                  'row 10-09')

        self._add('368',
                  'Pistachio Green Lt',
                  166,
                  194,
                  152,
                  'A6C298',
                  'row 10-10')

        self._add('320',
                  'Pistachio Green Med',
                  105,
                  136,
                  90,
                  '69885A',
                  'row 10-11')

        self._add('367',
                  'Pistachio Green Dk',
                  97,
                  122,
                  82,
                  '617A52',
                  'row 10-12')

        self._add('319',
                  'Pistachio Grn Vy Dk',
                  32,
                  95,
                  46,
                  '205F2E',
                  'row 10-13')

        self._add('890',
                  'Pistachio Grn Ult V D',
                  23,
                  73,
                  35,
                  '184923',
                  'row 10-14')

        self._add('164',
                  'Forest Green Lt',
                  200,
                  216,
                  184,
                  'C8D8B8',
                  'row 10-15')

        self._add('989',
                  'Forest Green ',
                  141,
                  166,
                  117,
                  '8DA675',
                  'row 10-16')

        self._add('988',
                  'Forest Green Med',
                  115,
                  139,
                  91,
                  '738B5B',
                  'row 10-17')

        self._add('987',
                  'Forest Green Dk',
                  88,
                  113,
                  65,
                  '587141',
                  'row 10-18')

        self._add('986',
                  'Forest Green Vy Dk',
                  64,
                  82,
                  48,
                  '405230',
                  'row 10-19')

        self._add('772',
                  'Yellow Green Vy Lt',
                  228,
                  236,
                  212,
                  'E4ECD4',
                  'row 10-20')

        self._add('3348',
                  'Yellow Green Lt',
                  204,
                  217,
                  177,
                  'CCD9B1',
                  'row 10-21')

        self._add('3347',
                  'Yellow Green Med',
                  113,
                  147,
                  92,
                  '71935C',
                  'row 10-22')

        self._add('3346',
                  'Hunter Green',
                  64,
                  106,
                  58,
                  '406A3A',
                  'row 10-23')

        self._add('3345',
                  'Hunter Green Dk',
                  27,
                  89,
                  21,
                  '1B5915',
                  'row 10-24')

        self._add('895',
                  'Hunter Green Vy Dk',
                  27,
                  83,
                  0,
                  '1B5300',
                  'row 10-25')

        self._add('704',
                  'Chartreuse Bright',
                  158,
                  207,
                  52,
                  '9ECF34',
                  'row 11-01')

        self._add('703',
                  'Chartreuse',
                  123,
                  181,
                  71,
                  '7BB547',
                  'row 11-02')

        self._add('702',
                  'Kelly Green',
                  71,
                  167,
                  47,
                  '47A72F',
                  'row 11-03')

        self._add('701',
                  'Green Light',
                  63,
                  143,
                  41,
                  '3F8F29',
                  'row 11-04')

        self._add('700',
                  'Green Bright',
                  7,
                  115,
                  27,
                  '07731B',
                  'row 11-05')

        self._add('699',
                  'Green',
                  5,
                  101,
                  23,
                  '056517',
                  'row 11-06')

        self._add('907',
                  'Parrot Green Lt',
                  199,
                  230,
                  102,
                  'C7E666',
                  'row 11-07')

        self._add('906',
                  'Parrot Green Md',
                  127,
                  179,
                  53,
                  '7FB335',
                  'row 11-08')

        self._add('905',
                  'Parrot Green Dk',
                  98,
                  138,
                  40,
                  '628A28',
                  'row 11-09')

        self._add('904',
                  'Parrot Green V Dk',
                  85,
                  120,
                  34,
                  '557822',
                  'row 11-10')

        self._add('472',
                  'Avocado Grn U Lt',
                  216,
                  228,
                  152,
                  'D8E498',
                  'row 11-11')

        self._add('471',
                  'Avocado Grn V Lt',
                  174,
                  191,
                  121,
                  'AEBF79',
                  'row 11-12')

        self._add('470',
                  'Avocado Grn Lt',
                  148,
                  171,
                  79,
                  '94AB4F',
                  'row 11-13')

        self._add('469',
                  'Avocado Green',
                  114,
                  132,
                  60,
                  '72843C',
                  'row 11-14')

        self._add('937',
                  'Avocado Green Md',
                  98,
                  113,
                  51,
                  '627133',
                  'row 11-15')

        self._add('936',
                  'Avocado Grn V Dk',
                  76,
                  88,
                  38,
                  '4C5826',
                  'row 11-16')

        self._add('935',
                  'Avocado Green Dk',
                  66,
                  77,
                  33,
                  '424D21',
                  'row 11-17')

        self._add('934',
                  'Avocado Grn Black',
                  49,
                  57,
                  25,
                  '313919',
                  'row 11-18')

        self._add('523',
                  'Fern Green Lt',
                  171,
                  177,
                  151,
                  'ABB197',
                  'row 11-19')

        self._add('3053',
                  'Green Gray',
                  156,
                  164,
                  130,
                  '9CA482',
                  'row 11-20')

        self._add('3052',
                  'Green Gray Md',
                  136,
                  146,
                  104,
                  '889268',
                  'row 11-21')

        self._add('3051',
                  'Green Gray Dk',
                  95,
                  102,
                  72,
                  '5F6648',
                  'row 11-22')

        self._add('524',
                  'Fern Green Vy Lt',
                  196,
                  205,
                  172,
                  'C4CDAC',
                  'row 11-23')

        self._add('522',
                  'Fern Green',
                  150,
                  158,
                  126,
                  '969E7E',
                  'row 11-24')

        self._add('520',
                  'Fern Green Dark',
                  102,
                  109,
                  79,
                  '666D4F',
                  'row 11-25')

        self._add('3364',
                  'Pine Green',
                  131,
                  151,
                  95,
                  '83975F',
                  'row 12-01')

        self._add('3363',
                  'Pine Green Md',
                  114,
                  130,
                  86,
                  '728256',
                  'row 12-02')

        self._add('3362',
                  'Pine Green Dk',
                  94,
                  107,
                  71,
                  '5E6B47',
                  'row 12-03')

        self._add('165',
                  'Moss Green Vy Lt',
                  239,
                  244,
                  164,
                  'EFF4A4',
                  'row 12-04')

        self._add('3819',
                  'Moss Green Lt',
                  224,
                  232,
                  104,
                  'E0E868',
                  'row 12-05')

        self._add('166',
                  'Moss Green Md Lt',
                  192,
                  200,
                  64,
                  'C0C840',
                  'row 12-06')

        self._add('581',
                  'Moss Green',
                  167,
                  174,
                  56,
                  'A7AE38',
                  'row 12-07')

        self._add('580',
                  'Moss Green Dk',
                  136,
                  141,
                  51,
                  '888D33',
                  'row 12-08')

        self._add('734',
                  'Olive Green Lt',
                  199,
                  192,
                  119,
                  'C7C077',
                  'row 12-09')

        self._add('733',
                  'Olive Green Md',
                  188,
                  179,
                  76,
                  'BCB34C',
                  'row 12-10')

        self._add('732',
                  'Olive Green',
                  148,
                  140,
                  54,
                  '948C36',
                  'row 12-11')

        self._add('731',
                  'Olive Green Dk',
                  147,
                  139,
                  55,
                  '938B37',
                  'row 12-12')

        self._add('730',
                  'Olive Green V Dk',
                  130,
                  123,
                  48,
                  '827B30',
                  'row 12-13')

        self._add('3013',
                  'Khaki Green Lt',
                  185,
                  185,
                  130,
                  'B9B982',
                  'row 12-14')

        self._add('3012',
                  'Khaki Green Md',
                  166,
                  167,
                  93,
                  'A6A75D',
                  'row 12-15')

        self._add('3011',
                  'Khaki Green Dk',
                  137,
                  138,
                  88,
                  '898A58',
                  'row 12-16')

        self._add('372',
                  'Mustard Lt',
                  204,
                  183,
                  132,
                  'CCB784',
                  'row 12-17')

        self._add('371',
                  'Mustard',
                  191,
                  166,
                  113,
                  'BFA671',
                  'row 12-18')

        self._add('370',
                  'Mustard Medium',
                  184,
                  157,
                  100,
                  'B89D64',
                  'row 12-19')

        self._add('834',
                  'Golden Olive Vy Lt',
                  219,
                  190,
                  127,
                  'DBBE7F',
                  'row 12-20')

        self._add('833',
                  'Golden Olive Lt',
                  200,
                  171,
                  108,
                  'C8AB6C',
                  'row 12-21')

        self._add('832',
                  'Golden Olive',
                  189,
                  155,
                  81,
                  'BD9B51',
                  'row 12-22')

        self._add('831',
                  'Golden Olive Md',
                  170,
                  143,
                  86,
                  'AA8F56',
                  'row 12-23')

        self._add('830',
                  'Golden Olive Dk',
                  141,
                  120,
                  75,
                  '8D784B',
                  'row 12-24')

        self._add('829',
                  'Golden Olive Vy Dk',
                  126,
                  107,
                  66,
                  '7E6B42',
                  'row 12-25')

        self._add('613',
                  'Drab Brown V Lt',
                  220,
                  196,
                  170,
                  'DCC4AA',
                  'row 13-01')

        self._add('612',
                  'Drab Brown Lt',
                  188,
                  154,
                  120,
                  'BC9A78',
                  'row 13-02')

        self._add('611',
                  'Drab Brown',
                  150,
                  118,
                  86,
                  '967656',
                  'row 13-03')

        self._add('610',
                  'Drab Brown Dk',
                  121,
                  96,
                  71,
                  '796047',
                  'row 13-04')

        self._add('3047',
                  'Yellow Beige Lt',
                  231,
                  214,
                  193,
                  'E7D6C1',
                  'row 13-05')

        self._add('3046',
                  'Yellow Beige Md',
                  216,
                  188,
                  154,
                  'D8BC9A',
                  'row 13-06')

        self._add('3045',
                  'Yellow Beige Dk',
                  188,
                  150,
                  106,
                  'BC966A',
                  'row 13-07')

        self._add('167',
                  'Yellow Beige V Dk',
                  167,
                  124,
                  73,
                  'A77C49',
                  'row 13-08')

        self._add('746',
                  'Off White',
                  252,
                  252,
                  238,
                  'FCFCEE',
                  'row 13-09')

        self._add('677',
                  'Old Gold Vy Lt',
                  245,
                  236,
                  203,
                  'F5ECCB',
                  'row 13-10')

        self._add('422',
                  'Hazelnut Brown Lt',
                  198,
                  159,
                  123,
                  'C69F7B',
                  'row 13-11')

        self._add('3828',
                  'Hazelnut Brown',
                  183,
                  139,
                  97,
                  'B78B61',
                  'row 13-12')

        self._add('420',
                  'Hazelnut Brown Dk',
                  160,
                  112,
                  66,
                  'A07042',
                  'row 13-13')

        self._add('869',
                  'Hazelnut Brown V Dk',
                  131,
                  94,
                  57,
                  '835E41',
                  'row 13-14')

        self._add('728',
                  'Topaz',
                  228,
                  180,
                  104,
                  'E4B468',
                  'row 13-15')

        self._add('783',
                  'Topaz Medium',
                  206,
                  145,
                  36,
                  'CE9124',
                  'row 13-16')

        self._add('782',
                  'Topaz Dark',
                  174,
                  119,
                  32,
                  'AE7720',
                  'row 13-17')

        self._add('781',
                  'Topaz Very Dark',
                  162,
                  109,
                  32,
                  'A26D20',
                  'row 13-18')

        self._add('780',
                  'Topaz Ultra Vy Dk',
                  148,
                  99,
                  26,
                  '94631A',
                  'row 13-19')

        self._add('676',
                  'Old Gold Lt',
                  229,
                  206,
                  151,
                  'E5CE97',
                  'row 13-20')

        self._add('729',
                  'Old Gold Medium',
                  208,
                  165,
                  62,
                  'D0A53E',
                  'row 13-21')

        self._add('680',
                  'Old Gold Dark',
                  188,
                  141,
                  14,
                  'BC8D0E',
                  'row 13-22')

        self._add('3829',
                  'Old Gold Vy Dark',
                  169,
                  130,
                  4,
                  'A98204',
                  'row 13-23')

        self._add('3822',
                  'Straw Light',
                  246,
                  220,
                  152,
                  'F6DC98',
                  'row 13-24')

        self._add('3821',
                  'Straw',
                  243,
                  206,
                  117,
                  'F3CE75',
                  'row 13-25')

        self._add('3820',
                  'Straw Dark',
                  223,
                  182,
                  95,
                  'DFB65F',
                  'row 13-26')

        self._add('3852',
                  'Straw Very Dark',
                  205,
                  157,
                  55,
                  'CD9D37',
                  'row 13-27')

        self._add('445',
                  'Lemon Light',
                  255,
                  251,
                  139,
                  'FFFB8B',
                  'row 14-01')

        self._add('307',
                  'Lemon',
                  253,
                  237,
                  84,
                  'FDED54',
                  'row 14-02')

        self._add('973',
                  'Canary Bright',
                  255,
                  227,
                  0,
                  'FFE300',
                  'row 14-03')

        self._add('444',
                  'Lemon Dark',
                  255,
                  214,
                  0,
                  'FFD600',
                  'row 14-04')

        self._add('3078',
                  'Golden Yellow Vy Lt',
                  253,
                  249,
                  205,
                  'FDF9CD',
                  'row 14-05')

        self._add('727',
                  'Topaz Vy Lt',
                  255,
                  241,
                  175,
                  'FFF1AF',
                  'row 14-06')

        self._add('726',
                  'Topaz Light',
                  253,
                  215,
                  85,
                  'FDD755',
                  'row 14-07')

        self._add('725',
                  'Topaz Med Lt',
                  255,
                  200,
                  64,
                  'FFC840',
                  'row 14-08')

        self._add('972',
                  'Canary Deep',
                  255,
                  181,
                  21,
                  'FFB515',
                  'row 14-09')

        self._add('745',
                  'Yellow Pale Light',
                  255,
                  233,
                  173,
                  'FFE9AD',
                  'row 14-10')

        self._add('744',
                  'Yellow Pale',
                  255,
                  231,
                  147,
                  'FFE793',
                  'row 14-11')

        self._add('743',
                  'Yellow Med',
                  254,
                  211,
                  118,
                  'FED376',
                  'row 14-12')

        self._add('742',
                  'Tangerine Light',
                  255,
                  191,
                  87,
                  'FFBF57',
                  'row 14-13')

        self._add('741',
                  'Tangerine Med',
                  255,
                  163,
                  43,
                  'FFA32B',
                  'row 14-14')

        self._add('740',
                  'Tangerine',
                  255,
                  139,
                  0,
                  'FF8B00',
                  'row 14-15')

        self._add('970',
                  'Pumpkin Light',
                  247,
                  139,
                  19,
                  'F78B13',
                  'row 14-16')

        self._add('971',
                  'Pumpkin',
                  246,
                  127,
                  0,
                  'F67F00',
                  'row 14-17')

        self._add('947',
                  'Burnt Orange',
                  255,
                  123,
                  77,
                  'FF7B4D',
                  'row 14-18')

        self._add('946',
                  'Burnt Orange Med',
                  235,
                  99,
                  7,
                  'EB6307',
                  'row 14-19')

        self._add('900',
                  'Burnt Orange Dark',
                  209,
                  88,
                  7,
                  'D15807',
                  'row 14-20')

        self._add('967',
                  'Apricot Very Light',
                  255,
                  222,
                  213,
                  'FFDED5',
                  'row 14-21')

        self._add('3824',
                  'Apricot Light',
                  254,
                  205,
                  194,
                  'FECDC2',
                  'row 14-22')

        self._add('3341',
                  'Apricot',
                  252,
                  171,
                  152,
                  'FCAB98',
                  'row 14-23')

        self._add('3340',
                  'Apricot Med',
                  255,
                  131,
                  111,
                  'FF836F',
                  'row 14-24')

        self._add('608',
                  'Burnt Orange Bright',
                  253,
                  93,
                  53,
                  'FD5D35',
                  'row 14-25')

        self._add('606',
                  'Orange?Red Bright',
                  250,
                  50,
                  3,
                  'FA3203',
                  'row 14-26')

        self._add('951',
                  'Tawny Light',
                  255,
                  226,
                  207,
                  'FFE2CF',
                  'row 15-01')

        self._add('3856',
                  'Mahogany Ult Vy Lt',
                  255,
                  211,
                  181,
                  'FFD3B5',
                  'row 15-02')

        self._add('722',
                  'Orange Spice Light',
                  247,
                  151,
                  111,
                  'F7976F',
                  'row 15-03')

        self._add('721',
                  'Orange Spice Med',
                  242,
                  120,
                  66,
                  'F27842',
                  'row 15-04')

        self._add('720',
                  'Orange Spice Dark',
                  229,
                  92,
                  31,
                  'E55C1F',
                  'row 15-05')

        self._add('3825',
                  'Pumpkin Pale',
                  253,
                  189,
                  150,
                  'FDBD96',
                  'row 15-06')

        self._add('922',
                  'Copper Light',
                  226,
                  115,
                  35,
                  'E27323',
                  'row 15-07')

        self._add('921',
                  'Copper',
                  198,
                  98,
                  24,
                  'C66218',
                  'row 15-08')

        self._add('920',
                  'Copper Med',
                  172,
                  84,
                  20,
                  'AC5414',
                  'row 15-09')

        self._add('919',
                  'Red?Copper',
                  166,
                  69,
                  16,
                  'A64510',
                  'row 15-10')

        self._add('918',
                  'Red?Copper Dark',
                  130,
                  52,
                  10,
                  '82340A',
                  'row 15-11')

        self._add('3770',
                  'Tawny Vy Light',
                  255,
                  238,
                  227,
                  'FFEEE3',
                  'row 15-12')

        self._add('945',
                  'Tawny',
                  251,
                  213,
                  187,
                  'FBD5BB',
                  'row 15-13')

        self._add('402',
                  'Mahogany Vy Lt',
                  247,
                  167,
                  119,
                  'F7A777',
                  'row 15-14')

        self._add('3776',
                  'Mahogany Light',
                  207,
                  121,
                  57,
                  'CF7939',
                  'row 15-15')

        self._add('301',
                  'Mahogany Med',
                  179,
                  95,
                  43,
                  'B35F2B',
                  'row 15-16')

        self._add('400',
                  'Mahogany Dark',
                  143,
                  67,
                  15,
                  '8F430F',
                  'row 15-17')

        self._add('300',
                  'Mahogany Vy Dk',
                  111,
                  47,
                  0,
                  '6F2F00',
                  'row 15-18')

        self._add('3823',
                  'Yellow Ultra Pale',
                  255,
                  253,
                  227,
                  'FFFDE3',
                  'row 15-19')

        self._add('3855',
                  'Autumn Gold Lt',
                  250,
                  211,
                  150,
                  'FAD396',
                  'row 15-20')

        self._add('3854',
                  'Autumn Gold Med',
                  242,
                  175,
                  104,
                  'F2AF68',
                  'row 15-21')

        self._add('3853',
                  'Autumn Gold Dk',
                  242,
                  151,
                  70,
                  'F29746',
                  'row 15-22')

        self._add('3827',
                  'Golden Brown Pale',
                  247,
                  187,
                  119,
                  'F7BB77',
                  'row 16-01')

        self._add('977',
                  'Golden Brown Light',
                  220,
                  156,
                  86,
                  'DC9C56',
                  'row 16-02')

        self._add('976',
                  'Golden Brown Med',
                  194,
                  129,
                  66,
                  'C28142',
                  'row 16-03')

        self._add('3826',
                  'Golden Brown',
                  173,
                  114,
                  57,
                  'AD7239',
                  'row 16-04')

        self._add('975',
                  'Golden Brown Dk',
                  145,
                  79,
                  18,
                  '914F12',
                  'row 16-05')

        self._add('948',
                  'Peach Very Light',
                  254,
                  231,
                  218,
                  'FEE7DA',
                  'row 16-06')

        self._add('754',
                  'Peach Light',
                  247,
                  203,
                  191,
                  'F7CBBF',
                  'row 16-07')

        self._add('3771',
                  'Terra Cotta Ult Vy Lt',
                  244,
                  187,
                  169,
                  'F4BBA9',
                  'row 16-08')

        self._add('758',
                  'Terra Cotta Vy Lt',
                  238,
                  170,
                  155,
                  'EEAA9B',
                  'row 16-09')

        self._add('3778',
                  'Terra Cotta Light',
                  217,
                  137,
                  120,
                  'D98978',
                  'row 16-10')

        self._add('356',
                  'Terra Cotta Med',
                  197,
                  106,
                  91,
                  'C56A5B',
                  'row 16-11')

        self._add('3830',
                  'Terra Cotta',
                  185,
                  85,
                  68,
                  'BC5544',
                  'row 16-12')

        self._add('355',
                  'Terra Cotta Dark',
                  152,
                  68,
                  54,
                  '984436',
                  'row 16-13')

        self._add('3777',
                  'Terra Cotta Vy Dk',
                  134,
                  48,
                  34,
                  '863022',
                  'row 16-14')

        self._add('3779',
                  'Rosewood Ult Vy Lt',
                  248,
                  202,
                  200,
                  'F8CAC8',
                  'row 16-15')

        self._add('3859',
                  'Rosewood Light',
                  186,
                  139,
                  124,
                  'BA8B7C',
                  'row 16-16')

        self._add('3858',
                  'Rosewood Med',
                  150,
                  74,
                  63,
                  '964A3F',
                  'row 16-17')

        self._add('3857',
                  'Rosewood Dark',
                  104,
                  37,
                  26,
                  '68251A',
                  'row 16-18')

        self._add('3774',
                  'Desert Sand Vy Lt',
                  243,
                  225,
                  215,
                  'F3E1D7',
                  'row 16-19')

        self._add('950',
                  'Desert Sand Light',
                  238,
                  211,
                  196,
                  'EED3C4',
                  'row 16-20')

        self._add('3064',
                  'Desert Sand',
                  196,
                  142,
                  112,
                  'C48E70',
                  'row 16-21')

        self._add('407',
                  'Desert Sand Med',
                  187,
                  129,
                  97,
                  'BB8161',
                  'row 16-22')

        self._add('3773',
                  'Desert Sand Dark',
                  182,
                  117,
                  82,
                  'B67552',
                  'row 16-23')

        self._add('3772',
                  'Desert Sand Vy Dk',
                  160,
                  108,
                  80,
                  'A06C50',
                  'row 16-24')

        self._add('632',
                  'Desert Sand Ult Vy Dk',
                  135,
                  85,
                  57,
                  '875539',
                  'row 16-25')

        self._add('453',
                  'Shell Gray Light',
                  215,
                  206,
                  203,
                  'D7CECB',
                  'row 17-01')

        self._add('452',
                  'Shell Gray Med',
                  192,
                  179,
                  174,
                  'C0B3AE',
                  'row 17-02')

        self._add('451',
                  'Shell Gray Dark',
                  145,
                  123,
                  115,
                  '917B73',
                  'row 17-03')

        self._add('3861',
                  'Cocoa Light',
                  166,
                  136,
                  129,
                  'A68881',
                  'row 17-04')

        self._add('3860',
                  'Cocoa',
                  125,
                  93,
                  87,
                  '7D5D57',
                  'row 17-05')

        self._add('779',
                  'Cocoa Dark',
                  98,
                  75,
                  69,
                  '624B45',
                  'row 17-06')

        self._add('712',
                  'Cream',
                  255,
                  251,
                  239,
                  'FFFBEF',
                  'row 17-07')

        self._add('739',
                  'Tan Ult Vy Lt',
                  248,
                  228,
                  200,
                  'F8E4C8',
                  'row 17-08')

        self._add('738',
                  'Tan Very Light',
                  236,
                  204,
                  158,
                  'ECCC9E',
                  'row 17-09')

        self._add('437',
                  'Tan Light',
                  228,
                  187,
                  142,
                  'E4BB8E',
                  'row 17-10')

        self._add('436',
                  'Tan',
                  203,
                  144,
                  81,
                  'CB9051',
                  'row 17-11')

        self._add('435',
                  'Brown Very Light',
                  184,
                  119,
                  72,
                  'B87748',
                  'row 17-12')

        self._add('434',
                  'Brown Light',
                  152,
                  94,
                  51,
                  '985E35',
                  'row 17-13')

        self._add('433',
                  'Brown Med',
                  122,
                  69,
                  31,
                  '7A451F',
                  'row 17-14')

        self._add('801',
                  'Coffee Brown Dk',
                  101,
                  57,
                  25,
                  '653919',
                  'row 17-15')

        self._add('898',
                  'Coffee Brown Vy Dk',
                  73,
                  42,
                  19,
                  '492A13',
                  'row 17-16')

        self._add('938',
                  'Coffee Brown Ult Dk',
                  54,
                  31,
                  14,
                  '361F0E',
                  'row 17-17')

        self._add('3371',
                  'Black Brown',
                  30,
                  17,
                  8,
                  '1E1108',
                  'row 17-18')

        self._add('543',
                  'Beige Brown Ult Vy Lt',
                  242,
                  227,
                  206,
                  'F2E3CE',
                  'row 17-18')

        self._add('3864',
                  'Mocha Beige Light',
                  203,
                  182,
                  156,
                  'CBB69C',
                  'row 17-20')

        self._add('3863',
                  'Mocha Beige Med',
                  164,
                  131,
                  92,
                  'A4835C',
                  'row 17-21')

        self._add('3862',
                  'Mocha Beige Dark',
                  138,
                  110,
                  78,
                  '8A6E4E',
                  'row 17-22')

        self._add('3031',
                  'Mocha Brown Vy Dk',
                  75,
                  60,
                  42,
                  '4B3C2A',
                  'row 17-23')

        self._add('B5200',
                  'Snow White',
                  255,
                  255,
                  255,
                  'FFFFFF',
                  'row 18-01')

        self._add('White',
                  'White',
                  252,
                  251,
                  248,
                  'FCFBF8',
                  'row 18-02')

        self._add('3865',
                  'Winter White',
                  249,
                  247,
                  241,
                  'F9F7F1',
                  'row 18-03')

        self._add('Ecru',
                  'Ecru',
                  240,
                  234,
                  218,
                  'F0EADA',
                  'row 18-04')

        self._add('822',
                  'Beige Gray Light',
                  231,
                  226,
                  211,
                  'E7E2D3',
                  'row 18-05')

        self._add('644',
                  'Beige Gray Med',
                  221,
                  216,
                  203,
                  'DDD8CB',
                  'row 18-06')

        self._add('642',
                  'Beige Gray Dark',
                  164,
                  152,
                  120,
                  'A49878',
                  'row 18-07')

        self._add('640',
                  'Beige Gray Vy Dk',
                  133,
                  123,
                  97,
                  '857B61',
                  'row 18-08')

        self._add('3787',
                  'Brown Gray Dark',
                  98,
                  93,
                  80,
                  '625D50',
                  'row 18-09')

        self._add('3021',
                  'Brown Gray Vy Dk',
                  79,
                  75,
                  65,
                  '4F4B41',
                  'row 18-10')

        self._add('3024',
                  'Brown Gray Vy Lt',
                  235,
                  234,
                  231,
                  'EBEAE7',
                  'row 18-11')

        self._add('3023',
                  'Brown Gray Light',
                  177,
                  170,
                  151,
                  'B1AA97',
                  'row 18-12')

        self._add('3022',
                  'Brown Gray Med',
                  142,
                  144,
                  120,
                  '8E9078',
                  'row 18-13')

        self._add('535',
                  'Ash Gray Vy Lt',
                  99,
                  100,
                  88,
                  '636458',
                  'row 18-14')

        self._add('3033',
                  'Mocha Brown Vy Lt',
                  227,
                  216,
                  204,
                  'E3D8CC',
                  'row 18-15')

        self._add('3782',
                  'Mocha Brown Lt',
                  210,
                  188,
                  166,
                  'D2BCA6',
                  'row 18-16')

        self._add('3032',
                  'Mocha Brown Med',
                  179,
                  159,
                  139,
                  'B39F8B',
                  'row 18-17')

        self._add('3790',
                  'Beige Gray Ult Dk',
                  127,
                  106,
                  85,
                  '7F6A55',
                  'row 18-18')

        self._add('3781',
                  'Mocha Brown Dk',
                  107,
                  87,
                  67,
                  '6B5743',
                  'row 18-19')

        self._add('3866',
                  'Mocha Brn Ult Vy Lt',
                  250,
                  246,
                  240,
                  'FAF6F0',
                  'row 18-20')

        self._add('842',
                  'Beige Brown Vy Lt',
                  209,
                  186,
                  161,
                  'D1BAA1',
                  'row 18-21')

        self._add('841',
                  'Beige Brown Lt',
                  182,
                  155,
                  126,
                  'B69B7E',
                  'row 18-22')

        self._add('840',
                  'Beige Brown Med',
                  154,
                  124,
                  92,
                  '9A7C5C',
                  'row 18-23')

        self._add('839',
                  'Beige Brown Dk',
                  103,
                  85,
                  65,
                  '675541',
                  'row 18-24')

        self._add('838',
                  'Beige Brown Vy Dk',
                  89,
                  73,
                  55,
                  '594937',
                  'row 18-25')

        self._add('3072',
                  'Beaver Gray Vy Lt',
                  230,
                  232,
                  232,
                  'E6E8E8',
                  'row 19-01')

        self._add('648',
                  'Beaver Gray Lt',
                  188,
                  180,
                  172,
                  'BCB4AC',
                  'row 19-02')

        self._add('647',
                  'Beaver Gray Med',
                  176,
                  166,
                  156,
                  'B0A69C',
                  'row 19-03')

        self._add('646',
                  'Beaver Gray Dk',
                  135,
                  125,
                  115,
                  '877D73',
                  'row 19-04')

        self._add('645',
                  'Beaver Gray Vy Dk',
                  110,
                  101,
                  92,
                  '6E655C',
                  'row 19-05')

        self._add('844',
                  'Beaver Gray Ult Dk',
                  72,
                  72,
                  72,
                  '484848',
                  'row 19-06')

        self._add('762',
                  'Pearl Gray Vy Lt',
                  236,
                  236,
                  236,
                  'ECECEC',
                  'row 19-07')

        self._add('415',
                  'Pearl Gray',
                  211,
                  211,
                  214,
                  'D3D3D6',
                  'row 19-08')

        self._add('318',
                  'Steel Gray Lt',
                  171,
                  171,
                  171,
                  'ABABAB',
                  'row 19-09')

        self._add('414',
                  'Steel Gray Dk',
                  140,
                  140,
                  140,
                  '8C8C8C',
                  'row 19-10')

        self._add('168',
                  'Pewter Very Light',
                  209,
                  209,
                  209,
                  'D1D1D1',
                  'row 19-11')

        self._add('169',
                  'Pewter Light',
                  132,
                  132,
                  132,
                  '848484',
                  'row 19-12')

        self._add('317',
                  'Pewter Gray',
                  108,
                  108,
                  108,
                  '6C6C6C',
                  'row 19-13')

        self._add('413',
                  'Pewter Gray Dark',
                  86,
                  86,
                  86,
                  '565656',
                  'row 19-14')

        self._add('3799',
                  'Pewter Gray Vy Dk',
                  66,
                  66,
                  66,
                  '424242',
                  'row 19-15')

        self._add('310',
                  'Black',
                  0,
                  0,
                  0,
                  '000000',
                  'row 19-16')
