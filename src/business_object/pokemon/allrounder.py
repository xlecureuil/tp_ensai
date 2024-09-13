class Allrounder(abstract_pokemon):
    def __init__(
        self, stat_max=None, stat_current=None, level=0, name=None, type_pk=None
    ):
        super().__init__(stat_max, stat_current, level, name, type_pk)

    def get_pokemon_attack_coef(self):
        multiplier = 1 + (self.sp_atk_current + self.sp_def_current) / 200
        return multiplier