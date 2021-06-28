class Island:
    def __init__(self):
        self.width = None
        self.height = None
        self.number_of_big_iron_ores = 0
        self.number_of_small_iron_ores = 0
        self.number_of_gold_ores = 0
        self.suitability_for_spices = 0.0  # 0 = 0%, 0.5 = 50%, 1 = 100%
        self.suitability_for_tabacco = 0.0
        self.suitability_for_vines = 0.0
        self.suitability_for_cotton = 0.0
        self.suitability_for_sugarcane = 0.0
        self.x = None
        self.y = None
