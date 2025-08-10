from time import sleep
from Classes.clearscreen import clearscreen
from Classes.inventory import Inventory
from Classes.pokemon import Pokémon
from Classes.trainer import Trainer, Player
from Classes.city import City, End, Bourg_palette
from Classes.road import Road, Site



bourg_palette = Bourg_palette()
plateau_indigo = End()

argenta = City(
    name= 'Argenta',
    has_arena= True, 
    shop_rank= "Beginner",
    arena_info= {
        "Name": "Arène d'Argenta", 
        "Liste Dresseurs": [
            Trainer(
                name= 'Campeur Elvin', 
                list_pokémon= [
                    Pokémon(pok_id= 74, level= 10),
                    Pokémon(pok_id= 27, level= 11)
                ]
            )
        ],
        "Champion": Trainer(
            name= 'Pierre',
            list_pokémon= [
                Pokémon(pok_id= 74,level= 12), 
                Pokémon(pok_id= 95,level= 14)
            ]
        ),
        "Nom Badge": 'Boulder Badge'
    }
)
jadielle = City(
    name= 'Jadielle',
    has_arena= True, 
    shop_rank= "Beginner",
    arena_info= {
        "Name": "Arène de Jadielle", 
        "Liste Dresseurs": [
            Trainer(
                name= "Dompteur Cyril",
                list_pokémon= [
                    Pokémon(pok_id= 24, level= 39),
                    Pokémon(pok_id= 128, level= 39)
                ]
            ), 
            Trainer(
                name= "Karatéka Akira", 
                list_pokémon= [
                    Pokémon(pok_id= 68, level= 43)
                ]
            ),
            Trainer(
                name= "Dompteur Youri",
                list_pokémon= [
                    Pokémon(pok_id= 111, level= 43)
                ]
            ),
            Trainer(
                name= "Topdresseur Samuel",
                list_pokémon= [
                    Pokémon(pok_id= 28, level= 37),
                    Pokémon(pok_id= 28, level= 37),
                    Pokémon(pok_id= 111, level= 37),
                    Pokémon(pok_id= 33, level= 39),
                    Pokémon(pok_id= 34, level= 39)
                ]
            ),
            Trainer(
                name= "Karatéka Tetsuo",
                list_pokémon= [
                    Pokémon(pok_id= 66, level= 40),
                    Pokémon(pok_id= 67, level= 40)
                ]
            ),
            Trainer(
                name= "Karatéka Takashi",
                list_pokémon= [
                    Pokémon(pok_id= 67, level= 38),
                    Pokémon(pok_id= 66, level= 38),
                    Pokémon(pok_id= 67, level= 38)
                ]
            ),
            Trainer(
                name= "Topdresseur Yuji",
                list_pokémon= [
                    Pokémon(pok_id= 28, level= 38),
                    Pokémon(pok_id= 75, level= 38),
                    Pokémon(pok_id= 95, level= 38),
                    Pokémon(pok_id= 75, level= 38),
                    Pokémon(pok_id= 105, level= 38)
                ]
            ),
            Trainer(
                name= "Topdresseur Wolfgang",
                list_pokémon= [
                    Pokémon(pok_id= 105, level= 37),
                    Pokémon(pok_id= 105, level= 37),
                    Pokémon(pok_id= 111, level= 38),
                    Pokémon(pok_id= 30, level= 39),
                    Pokémon(pok_id= 31, level= 39)
                ]
            )
        ],
        "Champion": Trainer(
            name= 'Giovanni',
            list_pokémon= [
                Pokémon(pok_id= 111,level= 45), 
                Pokémon(pok_id= 51,level= 42),
                Pokémon(pok_id= 31, level= 44),
                Pokémon(pok_id= 34, level= 45),
                Pokémon(pok_id= 112, level= 50)
            ]
        ),
        "Nom Badge": 'Earth Badge'
    }
)
azuria = City(
    name= 'Azuria',
    has_arena= True, 
    shop_rank= "Beginner",
    arena_info= {
        "Name": "Arène d'Azuria", 
        "Liste Dresseurs": [
            Trainer(
                name= "Nageur Louis", 
                list_pokémon= [
                    Pokémon(pok_id= 116, level= 16),
                    Pokémon(pok_id= 90, level= 16)
                ]
            ), 
            Trainer(
                name= "Pique-Nique Diane", 
                list_pokémon= [
                    Pokémon(pok_id= 118, level= 19)
                ]
            )
        ],
        "Champion": Trainer(
            name= 'Ondine',
            list_pokémon= [
                Pokémon(pok_id= 120,level= 18), 
                Pokémon(pok_id= 121,level= 21)
            ]
        ),
        "Nom Badge": 'Cascade Badge'
    }
)
carmin_sur_mer = City(
    name= 'Carmin-sur-Mer',
    has_arena= True, 
    shop_rank= "Intermediate",
    arena_info= {
        "Name": "Arène de Carmin-sur-Mer", 
        "Liste Dresseurs": [
            Trainer(
                name= "Marin Harold", 
                list_pokémon= [
                    Pokémon(pok_id= 25, level= 21),
                    Pokémon(pok_id= 25, level= 21)
                ]
            ), 
            Trainer(
                name= "Mécano Killian",
                list_pokémon= [
                    Pokémon(pok_id= 100, level= 21),
                    Pokémon(pok_id= 81, level= 21)
                ]
            ),
            Trainer(
                name= "Gentleman Anatole",
                list_pokémon= [
                    Pokémon(pok_id= 25, level= 23)
                ]
            )
        ],
        "Champion": Trainer(
            name= 'Major Bob',
            list_pokémon= [
                Pokémon(pok_id= 100, level= 21), 
                Pokémon(pok_id= 25, level= 18),
                Pokémon(pok_id= 26, level= 24)
            ]
        ),
        "Nom Badge": 'Thunder Badge'
    }
)
safrania = City(
    name= 'Safrania',
    has_arena= True, 
    shop_rank= "Advanced",
    arena_info= {
        "Name": "Arène de Safrania", 
        "Liste Dresseurs": [
            Trainer(
                name= "Kinésiste Prosper", 
                list_pokémon= [
                    Pokémon(pok_id= 79, level= 33),
                    Pokémon(pok_id= 79, level= 33),
                    Pokémon(pok_id= 80, level= 33)
                ]
            ),
            Trainer(
                name= "Kinésiste Tyron",
                list_pokémon= [
                    Pokémon(pok_id= 122, level= 34),
                    Pokémon(pok_id= 64, level= 34)
                ]
            ),
            Trainer(
                name= "Kinésiste Noé", 
                list_pokémon= [
                    Pokémon(pok_id= 64, level= 31),
                    Pokémon(pok_id= 79, level= 31),
                    Pokémon(pok_id= 122, level= 31),
                    Pokémon(pok_id= 64, level= 31)
                ]
            ),
            Trainer(
                name= "Kinésiste Polo",
                list_pokémon= [
                    Pokémon(pok_id= 80, level= 38)
                ]
            ),
            Trainer(
                name= "Exorciste Tatiana",
                list_pokémon= [
                    Pokémon(pok_id= 92, level= 33),
                    Pokémon(pok_id= 92, level= 33),
                    Pokémon(pok_id= 93, level= 33)
                ]
            ),
            Trainer(
                name= "Exorciste Aimée",
                list_pokémon= [
                    Pokémon(pok_id= 93, level= 38)
                ]
            ),
            Trainer(
                name= "Exorciste Amanda",
                list_pokémon= [
                    Pokémon(pok_id= 92, level= 34),
                    Pokémon(pok_id= 93, level= 34)
                ]
            )
        ],
        "Champion": Trainer(
            name= 'Morgane',
            list_pokémon= [
                Pokémon(pok_id= 64,level= 38), 
                Pokémon(pok_id= 122,level= 37), 
                Pokémon(pok_id= 49,level= 38), 
                Pokémon(pok_id= 65,level= 43)
            ]
        ),
        "Nom Badge": 'Marsh Badge'
    }
)
lavanvile = City(
    name= 'Lavanvile',
    has_arena= False, 
    shop_rank= "Intermediate",
    arena_info= None
)
céladopole = City(
    name= 'Céladopole',
    has_arena= True, 
    shop_rank= "Advanced",
    arena_info= {
        "Name": "Arène de Céladopole", 
        "Liste Dresseurs": [
            Trainer(
                name= "Fillette Katy", 
                list_pokémon= [
                    Pokémon(pok_id= 69, level= 23),
                    Pokémon(pok_id= 70, level= 23)
                ]
            ), 
            Trainer(
                name= "Canon Elodie", 
                list_pokémon= [
                    Pokémon(pok_id= 43, level= 21),
                    Pokémon(pok_id= 69, level= 21),
                    Pokémon(pok_id= 43, level= 21),
                    Pokémon(pok_id= 69, level= 21),
                ]
            ),
            Trainer(
                name= "Canon Tamia",
                list_pokémon= [
                    Pokémon(pok_id= 69, level= 24),
                    Pokémon(pok_id= 69, level= 24)
                ]
            ),
            Trainer(
                name= "Pique-Nique Tina",
                list_pokémon= [
                    Pokémon(pok_id= 1, level= 24),
                    Pokémon(pok_id= 2, level= 24)
                ]
            ),
            Trainer(
                name= "Fillette Lisa",
                list_pokémon= [
                    Pokémon(pok_id= 43, level= 23),
                    Pokémon(pok_id= 44, level= 23)
                ]
            ),
            Trainer(
                name= "Canon Laurence",
                list_pokémon= [
                    Pokémon(pok_id= 102, level= 24)
                ]
            ),
            Trainer(
                name= "Top Dresseur Marie",
                list_pokémon= [
                    Pokémon(pok_id= 69, level= 22),
                    Pokémon(pok_id= 43, level= 22),
                    Pokémon(pok_id= 70, level= 22),
                    Pokémon(pok_id= 44, level= 22),
                    Pokémon(pok_id= 2, level= 22)
                ]
            )
        ],
        "Champion": Trainer(
            name= 'Erika',
            list_pokémon= [
                Pokémon(pok_id= 71,level= 29), 
                Pokémon(pok_id= 114,level= 24),
                Pokémon(pok_id= 45, level= 29)
            ]
        ),
        "Nom Badge": 'Rainbow Badge'
    }
)
parmanie = City(
    name= 'Parmanie',
    has_arena= True, 
    shop_rank= "Advanced",
    arena_info= {
        "Name": "Arène de Parmanie", 
        "Liste Dresseurs": [
            Trainer(
                name= "Jongleur Melvin", 
                list_pokémon= [
                    Pokémon(pok_id= 97, level= 38)
                ]
            ), 
            Trainer(
                name= "Jongleur Vincente", 
                list_pokémon= [
                    Pokémon(pok_id= 96, level= 34),
                    Pokémon(pok_id= 64, level= 34)
                ]
            ),
            Trainer(
                name= "Jongleur Chris",
                list_pokémon= [
                    Pokémon(pok_id= 96, level= 31),
                    Pokémon(pok_id= 96, level= 31),
                    Pokémon(pok_id= 64, level= 34),
                    Pokémon(pok_id= 96, level= 31)

                ]
            ),
            Trainer(
                name= "Dompteur Edgard",
                list_pokémon= [
                    Pokémon(pok_id= 24, level= 33),
                    Pokémon(pok_id= 24, level= 33),
                    Pokémon(pok_id= 28, level= 33)
                ]
            ),
            Trainer(
                name= "Dompteur Phil",
                list_pokémon= [
                    Pokémon(pok_id= 28, level= 34),
                    Pokémon(pok_id= 24, level= 34),
                ]
            ),
            Trainer(
                name= "Jongleur Robert",
                list_pokémon= [
                    Pokémon(pok_id= 96, level= 34),
                    Pokémon(pok_id= 97, level= 34)
                ]
            )
        ],
        "Champion": Trainer(
            name= 'Koga',
            list_pokémon= [
                Pokémon(pok_id= 109,level= 37), 
                Pokémon(pok_id= 89, level= 39),
                Pokémon(pok_id= 109,level= 37), 
                Pokémon(pok_id= 110, level= 43)
            ]
        ),
        "Nom Badge": 'Soul Badge'
    }
)
cramois_ile = City(
    name= "Cramois'île",
    has_arena= True, 
    shop_rank= "Max",
    arena_info= {
        "Name": "Arène d'argenta", 
        "Liste Dresseurs": [
            Trainer(
                name= 'Sous-champion 1', 
                list_pokémon= [Pokémon(pok_id= 30)]), 
            Trainer(
                name= 'Sous-champion 2', 
                list_pokémon= [Pokémon(pok_id= 53)])],
        "Champion": Trainer(
            name= 'Auguste',
            list_pokémon= [
                Pokémon(pok_id= 43,level= 13), 
                Pokémon(pok_id= 67,level= 15)
            ]
        ),
        "Nom Badge": 'Volcano Badge'
    }
)
foret_de_jade = Site(
    name= "Foret de Jade",
    list_wild_pok_id= [10, 13, 11, 14, 25],
    wild_pok_lvl_range= range(3, 7),
    list_trainers= [
        Trainer(
            name= "Scout Omar",
            list_pokémon = [
                Pokémon(pok_id= 10, level= 6),
                Pokémon(pok_id= 13, level= 6)
                ]),
        Trainer(
            name= "Scout Alfred",
            list_pokémon= [
                Pokémon(pok_id= 13, level= 7),
                Pokémon(pok_id= 13, level= 7),
                Pokémon(pok_id= 14, level= 7)
                ]),
        Trainer(
            name= "Scout Anthony",
            list_pokémon= [
                Pokémon(pok_id= 10, level= 7),
                Pokémon(pok_id= 10, level= 8)
                ]),
        Trainer(
            name= "Scout Charles",
            list_pokémon= [
                Pokémon(pok_id= 11, level= 7),
                Pokémon(pok_id= 10, level= 7),
                Pokémon(pok_id= 11, level= 7)
                ]),
        Trainer(
            name= "Scout Sammy",
            list_pokémon= [
                Pokémon(pok_id= 13, level= 9)
            ]
        )
    ],
)
mont_selenite = Site(
    name= "Mont Sélénite",
    list_wild_pok_id= [41, 74, 46, 35],
    wild_pok_lvl_range= range(6, 13),
    list_trainers= [
        Trainer(
            name= "Scout Ken",
            list_pokémon= [
                Pokémon(pok_id= 13, level= 11),
                Pokémon(pok_id= 14, level= 11)
            ]
        ),
        Trainer(
            name= "Fillette Iris",
            list_pokémon= [
                Pokémon(pok_id= 35, level= 14)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 27, level= 11),
                Pokémon(pok_id= 19, level= 11),
                Pokémon(pok_id= 41, level= 11)
            ]
        ),
        Trainer(
            name= "Intello Remi",
            list_pokémon= [
                Pokémon(pok_id= 81, level= 11),
                Pokémon(pok_id= 100, level= 11)
            ]
        ),
        Trainer(
            name= "Scout Robin",
            list_pokémon= [
                Pokémon(pok_id= 10, level= 10),
                Pokémon(pok_id= 10, level= 10),
                Pokémon(pok_id= 11, level= 10)
            ]
        ),
        Trainer(
            name= "Fillette Miriam",
            list_pokémon= [
                Pokémon(pok_id= 43, level= 11),
                Pokémon(pok_id= 69, level= 11)
            ]
        ),
        Trainer(
            name= "Gamin Johnny",
            list_pokémon= [
                Pokémon(pok_id= 19, level= 10),
                Pokémon(pok_id= 19, level= 10),
                Pokémon(pok_id= 41, level= 10)
            ]
        ),
        Trainer(
            name= "Montagnard Marius",
            list_pokémon= [
                Pokémon(pok_id= 74, level= 10),
                Pokémon(pok_id= 74, level= 10),
                Pokémon(pok_id= 95, level= 10)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 41, level= 11),
                Pokémon(pok_id= 23, level= 11)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 19, level= 13),
                Pokémon(pok_id= 27, level= 13)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 19, level= 13),
                Pokémon(pok_id= 41, level= 13)
            ]
        ),
        Trainer(
            name= "Intello Michel",
            list_pokémon= [
                Pokémon(pok_id= 88, level= 12),
                Pokémon(pok_id= 100, level= 12),
                Pokémon(pok_id= 109, level= 12)
            ]
        )
    ],
    has_legendary= True,
    legendary_id= 142,
    legendary_level= 15
)
océane = Site(
    name= "L'Océane",
    list_wild_pok_id= None,
    wild_pok_lvl_range= None,
    list_trainers= [
        Trainer(
            name= "Gentleman Tony",
            list_pokémon= [
                Pokémon(pok_id= 58, level= 18),
                Pokémon(pok_id= 58, level= 18),
            ]
        ),
        Trainer(
            name= "Gentleman Lilian",
            list_pokémon= [
                Pokémon(pok_id= 32, level= 19),
                Pokémon(pok_id= 29, level= 19)
            ]   
        ),
        Trainer(
            name= "Gamin Ethan",
            list_pokémon= [
                Pokémon(pok_id= 32, level= 21)
            ]
        ),
        Trainer(
            name= "Fillette Lotte",
            list_pokémon= [
                Pokémon(pok_id= 16, level= 18),
                Pokémon(pok_id= 29, level= 18)
            ]
        ),
        Trainer(
            name= "Marin Ludovic",
            list_pokémon= [
                Pokémon(pok_id= 116, level= 17),
                Pokémon(pok_id= 90, level= 17),
                Pokémon(pok_id= 72, level= 17)
            ]
        ),
        Trainer(
            name= "Marin Leonard",
            list_pokémon= [
                Pokémon(pok_id= 90, level= 21)
            ]
        ),
        Trainer(
            name= "Marin Régis",
            list_pokémon= [
                Pokémon(pok_id= 116, level= 17),
                Pokémon(pok_id= 116, level= 17),
                Pokémon(pok_id= 116, level= 17),
            ]
        ),
        Trainer(
            name= "Marin Henri",
            list_pokémon= [
                Pokémon(pok_id= 72, level= 18),
                Pokémon(pok_id= 120, level= 18)
            ]
        ),
        Trainer(
            name= "Pêcheur Barney",
            list_pokémon= [
                Pokémon(pok_id= 72, level= 17),
                Pokémon(pok_id= 120, level= 17),
                Pokémon(pok_id= 90, level= 17)
            ]
        ),
        Trainer(
            name= "Marin Philippe",
            list_pokémon= [
                Pokémon(pok_id= 66, level=20)
            ]
        ),
        Trainer(
            name= "Pêcheur Fabio",
            list_pokémon= [
                Pokémon(pok_id= 118, level= 17),
                Pokémon(pok_id= 118, level= 17),
                Pokémon(pok_id= 72, level= 17)
            ]
        ),
        Trainer(
            name= "Gentleman Samy",
            list_pokémon= [
                Pokémon(pok_id= 25, level= 23),
            ]
        ),
        Trainer(
            name= "Fillette Maëlle",
            list_pokémon= [
                Pokémon(pok_id= 19, level= 18),
                Pokémon(pok_id= 25, level= 18)
            ]
        ),
        Trainer(
            name= "Gentleman Lamar",
            list_pokémon= [
                Pokémon(pok_id= 58, level= 17),
                Pokémon(pok_id= 77, level= 17)
            ]
        ),
        Trainer(
            name= "Marin Edmomd",
            list_pokémon= [
                Pokémon(pok_id= 66, level= 18),
                Pokémon(pok_id= 90, level= 18)
            ]
        ),
        Trainer(
            name= "Marin Trevor",
            list_pokémon= [
                Pokémon(pok_id= 66, level= 17),
                Pokémon(pok_id= 72, level= 17)
            ]
        )
    ]
)
grotte = Site(
    name= "Grotte",

    list_trainers= [
        Trainer(
            name= "Pokémoniac Quentin",
            list_pokémon= [
                Pokémon(pok_id= 104, level= 23),
                Pokémon(pok_id= 79, level= 23)
            ]
        ),
        Trainer(
            name="Pokémaniac Jean-Marie",
            list_pokémon= [
                Pokémon(pok_id= 79, level= 25)
            ]
        ),
        Trainer(
            name= "Pique-Nique Marthe",
            list_pokémon= [
                Pokémon(pok_id= 43, level= 22),
                Pokémon(pok_id= 1, level= 22)
            ]
        ),
        Trainer(
            name= "Pokémaniac Stephane",
            list_pokémon= [
                Pokémon(pok_id= 4, level= 22),
                Pokémon(pok_id= 104, level= 22)
            ]
        ),
        Trainer(
            name= "Montagnard Alain",
            list_pokémon= [
                Pokémon(pok_id= 74, level= 25)
            ]
        ),
        Trainer(
            name= "Montagnard Eric",
            list_pokémon= [
                Pokémon(pok_id= 66, level= 20),
                Pokémon(pok_id= 95, level= 20)
            ]
        ),
        Trainer(
            name= "Montagnard Jean-Luc",
            list_pokémon= [
                Pokémon(pok_id= 74, level= 19),
                Pokémon(pok_id= 74, level= 19),
                Pokémon(pok_id= 74, level= 19),
                Pokémon(pok_id= 66, level= 19)
            ]
        ),
        Trainer(
            name= "Mnntagnard Tanguy",
            list_pokémon= [
                Pokémon(pok_id= 95, level= 20),
                Pokémon(pok_id= 74, level= 20),
                Pokémon(pok_id= 95, level= 20)
            ]
        ),
        Trainer(
            name= "Montagnard Lucas",
            list_pokémon= [
                Pokémon(pok_id= 74, level= 21),
                Pokémon(pok_id= 75, level= 21)
            ]
        ),
        Trainer(
            name= "Pique-Nique Sofia",
            list_pokémon= [
                Pokémon(pok_id= 39, level= 21),
                Pokémon(pok_id= 16, level= 21),
                Pokémon(pok_id= 52, level= 21)
            ]
        ),
        Trainer(
            name= "Montagnard Dorian",
            list_pokémon= [
                Pokémon(pok_id= 74, level= 21),
                Pokémon(pok_id= 74, level= 21),
                Pokémon(pok_id= 75, level= 21)
            ]
        ),
        Trainer(
            name= "Pokémoniac Arthur",
            list_pokémon= [
                Pokémon(pok_id= 79, level= 20),
                Pokémon(pok_id= 79, level= 20),
                Pokémon(pok_id= 79, level= 20)
            ]
        ),
        Trainer(
            name= "Pique-Nique Erin",
            list_pokémon= [
                Pokémon(pok_id= 69, level= 22),
                Pokémon(pok_id= 35, level= 22),
            ]
        ),
        Trainer(
            name= "Pique-Nique Kim",
            list_pokémon= [
                Pokémon(pok_id= 16, level= 19),
                Pokémon(pok_id= 19, level= 19),
                Pokémon(pok_id= 19, level= 19),
                Pokémon(pok_id= 69, level= 19)
            ]
        ),
        Trainer(
            name= "Pique-Nique Christelle",
            list_pokémon= [
                Pokémon(pok_id= 52, level= 20),
                Pokémon(pok_id= 43, level= 20),
                Pokémon(pok_id= 16, level= 20)
            ]
        )
    ]
)
grotte_azurée = Site(
    name= "Grotte Azurée",
    list_trainers= None)
