from enum import Enum


Regime = Enum(
    value='Regime',
    names=[
        ("ZONE 30", 1),
        ("ZONE_30", 1),
        ("AIRE PIETONNE", 2),
        ("AIRE_PIETONNE", 2),
        ("ZONE DE RENCONTRE", 3),
        ("ZONE_DE_RENCONTRE", 3),
        ("EN AGGLOMERATION", 4),
        ("EN_AGGLOMERATION", 4),
        ("HORS AGGLOMERATION", 5),
        ("HORS_AGGLOMERATION", 5),
        ("AUTRE", 6),
    ])

Amenagement = Enum(
    value='Amenagement',
    names=[
        ("PISTE CYCLABLE", 1),
        ("PISTE_CYCLABLE", 1),
        ("BANDE CYCLABLE", 2),
        ("BANDE_CYCLABLE", 2),
        ("DOUBLE SENS CYCLABLE PISTE", 3),
        ("DOUBLE_SENS_CYCLABLE_PISTE", 3),
        ("DOUBLE SENS CYCLABLE BANDE", 4),
        ("DOUBLE_SENS_CYCLABLE_BANDE", 4),
        ("DOUBLE SENS CYCLABLE NON MATERIALISE", 5),
        ("DOUBLE_SENS_CYCLABLE_NON_MATERIALISE", 5),
        ("VOIE VERTE", 6),
        ("VOIE_VERTE", 6),
        ("VELO RUE", 7),
        ("VELO_RUE", 7),
        ("COULOIR BUS+VELO", 8),
        ("COULOIR_BUS_VELO", 8),
        ("RAMPE", 9),
        ("GOULOTTE", 10),
        ("AMENAGEMENT MIXTE PIETON VELO HORS VOIE VERTE", 11),
        ("AMENAGEMENT_MIXTE_PIETON_VELO_HORS_VOIE_VERTE", 11),
        ("CHAUSSEE A VOIE CENTRALE BANALISEE", 12),
        ("CHAUSSEE_A_VOIE_CENTRALE_BANALISEE", 12),
        ("ACCOTEMENT REVETU HORS CVCB", 13),
        ("ACCOTEMENT_REVETU_HORS_CVCB", 13),
        ("AUCUN", 14),
        ("AUTRE", 15),
    ]
)


class Revetement(Enum):
    LISSE = "LISSE"
    RUGUEUX = "RUGUEUX"
    MEUBLE = "MEUBLE"


Statut = Enum(value='Statut', names=[
    ("EN TRAVAUX", 1),
    ("EN_TRAVAUX", 1),
    ("EN SERVICE", 2),
    ("EN_SERVICE", 2),
    ("PROVISOIRE", 3),
])


class Emplacement(Enum):
    TROTTOIR = "TROTTOIR"
    INTERMEDIAIRE = "INTERMEDIAIRE"
    CHAUSSEE = "CHAUSSEE"


class Sens(Enum):
    UNIDIRECTIONNEL = "UNIDIRECTIONNEL"
    BIDIRECTIONNEL = "BIDIRECTIONNEL"


Acces = Enum(value='Acces', names=[
    ("ROLLER", 1),
    ("VELO DE ROUTE", 2),
    ("VELO_DE_ROUTE", 2),
    ("VTC", 3),
    ("VTT", 4),
])
