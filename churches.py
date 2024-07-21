"""
Ephesus
Smyrna
Pergamos (also known as Pergamum)
Thyatira
Sardis
Philadelphia
Laodicea
"""


from church import *

ephesus = Church(
    name="Ephesus",
    location="Asia Minor",
    christ_self_description=ChristSelfDescription(
        divine_attributes=[],
        symbolic_imagery=[SymbolicImagery.STARS, SymbolicImagery.LAMPSTANDS],
        actions=[Action.HOLDS, Action.WALKS],
        christological_titles=[],
        redemptive_work=[]
    ),
    commendations=[
        Commendation(
            category=CommendationCategory.PERSEVERANCE,
            specific_commendation=SpecificCommendation.PATIENT_ENDURANCE,
            description="I know thy works, and thy labour, and thy patience"
        ),
        Commendation(
            category=CommendationCategory.RESISTANCE_TO_EVIL,
            specific_commendation=SpecificCommendation.INTOLERANCE_OF_EVIL,
            description="thou canst not bear them which are evil"
        ),
        Commendation(
            category=CommendationCategory.DOCTRINAL_INTEGRITY,
            specific_commendation=SpecificCommendation.TESTING_FALSE_APOSTLES,
            description="thou hast tried them which say they are apostles, and are not, and hast found them liars"
        ),
        Commendation(
            category=CommendationCategory.PERSEVERANCE,
            specific_commendation=SpecificCommendation.ENDURANCE_IN_SUFFERING,
            description="And hast borne, and hast patience, and for my name's sake hast laboured, and hast not fainted"
        )
    ],
    criticisms=[
        Criticism(
            category=CriticismCategory.SPIRITUAL_DECLINE,
            specific_criticism=SpecificCriticism.LOST_FIRST_LOVE,
            description="Nevertheless I have somewhat against thee, because thou hast left thy first love"
        )
    ],
    exhortation=Exhortation(
        category=ExhortationCategory.REPENTANCE,
        specific_exhortation=SpecificExhortation.REMEMBER_AND_REPENT,
        description="Remember therefore from whence thou art fallen, and repent, and do the first works"
    ),
    promise_to_overcomers=Promise(
        category=PromiseCategory.SPIRITUAL_NOURISHMENT,
        specific_promise=SpecificPromise.ACCESS_TO_TREE_OF_LIFE,
        description="To him that overcometh will I give to eat of the tree of life, which is in the midst of the paradise of God"
    ),
    spiritual_state=SpiritualState.MIXED,
    main_challenge=Challenge(
        category=ChallengeCategory.SPIRITUAL_STAGNATION,
        specific_challenge=SpecificChallenge.LOSS_OF_FERVOR,
        description="Left their first love, indicating a cooling of their initial passion and devotion"
    )
)

smyrna = Church(
    name="Smyrna",
    location="Asia Minor",
    christ_self_description=ChristSelfDescription(
        divine_attributes=[DivineName.FIRST, DivineName.LAST],
        symbolic_imagery=[],
        actions=[],
        christological_titles=[],
        redemptive_work=[RedemptiveWork.DIED, RedemptiveWork.CAME_TO_LIFE]
    ),
    commendations=[
        Commendation(
            category=CommendationCategory.PERSEVERANCE,
            specific_commendation=SpecificCommendation.ENDURANCE_IN_SUFFERING,
            description="I know thy works, and tribulation, and poverty"
        ),
        Commendation(
            category=CommendationCategory.SPIRITUAL_GROWTH,
            specific_commendation=SpecificCommendation.SPIRITUAL_RICHNESS,
            description="(but thou art rich)"
        )
    ],
    criticisms=[],  # No criticisms mentioned for Smyrna
    exhortation=Exhortation(
        category=ExhortationCategory.PERSEVERANCE,
        specific_exhortation=SpecificExhortation.REMAIN_FAITHFUL,
        description="Fear none of those things which thou shalt suffer... be thou faithful unto death"
    ),
    promise_to_overcomers=Promise(
        category=PromiseCategory.ETERNAL_LIFE,
        specific_promise=SpecificPromise.CROWN_OF_LIFE,
        description="I will give thee a crown of life"
    ),
    spiritual_state=SpiritualState.THRIVING,
    main_challenge=Challenge(
        category=ChallengeCategory.EXTERNAL_PRESSURE,
        specific_challenge=SpecificChallenge.PERSECUTION,
        description="Facing tribulation, poverty, and slander from those who claim to be Jews"
    )
)