tour_pokémon = Site(
    name= "Tour Pokémon",
    list_trainers= [
        Trainer(
            name= " Gamin Kevin",
            list_pokémon= [
                Pokémon(pok_id= 17, level= 25),
                Pokémon(pok_id=130, level= 23),
                Pokémon(pok_id= 58, level= 22),
                Pokémon(pok_id= 2, level= 25),
                Pokémon(pok_id= 64, level= 20)
            ]
        ),
        Trainer(
            name= "Exorciste Lara",
            list_pokémon= [
                Pokémon(pok_id= 92, level= 24)
            ]
        ),
        Trainer(
            name= "Exorciste Patricia",
            list_pokémon= [
                Pokémon(pok_id= 92, level= 22)
            ]
        ),
        Trainer(
            name= "Exorciste Hortense",
            list_pokémon= [
                Pokémon(pok_id= 92, level= 23)
            ]
        ),
        Trainer(
            name= "Exorciste Graziella",
            list_pokémon= [
                Pokémon(pok_id= 92, level= 23),
                Pokémon(pok_id= 92, level= 23),
            ]
        ),
        Trainer(
            name= "Exorciste Joelle",
            list_pokémon= [
                Pokémon(pok_id= 92, level= 22)
            ]
        ),
        Trainer(
            name= "Exorciste Paula",
            list_pokémon= [
                Pokémon(pok_id= 92, level= 24)
            ]
        ),
        Trainer(
            name= "Exorciste Aurore",
            list_pokémon= [
                Pokémon(pok_id= 92, level= 22)
            ]
        ),
        Trainer(
            name= "Exorciste Tania",
            list_pokémon= [
                Pokémon(pok_id= 93, level= 23)
            ]
        ),
        Trainer(
            name= "Exorciste Karina",
            list_pokémon= [
                Pokémon(pok_id= 92, level= 24)
            ]
        ),
        Trainer(
            name= "Exorciste Zia",
            list_pokémon= [
                Pokémon(pok_id= 92, level= 22)
            ]
        ),
        Trainer(
            name= "Exorciste Angélique",
            list_pokémon= [
                Pokémon(pok_id= 92, level= 22),
                Pokémon(pok_id= 92, level= 22),
                Pokémon(pok_id= 92, level= 22)
            ]
        ),
        Trainer(
            name= "Exorciste Jennifer",
            list_pokémon= [
                Pokémon(pok_id= 92, level= 24)
            ]
        ),
        Trainer(
            name= "Exorciste Sara",
            list_pokémon= [
                Pokémon(pok_id= 92, level= 24)
            ]
        ),
        Trainer(
            name=  "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 41, level= 25),
                Pokémon(pok_id= 41, level= 25),
                Pokémon(pok_id= 42, level= 25)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 109, level= 26),
                Pokémon(pok_id= 96, level= 26)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 41, level= 23),
                Pokémon(pok_id= 19, level= 23),
                Pokémon(pok_id= 20, level= 23),
                Pokémon(pok_id= 41, level= 23)
            ]
        )
    ]
)
cave_taupiqueur = Site(
    name= "Cave Taupiqueur",
    list_wild_pok_id= [50, 51],
    wild_pok_lvl_range= range(15, 31),
    list_trainers= None
)
casino = Site(
    name= "Casino",
    list_trainers= [
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 20, level= 20),
                Pokémon(pok_id= 41, level= 20)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 20, level= 21),
                Pokémon(pok_id= 20, level= 21)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 96, level= 21),
                Pokémon(pok_id= 66, level= 21)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 41, level= 17),
                Pokémon(pok_id= 109, level= 17),
                Pokémon(pok_id= 88, level= 17),
                Pokémon(pok_id= 41, level= 17),
                Pokémon(pok_id= 20, level= 17)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 19, level= 19),
                Pokémon(pok_id= 20, level= 19),
                Pokémon(pok_id= 20, level= 19),
                Pokémon(pok_id= 19, level= 19)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 88, level= 20),
                Pokémon(pok_id= 109, level= 20),
                Pokémon(pok_id= 109, level= 20)
            ]
        ),
        Trainer(
            name=  "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 19, level= 20),
                Pokémon(pok_id= 20, level= 20),
                Pokémon(pok_id= 96, level= 20)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 109, level= 21),
                Pokémon(pok_id= 41, level= 21)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 66, level= 21),
                Pokémon(pok_id= 66, level= 21),
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 88, level= 22),
                Pokémon(pok_id= 109, level= 22)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 23, level= 23),
                Pokémon(pok_id= 27, level= 23),
                Pokémon(pok_id= 24, level= 23)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 27, level= 23),
                Pokémon(pok_id= 23, level= 23),
                Pokémon(pok_id= 28, level= 23)
            ]
        ),
        Trainer(
            name= "Boss Giovanni",
            list_pokémon= [
                Pokémon(pok_id= 95, level= 25),
                Pokémon(pok_id= 111, level= 24),
                Pokémon(pok_id= 115, level= 29)
            ]
        )
    ]
)
dojo = Road(
    name=  "Dojo Pokémon",
    list_trainers= [
        Trainer(
            name= "Karateka Hitoshi",
            list_pokémon= [
                Pokémon(pok_id= 66, level= 31),
                Pokémon(pok_id= 56, level= 31),
                Pokémon(pok_id= 57, level= 31)
            ]
        ),
        Trainer(
            name= "Karateka Hideki",
            list_pokémon= [
                Pokémon(pok_id= 66, level= 32),
                Pokémon(pok_id= 67, level= 32),

            ]
        ),
        Trainer(
            name= "Karateka Igor",
            list_pokémon= [
                Pokémon(pok_id= 57, level= 36),
            ]
        ),
        Trainer(
            name= "Karateka Maxime",
            list_pokémon= [
                Pokémon(pok_id= 56, level= 31),
                Pokémon(pok_id= 56, level= 31),
                Pokémon(pok_id= 57, level= 31)
            ]
        ),
        Trainer(
            name= "Karateka Koichi",
            list_pokémon= [
                Pokémon(pok_id= 106, level= 37),
                Pokémon(pok_id= 107, level= 37)
            ]
        )
    ]
)
sylphe_sarl = Road(
    name= "Sylphe S.A.R.L",
    list_trainers= [
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 110, level= 28),
                Pokémon(pok_id= 42, level= 28),
                Pokémon(pok_id= 109, level= 28)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 20, level= 26),
                Pokémon(pok_id= 42, level= 26),
                Pokémon(pok_id= 24, level= 26),
                Pokémon(pok_id= 109, level= 26)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 104, level= 29),
                Pokémon(pok_id= 104, level= 29),
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 20, level= 26),
                Pokémon(pok_id= 41, level= 26),
                Pokémon(pok_id= 42, level= 26),
                Pokémon(pok_id= 19, level= 26)
            ]
        ),
        Trainer(
            name= "Scientifique Joseph",
            list_pokémon= [
                Pokémon(pok_id= 101, level= 29),
                Pokémon(pok_id= 89, level= 29)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 20, level= 28),
                Pokémon(pok_id= 97, level= 28),
                Pokémon(pok_id= 20, level= 28)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 24, level= 33),
            ]
        ),
        Trainer(
            name= "Gamin Kevin",
            list_pokémon= [
                Pokémon(pok_id= 18, level= 37),
                Pokémon(pok_id= 130, level= 38),
                Pokémon(pok_id= 58, level= 35),
                Pokémon(pok_id= 65, level= 35),
                Pokémon(pok_id= 3, level= 40)
            ]
        ),
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 104, level= 32),
                Pokémon(pok_id= 105, level= 32),
                Pokémon(pok_id= 96, level= 32)
            ]
        ),
        Trainer(
            name= "Boss Giovanni",
            list_pokémon= [
                Pokémon(pok_id= 33, level= 37),
                Pokémon(pok_id= 111, level= 37),
                Pokémon(pok_id= 115, level= 35),
                Pokémon(pok_id= 31, level= 41)
            ]
        )
    ]
)
iles_écumes = Road(
    name= "îles Écumes",
    list_trainers= None)
