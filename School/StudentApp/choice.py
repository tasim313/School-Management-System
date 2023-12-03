from django.db import models


class Gender(models.TextChoices):
    FEMALE = "female", "Female"
    MALE = "male", "Male"
    OTHERS = "others", "Others"


class BloodGroup(models.TextChoices):
    A_POSITIVE = 'A+', 'A Positive'
    A_NEGATIVE = 'A-', 'A Negative'
    B_POSITIVE = 'B+', 'B Positive'
    B_NEGATIVE = 'B-', 'B Negative'
    AB_POSITIVE = 'AB+', 'AB Positive'
    AB_NEGATIVE = 'AB-', 'AB Negative'
    O_POSITIVE = 'O+', 'O Positive'
    O_NEGATIVE = 'O-', 'O Negative'


class Religion(models.TextChoices):
    ISLAM = 'Islam', 'Islam'
    CHRISTIANITY = 'Christianity', 'Christianity'
    HINDUISM = 'Hinduism', 'Hinduism'
    BUDDHISM = 'Buddhism', 'Buddhism'
    JUDAISM = 'Judaism', 'Judaism'
    SIKHISM = 'Sikhism', 'Sikhism'
    OTHER = 'Other', 'Other'


class FatherStatus(models.TextChoices):
    ALIVE = 'alive', 'Alive'
    DECEASED = 'deceased', 'Deceased'
    UNKNOWN = 'unknown', 'Unknown'


class MotherStatus(models.TextChoices):
    ALIVE = 'alive', 'Alive'
    DECEASED = 'deceased', 'Deceased'
    UNKNOWN = 'unknown', 'Unknown'


class MaritalStatus(models.TextChoices):
    MARRIED = 'married', 'Married'
    UNMARRIED = 'unmarried', 'Unmarried'
    WIDOWED = 'widowed', 'Widowed'
    CUSTOM = 'custom', 'Custom (বিপত্নীক etc.)'


class DisabilityStatus(models.TextChoices):
    NO_DISABILITY = 'no_disability', 'No Disability'
    VISUAL_IMPAIRMENT = 'visual_impairment', 'Visual Impairment'
    HEARING_IMPAIRMENT = 'hearing_impairment', 'Hearing Impairment'
    MOBILITY_IMPAIRMENT = 'mobility_impairment', 'Mobility Impairment'
    OTHER = 'other', 'Other (Specify)'


class EthnicGroup(models.TextChoices):
    BENGALI = 'bengali', 'Bengali'
    CHAKMA = 'chakma', 'Chakma'
    GARO = 'garo', 'Garo'
    MARMA = 'marma', 'Marma'
    SANTAL = 'santal', 'Santal'
    RAKHINE = 'rakhine', 'Rakhine'
    BAWM = 'bawm', 'Bawm'
    MRO = 'mro', 'Mro'
    MIZO = 'mizo', 'Mizo'
    TRIPURI = 'tripuri', 'Tripuri'
    OTHER = 'other', 'Other (Specify)'


from django.db import models

class GuardianStatus(models.TextChoices):
    GRANDFATHER = 'grandfather', 'Grandfather'
    GRANDMOTHER = 'grandmother', 'Grandmother'
    BROTHER = 'brother', 'Brother'
    UNCLE = 'uncle', 'Uncle'
    BROTHER_IN_LAW = 'brother_in_law', 'Brother-in-law'
    SISTER = 'sister', 'Sister'
    SISTER_IN_LAW = 'sister_in_law', 'Sister-in-law'
    LEGAL_GUARDIAN = 'legal_guardian', 'Legal Guardian'
    OTHER = 'other', 'Other (Specify)'