pergamos = Church(
    name="Pergamos",
    location="Asia Minor",
    christ_self_description=ChristSelfDescription(
        divine_attributes=[],
        symbolic_imagery=[SymbolicImagery.EYES_OF_FIRE],
        actions=[Action.HAS],
        christological_titles=[],
        redemptive_work=[]
    ),
    commendations=[
        Commendation(
            category=CommendationCategory.FAITH,
            specific_commendation=SpecificCommendation.STRONG_FAITH,
            description="thou holdest fast my name, and hast not denied my faith"
        ),
        Commendation(
            category=CommendationCategory.PERSEVERANCE,
            specific_commendation=SpecificCommendation.ENDURANCE_IN_SUFFERING,
            description="even in those days wherein Antipas was my faithful martyr, who was slain among you"
        )
    ],
    criticisms=[
        Criticism(
            category=CriticismCategory.DOCTRINAL_ERROR,
            specific_criticism=SpecificCriticism.TOLERATING_FALSE_TEACHING,
            description="thou hast there them that hold the doctrine of Balaam"
        ),
        Criticism(
            category=CriticismCategory.MORAL_FAILURE,
            specific_criticism=SpecificCriticism.SEXUAL_IMMORALITY,
            description="to eat things sacrificed unto idols, and to commit fornication"
        ),
        Criticism(
            category=CriticismCategory.DOCTRINAL_ERROR,
            specific_criticism=SpecificCriticism.FOLLOWING_FALSE_DOCTRINES,
            description="So hast thou also them that hold the doctrine of the Nicolaitanes, which thing I hate"
        )
    ],
    exhortation=Exhortation(
        category=ExhortationCategory.REPENTANCE,
        specific_exhortation=SpecificExhortation.TURN_FROM_SIN,
        description="Repent; or else I will come unto thee quickly, and will fight against them with the sword of my mouth"
    ),
    promise_to_overcomers=Promise(
        category=PromiseCategory.SPIRITUAL_NOURISHMENT,
        specific_promise=SpecificPromise.HIDDEN_MANNA,
        description="To him that overcometh will I give to eat of the hidden manna"
    ),
    spiritual_state=SpiritualState.MIXED,
    main_challenge=Challenge(
        category=ChallengeCategory.CULTURAL_ASSIMILATION,
        specific_challenge=SpecificChallenge.WORLDLINESS,
        description="Tolerating false teachings and immoral practices, possibly due to pressure from the surrounding culture"
    )
)