parc_safari = Road(
    name= "Parc Safari",
    list_trainers= None)
centrale_electrique = Road(
    name= "Centrale",
    list_trainers= [
        Trainer(
            name= "Pokémaniac Achille",
            list_pokémon= [
                Pokémon(pok_id= 111, level= 29),
                Pokémon(pok_id= 108, level= 29)
            ]
        )
    ])
manoir_pokémon = Road(
    name= "Manoir Pokémon",
    list_trainers= None)
route_victoire = Road(
    name= "Route Victoire",
    list_trainers= None)

road_1 = Road(
    name= "Route 1",
    list_wild_pok_id= [16, 19],
    wild_pok_lvl_range= range(2,6), 
    list_trainers= None
)
road_2 = Road(
    name= "Route 2",
    list_wild_pok_id= [10, 13, 16, 19],
    wild_pok_lvl_range= range(2, 6),
    list_trainers= None
)
road_3 = Road(
    name= "Route 3",
    list_wild_pok_id= [21, 16, 32, 29, 39, 56],
    wild_pok_lvl_range= range(5, 8),
    list_trainers= [
        Trainer(
            name= "Fillette Perrine",
            list_pokémon= [
                Pokémon(pok_id= 16, level= 9),
                Pokémon(pok_id= 16, level= 9)
            ]
        ),
        Trainer(
            name= "Scout Piotr",
            list_pokémon= [
                Pokémon(pok_id= 10, level= 10),
                Pokémon(pok_id= 13, level= 10),
                Pokémon(pok_id= 10, level= 10)
            ]
        ),
        Trainer(
            name= "Gamin Ben",
            list_pokémon= [
                Pokémon(pok_id= 19, level= 11),
                Pokémon(pok_id= 23,level= 11)
            ]
        ),
        Trainer(
            name= "Scout Gregory",
            list_pokémon= [
                Pokémon(pok_id= 13, level= 9),
                Pokémon(pok_id= 14, level= 9),
                Pokémon(pok_id= 10, level= 9),
                Pokémon(pok_id= 11, level= 9)
            ]
        ),
        Trainer(
            name= "Fillette Sally",
            list_pokémon= [
                Pokémon(pok_id=19, level= 10),
                Pokémon(pok_id=29, level= 10)
            ]
        ),
        Trainer(
            name= "Gamin Calvin",
            list_pokémon= [
                Pokémon(pok_id= 21, level= 14),
            ]
        ),
        Trainer(
            name= "Scout James",
            list_pokémon= [
                Pokémon(pok_id= 10, level= 11),
                Pokémon(pok_id= 11, level= 11)
            ]
        ),
        Trainer(
            name= "Fillete Suzette",
            list_pokémon= [
                Pokémon(pok_id= 39, level= 14)
            ]
        )                
    ]
)
road_4 = Road(
    name= "Route 4",
    list_wild_pok_id= [19, 21, 23, 27, 56, 72, 129],
    wild_pok_lvl_range= range (7, 13),
    list_trainers= [
        Trainer(
            name= "Fillette Rachel",
            list_pokémon= [
                Pokémon(pok_id= 46, level= 31),
                Pokémon(pok_id= 46, level= 31),
                Pokémon(pok_id= 47, level= 31)
            ]
        )
    ]
)
road_5 = Road(
    name= "Route 5",
    list_wild_pok_id= [16, 52, 43, 69],
    wild_pok_lvl_range= range(11, 17),
    list_trainers= [
        Trainer(
            name= "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 41, level= 17),
                Pokémon(pok_id= 96, level= 19)
            ]
        )
    ]
)
road_6 = Road(
    name= "Route 6",
    list_wild_pok_id= [16, 52, 43, 69, 129, 60, 118],
    wild_pok_lvl_range= range(12, 17),
    list_trainers= [
        Trainer(
            name= "Scout Keneda",
            list_pokémon= [
                Pokémon(pok_id= 13, level= 16),
                Pokémon(pok_id= 13, level= 16),
                Pokémon(pok_id= 10, level= 16)
            ]
        ),
        Trainer(
            name= "Campeur Rachid",
            list_pokémon= [
                Pokémon(pok_id= 7, level= 20)
            ]
        ),
        Trainer(
            name= "Pique-Nique Nancy",
            list_pokémon= [
                Pokémon(pok_id= 19, level= 16),
                Pokémon(pok_id= 25, level= 16)
            ]
        ),
        Trainer(
            name= "Scout Elijah",
            list_pokémon= [
                Pokémon(pok_id= 12, level= 20)
            ]
        ),
        Trainer(
            name= "Pique-Nique Isabelle",
            list_pokémon= [
                Pokémon(pok_id= 16, level= 16),
                Pokémon(pok_id= 16, level= 16),
                Pokémon(pok_id= 16, level= 16)
            ]
        ),
        Trainer(
            name= "campeur Antonio",
            list_pokémon= [
                Pokémon(pok_id= 21, level= 16),
                Pokémon(pok_id= 20, level= 16)
            ]
        )
    ]
)
road_7 = Road(
    name= "Route 7",
    list_wild_pok_id= [52, 16, 43, 69, 58, 37],
    wild_pok_lvl_range= range(17, 23),
    list_trainers= None
)
road_8 = Road(
    name= "Route 8",
    list_wild_pok_id= [16, 52, 23, 27, 37, 58],
    wild_pok_lvl_range= range(16, 20),
    list_trainers= [
        Trainer(
            name= "Fillette Julia",
            list_pokémon= [
                Pokémon(pok_id= 35, level= 22),
                Pokémon(pok_id= 35, level= 22),
            ]
        ),
        Trainer(
            name= "Croupier Blaise",
            list_pokémon= [
                Pokémon(pok_id= 58, level= 24),
                Pokémon(pok_id= 37, level= 24)
            ]
        ),
        Trainer(
            name= "Intello Glenn",
            list_pokémon= [
                Pokémon(pok_id= 88, level= 22),
                Pokémon(pok_id= 89, level= 22),
                Pokémon(pok_id= 88, level= 22)
            ]
        ),
        Trainer(
            name= "Fillette Manire",
            list_pokémon= [
                Pokémon(pok_id= 29, level= 23),
                Pokémon(pok_id= 30, level= 23)
            ]
        ),
        Trainer(
            name= "Intello Jovan",
            list_pokémon= [
                Pokémon(pok_id= 109, level= 26)
            ]
        ),
        Trainer(
            name= "Fillette Valentine",
            list_pokémon= [
                Pokémon(pok_id= 52, level= 24),
                Pokémon(pok_id= 52, level= 24),
                Pokémon(pok_id= 52, level= 24)
            ]
        ),
        Trainer(
            name= "Fillette Megan",
            list_pokémon= [
                Pokémon(pok_id= 16, level= 19),
                Pokémon(pok_id= 19, level= 19),
                Pokémon(pok_id= 32, level= 19),
                Pokémon(pok_id= 52, level= 19),
                Pokémon(pok_id= 25, level= 19)
            ]
        ),
        Trainer(
            name= "Motard Medhi",
            list_pokémon= [
                Pokémon(pok_id= 88, level= 24),
                Pokémon(pok_id= 88, level= 24)
            ]
        ),
        Trainer(
            name= "Motard Ricardo",
            list_pokémon= [
                Pokémon(pok_id= 109, level= 22),
                Pokémon(pok_id= 109, level= 22),
                Pokémon(pok_id= 88, level= 22)
            ]
        ),
        Trainer(
            name= "Croupier Stanislas",
            list_pokémon= [
                Pokémon(pok_id= 60, level= 22),
                Pokémon(pok_id= 60, level= 22),
                Pokémon(pok_id= 61, level= 22)
            ]
        ),
        Trainer(
            name= "Intello Luc",
            list_pokémon= [
                Pokémon(pok_id= 100, level= 20),
                Pokémon(pok_id= 109, level= 20),
                Pokémon(pok_id= 100, level= 20),
                Pokémon(pok_id= 81, level= 20)
            ]
        )
    ]
)
road_9 = Road(
    name= "Route 9",
    list_wild_pok_id= [19, 21, 23, 27],
    wild_pok_lvl_range= range(13, 18),
    list_trainers= [
        Trainer(
            name= "Pique-Nique Alicia",
            list_pokémon= [
                Pokémon(pok_id= 43, level= 18),
                Pokémon(pok_id= 69, level= 18),
                Pokémon(pok_id= 43, level= 18),
                Pokémon(pok_id= 69, level= 18)
            ]
        ),
        Trainer(
            name= "Montagnard Maurice",
            list_pokémon= [
                Pokémon(pok_id= 66, level= 20),
                Pokémon(pok_id= 95, level= 20)
            ]
        ),
        Trainer(
            name= "Campeur Christophe",
            list_pokémon= [
                Pokémon(pok_id= 58, level= 21),
                Pokémon(pok_id= 4, level= 21)
            ]
        ),
        Trainer(
            name= "Scout Brad",
            list_pokémon= [
                Pokémon(pok_id= 15, level= 19),
                Pokémon(pok_id= 15, level= 19)
            ]
        ),
        Trainer(
            name= "Montagnard Al",
            list_pokémon= [
                Pokémon(pok_id= 74, level= 21),
                Pokémon(pok_id= 95, level= 21)
            ]
        ),
        Trainer(
            name= "Scout Gerard",
            list_pokémon= [
                Pokémon(pok_id= 10, level= 20),
                Pokémon(pok_id= 13, level= 20),
                Pokémon(pok_id= 48, level= 20)
            ]
        ),
        Trainer(
            name= "Campeur Tristan",
            list_pokémon= [
                Pokémon(pok_id= 19, level= 19),
                Pokémon(pok_id= 27, level= 19),
                Pokémon(pok_id= 27, level= 19),
                Pokémon(pok_id= 23, level= 19)
            ]
        ),
        Trainer(
            name= "Montagnard Brice",
            list_pokémon= [
                Pokémon(pok_id= 74, level= 20),
                Pokémon(pok_id= 74, level= 20),
                Pokémon(pok_id= 66, level= 20)
            ]
        ),
        Trainer(
            name= "Pique-Nique Emma",
            list_pokémon= [
                Pokémon(pok_id= 52, level=23)
            ]
        )
    ]
)
road_10 = Road(
    name= "Route 10",
    list_wild_pok_id= [100, 21, 23, 27, 72, 129],
    wild_pok_lvl_range= range(13, 18),
    list_trainers= [
        Trainer(
            name= "Pique-Nique Heidi",
            list_pokémon= [
                Pokémon(pok_id= 25, level= 20),
                Pokémon(pok_id= 35, level= 20)
            ]
        ),
        Trainer(
            name= "Montagnard Luigi",
            list_pokémon= [
                Pokémon(pok_id= 74, level= 21),
                Pokémon(pok_id= 95, level= 21)
            ]
        ),
        Trainer(
            name= "Montagnard Guillaume",
            list_pokémon= [
                Pokémon(pok_id= 95, level= 19),
                Pokémon(pok_id= 75, level= 19)
            ]
        ),
        Trainer(
            name=  "Pokémaniac Hervé",
            list_pokémon= [
                Pokémon(pok_id= 104, level= 20),
                Pokémon(pok_id= 79, level= 20)
            ]
        )
    ]
)
road_11 = Road(
    name= "Route 11",
    list_wild_pok_id= [23, 27, 21, 96, 72, 129, 98, 116],
    wild_pok_lvl_range= range(12, 17),
    list_trainers= [
        Trainer(
            name= "Gamin Eddie",
            list_pokémon= [
                Pokémon(pok_id= 23, level= 21)
            ]
        ),
        Trainer(
            name= "Gamin Denden",
            list_pokémon= [
                Pokémon(pok_id= 27, level= 19),
                Pokémon(pok_id= 41, level= 19)
            ]
        ),
        Trainer(
            name= "Gamin Dave",
            list_pokémon= [
                Pokémon(pok_id= 32, level= 18),
                Pokémon(pok_id= 33, level= 18)
            ]
        ),
        Trainer(
            name= "Croupier Dimitri",
            list_pokémon= [
                Pokémon(pok_id= 69, level= 18),
                Pokémon(pok_id= 43, level= 18)
            ]
        ),
        Trainer(
            name= "Mécano Maxence",
            list_pokémon= [
                Pokémon(pok_id= 81, level= 21)
            ]
        ),
        Trainer(
            name= "Croupier Esteban",
            list_pokémon= [
                Pokémon(pok_id= 58, level= 18),
                Pokémon(pok_id= 37, level= 18)
            ]
        ),
        Trainer(
            name= "Gamin Chon",
            list_pokémon= [
                Pokémon(pok_id= 19, level= 17),
                Pokémon(pok_id= 19, level= 17),
                Pokémon(pok_id= 20, level= 17)
            ]
        ),
        Trainer(
            name= "Mécano Bernard",
            list_pokémon= [
                Pokémon(pok_id= 81, level= 18),
                Pokémon(pok_id= 81, level= 18),
                Pokémon(pok_id= 82, level= 18)

            ]
        ),
        Trainer(
            name= "Croupier Ugo",
            list_pokémon= [
                Pokémon(pok_id= 60, level= 18),
                Pokémon(pok_id= 116, level= 18)
            ]
        ),
        Trainer(
            name= "Croupier Clement",
            list_pokémon= [
                Pokémon(pok_id= 100, level= 18),
                Pokémon(pok_id= 81, level= 18)
            ]
        )
    ]
)
road_12 = Road(
    name= "Route 12",
    list_wild_pok_id= [43, 69, 16, 48, 44, 70, 72, 129, 98, 116],
    wild_pok_lvl_range= range (22, 30),
    list_trainers= [
        Trainer(
            name= "Pêcheur Erwan",
            list_pokémon= [
                Pokémon(pok_id= 118, level= 22),
                Pokémon(pok_id= 60, level= 22),
                Pokémon(pok_id= 118, level= 22)
            ]
        ),
        Trainer(
            name= "Pêcheur Alphonse",
            list_pokémon= [
                Pokémon(pok_id= 72, level= 24),
                Pokémon(pok_id= 118, level= 24)
            ]
        ),
        Trainer(
            name= "Pêcheur Serge",
            list_pokémon= [
                Pokémon(pok_id= 118, level= 27)
            ]
        ),
        Trainer(
            name= "Pêcheur Elliot",
            list_pokémon= [
                Pokémon(pok_id= 60, level= 21),
                Pokémon(pok_id= 90, level= 21),
                Pokémon(pok_id= 118, level= 21),
                Pokémon(pok_id= 116, level= 21)
            ]
        ),
        Trainer(
            name= "Rocker Elton",
            list_pokémon= [
                Pokémon(pok_id= 100, level= 29),
                Pokémon(pok_id= 101, level= 29)
            ]
        ),
        Trainer(
            name= "Campeur Justin",
            list_pokémon= [
                Pokémon(pok_id= 32, level= 29),
                Pokémon(pok_id= 33, level= 29)
            ]
        ),
        Trainer(
            name= "Pêcheur Ali",
            list_pokémon= [
                Pokémon(pok_id= 129, level= 24),
                Pokémon(pok_id= 129, level= 24)
            ]
        )
    ])
