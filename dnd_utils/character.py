import typing as t
import pydantic

from .utils import AllowedJSONFormatsEnum, parse_int_value, LONG_STORY_SHOT_STAT_LABELS_TO_DATA, MAP_FORMAT_TO_EXTRACTOR


class CharacterSubinfo(pydantic.BaseModel):
    age: t.Optional[int]
    height: t.Optional[int]
    weight: t.Optional[int]
    eyes: t.Optional[str]
    hair: t.Optional[str]


class CharacterStats(pydantic.BaseModel):
    strength: int = 10 # Сила
    dexterity: int = 10 # Ловкость
    constitution: int = 10 # Телосложение
    intelligence: int = 10 # Интеллект
    wisdom: int = 10 # Мудрость
    charisma: int = 10 # Харизма

class CharacterStatMods(pydantic.BaseModel):
    strength: int = 0 # Сила
    dexterity: int = 0 # Ловкость
    constitution: int = 0 # Телосложение
    intelligence: int = 0 # Интеллект
    wisdom: int = 0 # Мудрость
    charisma: int = 0 # Харизма


class CharacterSkills(pydantic.BaseModel):
    acrobatics: int = 0 # Акробатика
    investigation: int = 0 # Анализ
    athletics: int = 0 # Атлетика
    perception: int = 0 # Восприятие
    survival: int = 0 # Выживание
    performance: int = 0 # Выступление
    intimidation: int = 0 # Запугивание
    history: int = 0 # История
    sleight_of_hand: int = 0 # Ловкость рук
    arcana: int = 0 # Магия
    medicine: int = 0 # Медицина
    deception: int = 0 # Обман
    nature: int = 0 # Природа
    insight: int = 0 # Проницательность
    religion: int = 0 # Религия
    stealth: int = 0 # Скрытность
    persuasion: int = 0 # Убеждение
    animal_handling: int = 0 # Уход за животными


class BaseCharacter(pydantic.BaseModel):
    name: str
    char_class: str
    level: int
    race: str
    alignment: t.Optional[str]
    sub_info: t.Optional[CharacterSubinfo]
    stats: CharacterStats
    stat_mods: CharacterStatMods
    skills: CharacterSkills
    
class Character(BaseCharacter):

    @classmethod
    def _parse_longstoryshot(cls, data: t.Dict):
        char = Character(
            name=data["name"]["value"],
            level=data["info"]["level"]["value"],
            race=data["info"]["race"]["value"],
            alignment=data["info"]["alignment"]["value"],
            char_class=data["info"]["charClass"]["value"],
            sub_info={
                k:parse_int_value(v["value"]) for k,v in data["subInfo"].items()
            },
            stats={
                LONG_STORY_SHOT_STAT_LABELS_TO_DATA[k]:v["score"] for k,v in data["stats"].items()
            },
            stat_mods={
                LONG_STORY_SHOT_STAT_LABELS_TO_DATA[k]:parse_int_value(v.get("customModifier")) for k,v in data["saves"].items()    
            },
            skills={
                k:parse_int_value(v.get("customModifier")) for k,v in data["skills"].items()
            },
        )
        return char

    @classmethod
    def from_json(cls, data: t.Dict, format: AllowedJSONFormatsEnum = AllowedJSONFormatsEnum.LONG_STORY_SHOT):
        if format == AllowedJSONFormatsEnum.LONG_STORY_SHOT:
            return cls._parse_longstoryshot(data)
    
    @classmethod
    def from_file(cls, file_path: str, format: AllowedJSONFormatsEnum = AllowedJSONFormatsEnum.LONG_STORY_SHOT):
        with open(file_path, 'r') as f:
            data = MAP_FORMAT_TO_EXTRACTOR[format](f)
        return cls.from_json(data, format)

    def get_stat_mod(self, stat_name: str) -> int:
        stat_score = getattr(self.stats, stat_name)
        mod_score = getattr(self.stat_mods, stat_name)
        return (stat_score-10)//2+mod_score