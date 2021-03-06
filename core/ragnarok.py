class Ragnarok(object):
    classes = {
        0: 'Novice',
        1: 'Swordsman',
        2: 'Mage',
        3: 'Archer',
        4: 'Acolyte',
        5: 'Merchant',
        6: 'Thief',
        7: 'Knight',
        8: 'Priest',
        9: 'Wizard',
        10: 'Blacksmith',
        11: 'Hunter',
        12: 'Assassin',
        14: 'Crusader',
        15: 'Monk',
        16: 'Sage',
        17: 'Rogue',
        18: 'Alchemist',
        19: 'Bard',
        20: 'Dancer',
        23: 'Super Novice',
        24: 'Gunslinger',
        25: 'Ninja',
        4001: 'Novice High',
        4002: 'Swordman High',
        4003: 'Mage High',
        4004: 'Archer High',
        4005: 'Acolyte High',
        4006: 'Merchant High',
        4007: 'Thief High',
        4008: 'Lord Knight',
        4009: 'High Priest',
        4010: 'High Wizard',
        4011: 'Whitesmith',
        4012: 'Sniper',
        4013: 'Assassin Cross',
        4015: 'Paladin',
        4016: 'Champion',
        4017: 'Professor',
        4018: 'Stalker',
        4019: 'Creator',
        4020: 'Clown',
        4021: 'Gypsy',
        4023: 'Baby Novice',
        4024: 'Baby Swordsman',
        4025: 'Baby Mage',
        4026: 'Baby Archer',
        4027: 'Baby Acolyte',
        4028: 'Baby Merchant',
        4029: 'Baby Thief',
        4030: 'Baby Knight',
        4031: 'Baby Priest',
        4032: 'Baby Wizard',
        4033: 'Baby Blacksmith',
        4034: 'Baby Hunter',
        4035: 'Baby Assassin',
        4037: 'Baby Crusader',
        4038: 'Baby Monk',
        4039: 'Baby Sage',
        4040: 'Baby Rogue',
        4041: 'Baby Alchemist',
        4042: 'Baby Bard',
        4043: 'Baby Dancer',
        4045: 'Super Baby',
        4046: 'Taekwon Kid',
        4047: 'Taekwon Master',
        4049: 'Soul Linker',
        4054: 'Rune Knight',
        4055: 'Warlock',
        4056: 'Ranger',
        4057: 'Arch Bishop',
        4058: 'Mechanic',
        4059: 'Guillotine Cross',
        4060: 'Rune Knight (Trans)',
        4061: 'Warlock (Trans)',
        4062: 'Ranger (Trans)',
        4063: 'Arch Bishop (Trans)',
        4064: 'Mechanic (Trans)',
        4065: 'Guillotine Cross (Trans)',
        4066: 'Royal Guard (Trans)',
        4067: 'Sorcerer',
        4068: 'Minstrel',
        4069: 'Wanderer',
        4070: 'Sura',
        4071: 'Genetic',
        4072: 'Shadow Chaser',
        4073: 'Royal Guard (Trans)',
        4074: 'Sorcerer (Trans)',
        4075: 'Minstrel (Trans)',
        4076: 'Wanderer (Trans)',
        4077: 'Sura (Trans)',
        4078: 'Genetic (Trans)',
        4079: 'Shadow Chaser (Trans)',
        4080: 'Rune Knight Mount',
        4081: 'Rune Knight Mount (Trans)',
        4082: 'Royal Guard Mount',
        4083: 'Royal Guard Mount (Trans)',
        4084: 'Ranger Mount',
        4085: 'Ranger Mount (Trans)',
        4086: 'Mechanic Mount',
        4087: 'Mechanic Mount (Trans)',
        4088: 'Rune Knight Mount',
        4089: 'Rune Knight Mount (Trans)',
        4090: 'Rune Knight Mount',
        4091: 'Rune Knight Mount (Trans)',
        4092: 'Rune Knight Mount',
        4093: 'Rune Knight Mount (Trans)',
        4094: 'Rune Knight Mount',
        4095: 'Rune Knight Mount (Trans)',
        4211: 'Kagerou',
        4212: 'Oboro'
    }

    def class_name(self, cls_id):
        try:
            return self.classes[cls_id]
        except KeyError:
            return 'Not found'


ragnarok = Ragnarok()