road_13 = Road(
    name= "Route 13",
    list_wild_pok_id= [43, 69, 48, 16, 17, 44, 70, 132, 72, 129, 98, 116],
    wild_pok_lvl_range= range(22, 29),
    list_trainers= [
        Trainer(
            name= "Pique-Nique Axelle",
            list_pokémon= [
                Pokémon(pok_id= 118, level= 28),
                Pokémon(pok_id= 60, level= 28),
                Pokémon(pok_id= 116, level= 28)
            ]
        ),
        Trainer(
            name= "Ornithologue Sébastien",
            list_pokémon= [
                Pokémon(pok_id= 16, level= 29),
                Pokémon(pok_id= 17, level= 29)
            ]
        ),
        Trainer(
            name= "Pique-Nique Suzy",
            list_pokémon= [
                Pokémon(pok_id= 16, level= 24),
                Pokémon(pok_id= 52, level= 24),
                Pokémon(pok_id= 19, level= 24),
                Pokémon(pok_id= 25, level= 24),
                Pokémon(pok_id= 52, level= 24)
            ]
        ),
        Trainer(
            name= "Canon Léa",
            list_pokémon= [
                Pokémon(pok_id= 19, level= 27),
                Pokémon(pok_id= 25, level= 27),
                Pokémon(pok_id= 19, level= 27)
            ]
        ),
        Trainer(
            name= "Canon Sheila",
            list_pokémon= [
                Pokémon(pok_id= 16, level= 27),
                Pokémon(pok_id= 52, level= 27),
                Pokémon(pok_id= 16, level= 27),
                Pokémon(pok_id= 17, level= 27)
            ]
        ),
        Trainer(
            name= "Ornithologue Pedro",
            list_pokémon= [
                Pokémon(pok_id= 21, level= 25),
                Pokémon(pok_id= 16, level= 25),
                Pokémon(pok_id= 16, level= 25),
                Pokémon(pok_id= 21, level= 25),
                Pokémon(pok_id= 21, level= 25)
            ]
        ),
        Trainer(
            name= "Motard Boris",
            list_pokémon= [
                Pokémon(pok_id= 109, level= 28),
                Pokémon(pok_id= 109, level= 28),
                Pokémon(pok_id= 109, level= 28)
            ]
        ),
        Trainer(
            name= "Ornithologue Bob",
            list_pokémon= [
                Pokémon(pok_id= 16, level= 26),
                Pokémon(pok_id= 17, level= 26),
                Pokémon(pok_id= 21, level= 26),
                Pokémon(pok_id= 22, level= 26)
            ]
        )
    ])
