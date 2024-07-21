from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional

class SpiritualState(Enum):
    THRIVING = auto()
    MIXED = auto()
    STRUGGLING = auto()

class DivineName(Enum):
    BEGINNING = auto()
    END = auto()
    FIRST = auto()
    LAST = auto()
    ALL_SEEING = auto()
    ALL_KNOWING = auto()
    ALMIGHTY = auto()
    CREATOR = auto()
    HOLY = auto()
    TRUE = auto()
    RULER = auto()
    JUDGE = auto()

class SymbolicImagery(Enum):
    STARS = auto()
    MORNING_STAR = auto()
    LAMPSTANDS = auto()
    KEY = auto()
    EYES_OF_FIRE = auto()
    FEET_OF_BRONZE = auto()
    VOICE_OF_WATERS = auto()

class Action(Enum):
    WALKS = auto()
    STANDS = auto()
    HOLDS = auto()
    HAS = auto()

class ChristologicalTitle(Enum):
    SON_OF_GOD = auto()
    ALPHA_AND_OMEGA = auto()
    AMEN = auto()
    FAITHFUL_WITNESS = auto()

class RedemptiveWork(Enum):
    DIED = auto()
    CAME_TO_LIFE = auto()
    LIVING_ONE = auto()

@dataclass
class ChristSelfDescription:
    divine_attributes: List[DivineName]
    symbolic_imagery: List[SymbolicImagery]
    actions: List[Action]
    christological_titles: List[ChristologicalTitle]
    redemptive_work: List[RedemptiveWork]

class CommendationCategory(Enum):
    FAITH = auto()
    PERSEVERANCE = auto()
    LOVE = auto()
    SERVICE = auto()
    DOCTRINAL_INTEGRITY = auto()
    SPIRITUAL_GROWTH = auto()
    RESISTANCE_TO_EVIL = auto()
    OBEDIENCE = auto()

class SpecificCommendation(Enum):
    # Faith category
    STRONG_FAITH = auto()
    UNWAVERING_BELIEF = auto()

    # Perseverance category
    ENDURANCE_IN_SUFFERING = auto()
    PATIENT_ENDURANCE = auto()
    STEADFASTNESS = auto()

    # Love category
    LOVE_FOR_GOD = auto()
    LOVE_FOR_OTHERS = auto()

    # Service category
    DILIGENT_WORK = auto()
    ACTIVE_MINISTRY = auto()

    # Doctrinal Integrity category
    DOCTRINAL_PURITY = auto()
    RESISTING_FALSE_TEACHING = auto()

    # Spiritual Growth category
    INCREASING_GOOD_DEEDS = auto()
    SPIRITUAL_RICHNESS = auto()

    # Resistance to Evil category
    INTOLERANCE_OF_EVIL = auto()
    TESTING_FALSE_APOSTLES = auto()
    RESISTING_CULTURAL_PRESSURE = auto()

    FAITHFUL_REMNANT = auto()
    KEEPING_GODS_WORD = auto()

@dataclass
class Commendation:
    category: CommendationCategory
    specific_commendation: SpecificCommendation
    description: Optional[str] = None

class CriticismCategory(Enum):
    SPIRITUAL_DECLINE = auto()
    DOCTRINAL_ERROR = auto()
    MORAL_FAILURE = auto()
    LACK_OF_DISCERNMENT = auto()
    COMPLACENCY = auto()
    LACK_OF_LOVE = auto()
    COMPROMISE = auto()
    SPIRITUAL_BLINDNESS = auto()

class SpecificCriticism(Enum):
    # Spiritual Decline category
    LOST_FIRST_LOVE = auto()
    SPIRITUAL_DEATH = auto()
    LUKEWARM_FAITH = auto()

    # Doctrinal Error category
    TOLERATING_FALSE_TEACHING = auto()
    FOLLOWING_FALSE_DOCTRINES = auto()

    # Moral Failure category
    SEXUAL_IMMORALITY = auto()
    IDOLATRY = auto()

    # Lack of Discernment category
    ACCEPTING_FALSE_APOSTLES = auto()
    FOLLOWING_FALSE_PROPHETS = auto()

    # Complacency category
    SELF_SATISFACTION = auto()
    INCOMPLETE_WORKS = auto()

    # Lack of Love category
    DIMINISHED_LOVE = auto()
    LACK_OF_BROTHERLY_LOVE = auto()

    # Compromise category
    WORLDLY_COMPROMISE = auto()
    TOLERATING_SIN = auto()

    LACK_OF_SELF_AWARENESS = auto()

@dataclass
class Criticism:
    category: CriticismCategory
    specific_criticism: SpecificCriticism
    description: Optional[str] = None