thyatira = Church(
    name="Thyatira",
    location="Asia Minor",
    christ_self_description=ChristSelfDescription(
        divine_attributes=[],
        symbolic_imagery=[SymbolicImagery.EYES_OF_FIRE, SymbolicImagery.FEET_OF_BRONZE],
        actions=[],
        christological_titles=[ChristologicalTitle.SON_OF_GOD],
        redemptive_work=[]
    ),
    commendations=[
        Commendation(
            category=CommendationCategory.LOVE,
            specific_commendation=SpecificCommendation.LOVE_FOR_OTHERS,
            description="I know thy works, and charity"
        ),
        Commendation(
            category=CommendationCategory.SERVICE,
            specific_commendation=SpecificCommendation.ACTIVE_MINISTRY,
            description="and service"
        ),
        Commendation(
            category=CommendationCategory.FAITH,
            specific_commendation=SpecificCommendation.STRONG_FAITH,
            description="and faith"
        ),
        Commendation(
            category=CommendationCategory.PERSEVERANCE,
            specific_commendation=SpecificCommendation.PATIENT_ENDURANCE,
            description="and thy patience"
        ),
        Commendation(
            category=CommendationCategory.SPIRITUAL_GROWTH,
            specific_commendation=SpecificCommendation.INCREASING_GOOD_DEEDS,
            description="and thy works; and the last to be more than the first"
        )
    ],
    criticisms=[
        Criticism(
            category=CriticismCategory.DOCTRINAL_ERROR,
            specific_criticism=SpecificCriticism.TOLERATING_FALSE_TEACHING,
            description="thou sufferest that woman Jezebel, which calleth herself a prophetess, to teach"
        ),
        Criticism(
            category=CriticismCategory.MORAL_FAILURE,
            specific_criticism=SpecificCriticism.SEXUAL_IMMORALITY,
            description="to seduce my servants to commit fornication"
        ),
        Criticism(
            category=CriticismCategory.MORAL_FAILURE,
            specific_criticism=SpecificCriticism.IDOLATRY,
            description="and to eat things sacrificed unto idols"
        )
    ],
    exhortation=Exhortation(
        category=ExhortationCategory.PERSEVERANCE,
        specific_exhortation=SpecificExhortation.HOLD_FAST,
        description="But unto you I say, and unto the rest in Thyatira, as many as have not this doctrine... That which ye have already hold fast till I come"
    ),
    promise_to_overcomers=Promise(
        category=PromiseCategory.AUTHORITY,
        specific_promise=SpecificPromise.AUTHORITY_OVER_NATIONS,
        description="And he that overcometh, and keepeth my works unto the end, to him will I give power over the nations"
    ),
    spiritual_state=SpiritualState.MIXED,
    main_challenge=Challenge(
        category=ChallengeCategory.SPIRITUAL_DECEPTION,
        specific_challenge=SpecificChallenge.FALSE_PROPHETS,
        description="Tolerating false teaching from 'Jezebel', who claims to be a prophetess"
    )
)

sardis = Church(
    name="Sardis",
    location="Asia Minor",
    christ_self_description=ChristSelfDescription(
        divine_attributes=[],
        symbolic_imagery=[SymbolicImagery.STARS],
        actions=[Action.HAS],
        christological_titles=[],
        redemptive_work=[]
    ),
    commendations=[
        Commendation(
            category=CommendationCategory.FAITH,
            specific_commendation=SpecificCommendation.FAITHFUL_REMNANT,
            description="Thou hast a few names even in Sardis which have not defiled their garments"
        )
    ],
    criticisms=[
        Criticism(
            category=CriticismCategory.SPIRITUAL_DECLINE,
            specific_criticism=SpecificCriticism.SPIRITUAL_DEATH,
            description="I know thy works, that thou hast a name that thou livest, and art dead"
        ),
        Criticism(
            category=CriticismCategory.COMPLACENCY,
            specific_criticism=SpecificCriticism.INCOMPLETE_WORKS,
            description="I have not found thy works perfect before God"
        )
    ],
    exhortation=Exhortation(
        category=ExhortationCategory.VIGILANCE,
        specific_exhortation=SpecificExhortation.BE_WATCHFUL,
        description="Be watchful, and strengthen the things which remain, that are ready to die"
    ),
    promise_to_overcomers=Promise(
        category=PromiseCategory.HEAVENLY_REWARD,
        specific_promise=SpecificPromise.WHITE_GARMENTS,
        description="He that overcometh, the same shall be clothed in white raiment"
    ),
    spiritual_state=SpiritualState.STRUGGLING,
    main_challenge=Challenge(
        category=ChallengeCategory.SPIRITUAL_STAGNATION,
        specific_challenge=SpecificChallenge.COMPLACENCY,
        description="Having a reputation of being alive, but actually being spiritually dead"
    )
)