road_14 = Road(
    name= "Route 14",
    list_wild_pok_id= [43, 69, 48, 132, 16, 17, 44, 70],
    wild_pok_lvl_range= range(24, 31),
    list_trainers= [
        Trainer(
            name= "Ornithologue Francis",
            list_pokémon= [
                Pokémon(pok_id= 16, level= 28),
                Pokémon(pok_id= 84, level= 28),
                Pokémon(pok_id= 17, level= 28)
            ]
        ),
        Trainer(
            name= "Ornithologue Mitch",
            list_pokémon= [
                Pokémon(pok_id= 16, level= 26),
                Pokémon(pok_id= 21, level= 26),
                Pokémon(pok_id= 16, level= 26),
                Pokémon(pok_id= 22, level= 26)
            ]
        ),
        Trainer(
            name= "Ornithologue Erik",
            list_pokémon= [
                Pokémon(pok_id= 21, level= 28),
                Pokémon(pok_id= 84, level= 28),
                Pokémon(pok_id= 22, level= 28)
            ]
        ),
        Trainer(
            name= "Ornithologue Ladislas",
            list_pokémon= [
                Pokémon(pok_id= 17, level= 29),
                Pokémon(pok_id= 22, level= 29)
            ]
        ),
        Trainer(
            name= "Ornithologue Donald",
            list_pokémon= [
                Pokémon(pok_id= 83, level= 33)
            ]
        ),
        Trainer(
            name= "Ornithologue Frédo",
            list_pokémon= [
                Pokémon(pok_id= 21, level= 29),
                Pokémon(pok_id= 22, level= 29)
            ]
        ),
        Trainer(
            name= "Motard Gérald",
            list_pokémon= [
                Pokémon(pok_id= 109, level= 29),
                Pokémon(pok_id= 89, level= 29)
            ]
        ),
        Trainer(
            name= "Motard Malik",
            list_pokémon= [
                Pokémon(pok_id= 109, level= 29),
                Pokémon(pok_id= 88, level= 29)
            ]
        ),
        Trainer(
            name= "Motard Isaac",
            list_pokémon= [
                Pokémon(pok_id= 88, level= 28),
                Pokémon(pok_id= 88, level= 28),
                Pokémon(pok_id= 109, level= 28)
            ]
        ),
        Trainer(
            name= "Motard Mathéo",
            list_pokémon= [
                Pokémon(pok_id= 109, level= 26),
                Pokémon(pok_id= 109, level= 26),
                Pokémon(pok_id= 88, level= 26),
                Pokémon(pok_id= 109, level= 26)
            ]
        )
    ])
