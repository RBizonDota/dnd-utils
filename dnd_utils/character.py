import typing as t
import pydantic

from .utils import AllowedJSONFormatsEnum, parse_int_value, LONG_STORY_SHOT_STAT_LABELS_TO_DATA


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
    
class Character(BaseCharacter):
    char_class: str
    level: int
    race: str
    alignment: t.Optional[str]
    # experience: t.Optional[int]
    sub_info: t.Optional[CharacterSubinfo]
    stats: CharacterStats
    skills: CharacterSkills

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
            skills={
                k:parse_int_value(v.get("customModifier")) for k,v in data["skills"].items()
            },
        )
        return char

    @classmethod
    def from_json(cls, data: t.Dict, format: AllowedJSONFormatsEnum):
        if format == AllowedJSONFormatsEnum.LONG_STORY_SHOT:
            return cls._parse_longstoryshot(data)