philadelphia = Church(
    name="Philadelphia",
    location="Asia Minor",
    christ_self_description=ChristSelfDescription(
        divine_attributes=[DivineName.HOLY, DivineName.TRUE],
        symbolic_imagery=[],
        actions=[Action.HOLDS],
        christological_titles=[],
        redemptive_work=[]
    ),
    commendations=[
        Commendation(
            category=CommendationCategory.PERSEVERANCE,
            specific_commendation=SpecificCommendation.PATIENT_ENDURANCE,
            description="thou hast kept the word of my patience"
        ),
        Commendation(
            category=CommendationCategory.FAITH,
            specific_commendation=SpecificCommendation.STRONG_FAITH,
            description="and hast not denied my name"
        ),
        Commendation(
            category=CommendationCategory.OBEDIENCE,
            specific_commendation=SpecificCommendation.KEEPING_GODS_WORD,
            description="thou hast kept my word"
        )
    ],
    criticisms=[],  # No criticisms mentioned for Philadelphia
    exhortation=Exhortation(
        category=ExhortationCategory.PERSEVERANCE,
        specific_exhortation=SpecificExhortation.HOLD_FAST,
        description="Behold, I come quickly: hold that fast which thou hast, that no man take thy crown"
    ),
    promise_to_overcomers=Promise(
        category=PromiseCategory.DIVINE_RECOGNITION,
        specific_promise=SpecificPromise.PILLAR_IN_GODS_TEMPLE,
        description="Him that overcometh will I make a pillar in the temple of my God, and he shall go no more out"
    ),
    spiritual_state=SpiritualState.THRIVING,
    main_challenge=Challenge(
        category=ChallengeCategory.EXTERNAL_PRESSURE,
        specific_challenge=SpecificChallenge.PERSECUTION,
        description="Facing opposition from 'those who are of the synagogue of Satan, who claim to be Jews though they are not'"
    )
)


laodicea = Church(
    name="Laodicea",
    location="Asia Minor",
    christ_self_description=ChristSelfDescription(
        divine_attributes=[],
        symbolic_imagery=[],
        actions=[],
        christological_titles=[ChristologicalTitle.AMEN, ChristologicalTitle.FAITHFUL_WITNESS],
        redemptive_work=[]
    ),
    commendations=[],  # No commendations mentioned for Laodicea
    criticisms=[
        Criticism(
            category=CriticismCategory.SPIRITUAL_DECLINE,
            specific_criticism=SpecificCriticism.LUKEWARM_FAITH,
            description="I know thy works, that thou art neither cold nor hot: I would thou wert cold or hot"
        ),
        Criticism(
            category=CriticismCategory.COMPLACENCY,
            specific_criticism=SpecificCriticism.SELF_SATISFACTION,
            description="Because thou sayest, I am rich, and increased with goods, and have need of nothing"
        ),
        Criticism(
            category=CriticismCategory.SPIRITUAL_BLINDNESS,
            specific_criticism=SpecificCriticism.LACK_OF_SELF_AWARENESS,
            description="and knowest not that thou art wretched, and miserable, and poor, and blind, and naked"
        )
    ],
    exhortation=Exhortation(
        category=ExhortationCategory.SPIRITUAL_GROWTH,
        specific_exhortation=SpecificExhortation.SEEK_SPIRITUAL_RICHES,
        description="I counsel thee to buy of me gold tried in the fire, that thou mayest be rich; and white raiment, that thou mayest be clothed, and that the shame of thy nakedness do not appear; and anoint thine eyes with eyesalve, that thou mayest see"
    ),
    promise_to_overcomers=Promise(
        category=PromiseCategory.INTIMACY_WITH_GOD,
        specific_promise=SpecificPromise.SIT_WITH_CHRIST_ON_THRONE,
        description="To him that overcometh will I grant to sit with me in my throne, even as I also overcame, and am set down with my Father in his throne"
    ),
    spiritual_state=SpiritualState.STRUGGLING,
    main_challenge=Challenge(
        category=ChallengeCategory.SPIRITUAL_STAGNATION,
        specific_challenge=SpecificChallenge.COMPLACENCY,
        description="Self-satisfaction and lukewarmness leading to spiritual blindness and poverty"
    )
)