# -*- coding: utf-8 -*-
"""Orange France"""
from lib.provider_templates import OrangeTemplate

class OrangeFranceProvider(OrangeTemplate):
    """Orange France provider"""

    # pylint: disable=line-too-long
    def __init__(self) -> None:
        super().__init__(
            endpoint_stream_info = 'https://mediation-tv.orange.fr/all/live/v3/applications/PC/users/me/channels/{channel_id}/stream?terminalModel=WEB_PC',
            endpoint_streams = 'https://mediation-tv.orange.fr/all/live/v3/applications/PC/channels?mco=OFR',
            endpoint_programs = 'https://mediation-tv.orange.fr/all/live/v3/applications/PC/programs?period={period}&mco=OFR',
            groups = {
                'TNT': \
                    [192, 4, 80, 34, 47, 118, 111, 445, 119, 195, 446, 444, 234, 78, 481, 226, 458, 482, 3163, 1404, 1401, 1403, 1402, 1400, 1399, 112, 2111],
                'Généralistes': \
                    [205, 191, 145, 115, 225],
                'Premium': \
                    [1290, 1304, 1335, 730, 733, 732, 734],
                'Cinéma': \
                    [185, 1562, 2072, 10, 282, 284, 283, 401, 285, 287, 1190],
                'Divertissement': \
                    [128, 1960, 5, 121, 2441, 2752, 87, 1167, 54, 2326, 2334, 49, 1408, 1832],
                'Jeunesse': \
                    [2803, 321, 928, 924, 229, 32, 888, 473, 2065, 1746, 58, 299, 300, 36, 344, 197, 293],
                'Découverte': \
                    [90112, 1072, 12, 2037, 38, 7, 88, 451, 829, 63, 508, 719, 147, 662, 402],
                'Jeunes': \
                    [563, 2942, 2353, 2442, 6, 2040, 1585, 2171, 2781],
                'Musique': \
                    [90150, 605, 2006, 1989, 453, 90159, 265, 90161, 90162, 90165, 2958, 125, 907, 1353],
                'Sport': \
                    [64, 2837, 1336, 1337, 1338, 1339, 1340, 1341, 1342, 15, 1166],
                'Jeux': \
                    [1061],
                'Société': \
                    [1996, 531, 90216, 57, 110, 90221],
                'Information française': \
                    [992, 90226, 1073, 140, 90230, 90231],
                'Information internationnale': \
                    [671, 90233, 53, 51, 410, 19, 525, 90239, 90240, 90241, 90242, 781, 830, 90246, 90504, 90505],
                'France 3 Régions': \
                    [655, 249, 304, 649, 647, 636, 634, 306, 641, 308, 642, 637, 646, 650, 638, 640, 651, 644, 313, 635, 645, 639, 643, 648]
            }
        )
