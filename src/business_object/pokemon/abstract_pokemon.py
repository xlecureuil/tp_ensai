import copy
from abc import ABC, abstractmethod
from business_object.statistic import Statistic


class AbstractPokemon(ABC):
    """
    Abstract class for a Pokemon
    """

    # -------------------------------------------------------------------------
    # Constructor
    # -------------------------------------------------------------------------

    def __init__(
        self, stat_max=None, stat_current=None, level=0, name=None, type_pk=None
    ):
        # -----------------------------
        # Attributes
        # -----------------------------
        self._stat_max: Statistic = stat_max
        self._stat_current: Statistic = stat_current
        self._level: int = level
        self._name: str = name
        self._type: str = type_pk

    # -------------------------------------------------------------------------
    # Abstract Methods
    # -------------------------------------------------------------------------

    @abstractmethod
    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the pokemon type.
        Must be implemented by subclasses.

        Returns :
            float : the multiplier
        """
        pass

    @abstractmethod
    def level_up(self) -> None:
        """
        Increase the level by one.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def reset_actual_stat(self) -> None:
        """
        Reset the actual stats of the Pokemon.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def get_hit(self, damage) -> None:
        """
        Decrease health point when receiving damages.
        Must be implemented by subclasses.
        """
        pass

    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------

    def __str__(self):
        res = "I am " + str(self.name)
        res += ", level : " + str(self.level)
        res += ", attack coef : " + str(self.get_pokemon_attack_coef())
        return res

    # -------------------------------------------------------------------------
    # Getters and Setters
    # -------------------------------------------------------------------------

    @property
    def attack(self):
        return self._stat_max.attack

    @property
    def hp(self):
        return self._stat_max.hp

    @property
    def defense(self):
        return self._stat_max.defense

    @property
    def sp_atk(self):
        return self._stat_max.sp_atk

    @property
    def sp_def(self):
        return self._stat_max.sp_def

    @property
    def speed(self):
        return self._stat_max.speed

    @property
    def attack_current(self):
        return self._stat_current.attack

    @attack_current.setter
    def attack_current(self, value):
        self._stat_current.attack = value

    @property
    def hp_current(self):
        return self._stat_current.hp

    @hp_current.setter
    def hp_current(self, value):
        self._stat_current.hp = value

    @property
    def defense_current(self):
        return self._stat_current.defense

    @defense_current.setter
    def defense_current(self, value):
        self._stat_current.defense = value

    @property
    def sp_atk_current(self):
        return self._stat_current.sp_atk

    @sp_atk_current.setter
    def sp_atk_current(self, value):
        self._stat_current.sp_atk = value

    @property
    def sp_def_current(self):
        return self._stat_current.sp_def

    @sp_def_current.setter
    def sp_def_current(self, value):
        self._stat_current.sp_def = value

    @property
    def speed_current(self):
        return self._stat_current.speed

    @speed_current.setter
    def speed_current(self, value):
        self._stat_current.speed = value

    # Basic Getter / Setter
    @property
    def stat(self):
        return self.stat

    @property
    def level(self):
        return self._level

    @property
    def name(self):
        return self._name