road_15 = Road(
    name= "Route 15",
    list_wild_pok_id= [43, 69, 16, 48, 17, 44, 70, 132],
    wild_pok_lvl_range= range(24, 31),
    list_trainers= [
        Trainer(
            name= "Pique-Nique Geneviève",
            list_pokémon= [
                Pokémon(pok_id= 25, level= 29),
                Pokémon(pok_id= 26, level= 29)
            ]
        ),
        Trainer(
            name= "Pique-Nique Célia",
            list_pokémon= [
                Pokémon(pok_id=35, level= 33),
            ]
        ),
        Trainer(
            name= "Motard Ernest",
            list_pokémon= [
                Pokémon(pok_id= 109, level= 25),
                Pokémon(pok_id= 109, level= 25),
                Pokémon(pok_id= 110, level= 25),
                Pokémon(pok_id= 109, level= 25),
                Pokémon(pok_id= 88, level= 25)
            ]
        ),
        Trainer(
            name= "Motard Alex",
            list_pokémon= [
                Pokémon(pok_id= 109, level= 28),
                Pokémon(pok_id= 88, level= 28),
                Pokémon(pok_id= 110, level= 28)
            ]
        ),
        Trainer(
            name= "Canon Grace",
            list_pokémon= [
                Pokémon(pok_id= 17, level= 29),
                Pokémon(pok_id= 40, level= 29)
            ]
        ),
        Trainer(
            name= "Canon Olivia",
            list_pokémon= [
                Pokémon(pok_id= 1, level= 29),
                Pokémon(pok_id= 2, level= 29)
            ]
        ),
        Trainer(
            name= "Pique-Nique Selena",
            list_pokémon= [
                Pokémon(pok_id= 44, level= 28),
                Pokémon(pok_id= 43, level= 28),
                Pokémon(pok_id= 43, level= 28)
            ]
        ),
        Trainer(
            name= "Ornithologue Juste",
            list_pokémon= [
                Pokémon(pok_id= 85, level= 28),
                Pokémon(pok_id= 84, level= 28),
                Pokémon(pok_id= 84, level= 28)
            ]
        ),
        Trainer(
            name= "Ornithologue Martin",
            list_pokémon= [
                Pokémon(pok_id= 17, level= 26),
                Pokémon(pok_id= 83, level= 26),
                Pokémon(pok_id= 84, level= 26),
                Pokémon(pok_id= 16, level= 26)
            ]
        ),
        Trainer(
            name= "Pique-Niuqe Jeanne",
            list_pokémon= [
                Pokémon(pok_id= 69, level= 29),
                Pokémon(pok_id= 43, level= 29),
                Pokémon(pok_id= 114, level= 29)
            ]
        )
    ]
)
road_16 = Road(
    name= "Route 16",
    list_trainers= [
        Trainer(
            name= "Motard Layo",
            list_pokémon= [
                Pokémon(pok_id= 88, level= 29),
                Pokémon(pok_id= 109, level= 29),
            ]
        ),
        Trainer(
            name= "Loubard Koji",
            list_pokémon= [
                Pokémon(pok_id= 66, level= 28),
                Pokémon(pok_id= 56, level= 28),
                Pokémon(pok_id= 66, level= 28)
            ]
        ),
        Trainer(
            name= "Loubard Karl",
            list_pokémon= [
                Pokémon(pok_id= 56, level= 29),
                Pokémon(pok_id= 66, level= 29)
            ]
        ),
        Trainer(
            name= "Motard Hideo",
            list_pokémon= [
                Pokémon(pok_id= 110, level= 33)
            ]
        ),
        Trainer(
            name= "Motard Steven",
            list_pokémon= [
                Pokémon(pok_id= 110, level= 28),
                Pokémon(pok_id= 109, level= 28),
                Pokémon(pok_id= 110, level= 28)
            ]
        ),
        Trainer(
            name= "Loubard Yann",
            list_pokémon= [
                Pokémon(pok_id= 56, level= 29),
                Pokémon(pok_id= 66, level= 29)
            ]
        ),
    ]    
)
road_17 = Road(
    name= "Route 17",
    list_trainers= [
         Trainer(
            name= "Motard Virgile",
            list_pokémon= [
                Pokémon(pok_id= 110, level= 28),
                Pokémon(pok_id= 109, level= 28),
                Pokémon(pok_id= 110, level= 28)
            ]
        ),
        Trainer(
            name= "Motard Willy",
            list_pokémon= [
                Pokémon(pok_id= 89, level= 33),
            ]
        ),
        Trainer(
            name= "Loubard Jamal",
            list_pokémon= [
                Pokémon(pok_id= 56, level= 26),
                Pokémon(pok_id= 56, level= 26),
                Pokémon(pok_id= 68, level= 26),
                Pokémon(pok_id= 66, level= 26)
            ]
        ),
        Trainer(
            name= "Motard William",
            list_pokémon= [
                Pokémon(pok_id= 109, level= 25),
                Pokémon(pok_id= 110, level= 25),
                Pokémon(pok_id= 109, level= 25),
                Pokémon(pok_id= 109, level= 25),
                Pokémon(pok_id= 110, level= 25)
            ]
        )
    ]
)
road_18 = Road(
    name= "Route 18",
    list_trainers= [
        Trainer(
            name= "Ornithologue Wilfried",
            list_pokémon= [
                Pokémon(pok_id= 21, level= 29),
                Pokémon(pok_id= 22, level= 29)
            ]
        ),
        Trainer(
            name= "Ornithologue Jacob",
            list_pokémon= [
                Pokémon(pok_id= 21, level= 26),
                Pokémon(pok_id= 21, level= 26),
                Pokémon(pok_id= 22, level= 26),
                Pokémon(pok_id= 21, level= 26)
            ]
        ),
        Trainer(
            name= "Ornithologue Ramiro",
            list_pokémon= [
                Pokémon(pok_id= 85, level= 34)
            ]
        )
    ])