class ExhortationCategory(Enum):
    REPENTANCE = auto()
    PERSEVERANCE = auto()
    SPIRITUAL_GROWTH = auto()
    DOCTRINAL_PURITY = auto()
    VIGILANCE = auto()
    RECOMMITMENT = auto()
    BOLDNESS = auto()

class SpecificExhortation(Enum):
    # Repentance category
    REMEMBER_AND_REPENT = auto()
    TURN_FROM_SIN = auto()

    # Perseverance category
    HOLD_FAST = auto()
    REMAIN_FAITHFUL = auto()
    ENDURE_SUFFERING = auto()

    # Spiritual Growth category
    STRENGTHEN_WHAT_REMAINS = auto()
    REKINDLE_LOVE = auto()
    SEEK_SPIRITUAL_RICHES = auto()

    # Doctrinal Purity category
    REJECT_FALSE_TEACHING = auto()
    MAINTAIN_SOUND_DOCTRINE = auto()

    # Vigilance category
    STAY_ALERT = auto()
    BE_WATCHFUL = auto()

    # Recommitment category
    RETURN_TO_FIRST_WORKS = auto()
    RENEW_COMMITMENT = auto()

    # Boldness category
    OPEN_THE_DOOR = auto()
    OVERCOME_FEAR = auto()

@dataclass
class Exhortation:
    category: ExhortationCategory
    specific_exhortation: SpecificExhortation
    description: Optional[str] = None

class PromiseCategory(Enum):
    ETERNAL_LIFE = auto()
    DIVINE_PROTECTION = auto()
    SPIRITUAL_NOURISHMENT = auto()
    HEAVENLY_REWARD = auto()
    DIVINE_RECOGNITION = auto()
    AUTHORITY = auto()
    INTIMACY_WITH_GOD = auto()

class SpecificPromise(Enum):
    # Eternal Life category
    ACCESS_TO_TREE_OF_LIFE = auto()
    IMMUNITY_FROM_SECOND_DEATH = auto()

    # Divine Protection category
    PROTECTION_FROM_SECOND_DEATH = auto()
    KEPT_FROM_HOUR_OF_TRIAL = auto()

    # Spiritual Nourishment category
    HIDDEN_MANNA = auto()

    # Heavenly Reward category
    CROWN_OF_LIFE = auto()
    MORNING_STAR = auto()
    WHITE_GARMENTS = auto()

    # Divine Recognition category
    NEW_NAME = auto()
    NAME_ACKNOWLEDGED_BEFORE_GOD = auto()
    PILLAR_IN_GODS_TEMPLE = auto()

    # Authority category
    AUTHORITY_OVER_NATIONS = auto()
    SIT_WITH_CHRIST_ON_THRONE = auto()

    # Intimacy with God category
    DINE_WITH_CHRIST = auto()

@dataclass
class Promise:
    category: PromiseCategory
    specific_promise: SpecificPromise
    description: Optional[str] = None

class ChallengeCategory(Enum):
    EXTERNAL_PRESSURE = auto()
    INTERNAL_CONFLICT = auto()
    SPIRITUAL_STAGNATION = auto()
    DOCTRINAL_CORRUPTION = auto()
    MORAL_DECAY = auto()
    CULTURAL_ASSIMILATION = auto()
    SPIRITUAL_DECEPTION = auto()

class SpecificChallenge(Enum):
    # External Pressure category
    PERSECUTION = auto()
    ECONOMIC_HARDSHIP = auto()
    SOCIAL_OSTRACISM = auto()

    # Internal Conflict category
    LEADERSHIP_DISPUTES = auto()
    FACTIONAL_DIVISION = auto()

    # Spiritual Stagnation category
    LOSS_OF_FERVOR = auto()
    COMPLACENCY = auto()
    SPIRITUAL_LAZINESS = auto()

    # Doctrinal Corruption category
    FALSE_TEACHING = auto()
    HERETICAL_INFLUENCES = auto()

    # Moral Decay category
    SEXUAL_IMMORALITY = auto()
    IDOLATRY = auto()
    ETHICAL_COMPROMISE = auto()

    # Cultural Assimilation category
    WORLDLINESS = auto()
    SYNCRETISM = auto()

    # Spiritual Deception category
    FALSE_PROPHETS = auto()
    SELF_DECEPTION = auto()

@dataclass
class Challenge:
    category: ChallengeCategory
    specific_challenge: SpecificChallenge
    description: Optional[str] = None

@dataclass
class Church:
    name: str
    location: str
    christ_self_description: ChristSelfDescription
    commendations: List[Commendation]
    criticisms: List[Criticism]
    exhortation: Exhortation
    promise_to_overcomers: Promise
    spiritual_state: SpiritualState
    main_challenge: Challenge