road_19 = Road(
    name= "Route 19",
    list_trainers= [
        Trainer(
            name= "Nageur Richard",
            list_pokémon= [
                Pokémon(pok_id= 72, level= 30),
                Pokémon(pok_id= 90, level= 30)
            ]
        ),
        Trainer(
            name= "Nageur Théo",
            list_pokémon= [
                Pokémon(pok_id= 118, level= 29),
                Pokémon(pok_id= 116, level= 29),
                Pokémon(pok_id= 120, level= 29)
            ]
        ),
        Trainer(
            name= "",
            list_pokémon= [
                Pokémon(pok_id=)
            ]
        )
    ])
road_20 = Road(
    name= "Route 20",
    list_trainers= None)
road_21 = Road(
    name= "Route 21",
    list_trainers= None)
road_22 = Road(
    name= "Route 22",
    list_trainers= None)
road_23 = Road(
    name= "Route 23",
    list_trainers= None)
road_24 = Road(
    name= "Route 24",
    list_trainers= [
        Trainer(
            name= "Scout Aymeric",
            list_pokémon= [
                Pokémon(pok_id= 10, level= 10),
                Pokémon(pok_id= 13, level= 10),
                Pokémon(pok_id= 11, level= 10),
                Pokémon(pok_id= 14, level= 10)
            ]
        ),
        Trainer(
            name= "Fillette Meg",
            list_pokémon= [
                Pokémon(pok_id= 16, level= 12),
                Pokémon(pok_id= 43, level= 12),
                Pokémon(pok_id= 61, level= 12)
            ]
        ),
        Trainer(
            name= "Gamin Tim",
            list_pokémon= [
                Pokémon(pok_id= 27, level= 14),
                Pokémon(pok_id= 23, level= 14)
            ]    
        ),
        Trainer(
            name= "Fillette Lana",
            list_pokémon= [
                Pokémon(pok_id= 32, level= 16),
                Pokémon(pok_id= 29, level= 16)
            ]
        ),
        Trainer(
            name= "Campeur Diego",
            list_pokémon= [
                Pokémon(pok_id= 56, level= 18)
            ]
        ),
        Trainer(
            name=  "Sbire Team Rocket",
            list_pokémon= [
                Pokémon(pok_id= 23, level= 15),
                Pokémon(pok_id= 41, level= 15)
            ]
        )
    ]
)
road_25 = Road(
    name= "Route 25",
    list_trainers= [
        Trainer(
            name= "Montagnard François",
            list_pokémon= [
                Pokémon(pok_id= 66, level= 15),
                Pokémon(pok_id= 74, level= 15)
            ]
        ),
        Trainer(
            name= "Gamin Jo",
            list_pokémon= [
                Pokémon(pok_id= 19, level= 15),
                Pokémon(pok_id= 21, level= 15)
            ]
        ),
        Trainer(
            name= "Montagnard Jeremy",
            list_pokémon= [
                Pokémon(pok_id= 95, level= 17)
            ]
        ),
        Trainer(
            name= "Gamin Dan",
            list_pokémon= [
                Pokémon(pok_id= 79, level= 17)
            ]
        ),
        Trainer(
            name= "Pique-Nique Zora",
            list_pokémon= [
                Pokémon(pok_id= 32, level= 15),
                Pokémon(pok_id= 29, level= 15)
            ]
        ),
        Trainer(
            name= "Montagnard Hiro",
            list_pokémon= [
                Pokémon(pok_id= 74, level= 13),
                Pokémon(pok_id= 74, level= 13),
                Pokémon(pok_id= 74, level= 13),
                Pokémon(pok_id= 66, level= 13)
            ]
        ),
        Trainer(
            name= "Campeur Frédéric",
            list_pokémon= [
                Pokémon(pok_id= 19, level= 14),
                Pokémon(pok_id= 23, level= 14)
            ]
        ),
        Trainer(
            name= "Gamin Cedric",
            list_pokémon= [
                Pokémon(pok_id= 23, level= 14),
                Pokémon(pok_id= 27, level= 14)
            ]
        ),
        Trainer(
            name= "Fillette Aude",
            list_pokémon= [
                Pokémon(pok_id= 43, level= 13),
                Pokémon(pok_id= 16, level= 13),
                Pokémon(pok_id= 43, level= 13)
            ]
        )
    ]
)
azuria_to_carmin = Road(
    name="Chemin express Azuria/Carmin sur Mer",
    list_wild_pok_id= None,
    wild_pok_lvl_range= None,
    list_trainers= None
)


relation_map_dict = {
    bourg_palette: [road_1, road_21],
    jadielle: [road_2, road_22, road_1],
    foret_de_jade: [argenta, road_2],
    argenta: [road_3, foret_de_jade],
    mont_selenite: [road_4, road_3], 
    azuria: [road_5, road_9, road_24],
    azuria_to_carmin: [road_5, road_6],
    carmin_sur_mer: [road_11, océane, road_6],
    océane: [carmin_sur_mer],
    safrania: [dojo, sylphe_sarl, road_5, road_6, road_7, road_8],
    grotte: [road_10, road_9],
    lavanvile: [tour_pokémon, road_8, road_12],
    tour_pokémon: [lavanvile],
    cave_taupiqueur: [foret_de_jade],
    parmanie: [parc_safari, road_18, road_19, road_15],
    parc_safari: [parmanie],
    céladopole: [road_16, casino, road_7],
    casino: [céladopole],
    dojo: [safrania],
    sylphe_sarl: [safrania],
    iles_écumes: [road_20, road_19],
    cramois_ile: [manoir_pokémon, road_21, road_20],
    route_victoire: [plateau_indigo, road_23],
    plateau_indigo: [route_victoire],
    road_1: [jadielle, bourg_palette],
    road_2: [foret_de_jade, jadielle],
    road_3: [mont_selenite, argenta],
    road_4: [azuria, mont_selenite],
    road_5: [safrania, azuria_to_carmin, azuria],
    road_6: [carmin_sur_mer, azuria_to_carmin, safrania],
    road_7: [céladopole, safrania],
    road_8: [lavanvile, safrania],
    road_9: [grotte, azuria],
    road_10: [lavanvile, grotte],
    road_11: [cave_taupiqueur, road_12, carmin_sur_mer],
    road_12: [road_13, road_11, lavanvile],
    road_13: [road_14, road_12],
    road_14: [road_15, road_13],
    road_15: [parmanie, road_14],
    road_16: [road_17, céladopole],
    road_17: [road_18, road_16],
    road_18: [parmanie, road_17],
    road_19: [iles_écumes, parmanie],
    road_20: [cramois_ile, iles_écumes],
    road_21: [bourg_palette, cramois_ile],
    road_22: [road_23, jadielle],
    road_23: [route_victoire, road_22],
    road_24: [road_25, grotte_azurée, azuria],
    road_25: [road_24],
    }

def creation_player():
    print("Hello and welcome to my Python made Pokémon 1st generation!")
    sleep(2)
    print("First of all, you need a name!")
    sleep(1)
    name = input("What is your character's name?\n")
    sleep(1)
    return Player(name= name, list_pokémon= [])

def where_to_go(position):
    while True:
        counter = 1
        print("Destination available: ")
        for destination in relation_map_dict[position]:
            print(f"{counter}| {destination.name}")
            counter += 1
        choice = input("Enter the number coresponding where you want to go or type 'c' to cancel : ")
        if choice == "cancel" or choice == "c":
            return position
        try:
            choice_int = int(choice)
        except ValueError:
            continue
        if choice_int > 0 and choice_int <= len(relation_map_dict[position]):
            return relation_map_dict[position][choice_int -1]

def game_loop(player: Player):
    where_i_am = bourg_palette
    while True:
        where_i_am.roaming(player= player)
        if type(where_i_am) == End and End.pokémon_master_defeated:
            break
        where_i_am = where_to_go(position= where_i_am)
    clearscreen()
                
clearscreen()
player = creation_player()
game_loop(player= player)
print("Congratulation, You have defeated the Game!")
sleep(10)


