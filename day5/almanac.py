import re
from utils.list import split_list


class MappingItem:
    def __init__(self, line) -> None:
        match = re.match("(\d+) (\d+) (\d+)", line)
        if match is None:
            raise Exception("ParseException: mapping item line is not correctly formed")
        self.destination = int(match.group(1))
        self.source = int(match.group(2))
        self.length = int(match.group(3))
        self.source_range = range(self.source, self.source + self.length)


class BaseAlmanac:
    seeds = list()

    def __init__(self, lines) -> None:
        maps = split_list(lines)
        self.seed_to_soil = list(map(MappingItem, maps[1][1:]))
        self.soil_to_fertilizer = list(map(MappingItem, maps[2][1:]))
        self.fertilizer_to_water = list(map(MappingItem, maps[3][1:]))
        self.water_to_light = list(map(MappingItem, maps[4][1:]))
        self.light_to_temperature = list(map(MappingItem, maps[5][1:]))
        self.temperature_to_humidity = list(map(MappingItem, maps[6][1:]))
        self.humidity_to_location = list(map(MappingItem, maps[7][1:]))

    def map_to(self, value: int, mapping_items: list[MappingItem]) -> int:
        for mapping_item in mapping_items:
            if value in mapping_item.source_range:
                return value - mapping_item.source + mapping_item.destination
        return value

    def map_all_to(
        self, values: list[int], mapping_items: list[MappingItem]
    ) -> list[int]:
        return list(map(lambda s: self.map_to(s, mapping_items), values))

    @property
    def locations(self):
        soils = self.map_all_to(self.seeds, self.seed_to_soil)
        fertilizers = self.map_all_to(soils, self.soil_to_fertilizer)
        waters = self.map_all_to(fertilizers, self.fertilizer_to_water)
        lights = self.map_all_to(waters, self.water_to_light)
        temperatures = self.map_all_to(lights, self.light_to_temperature)
        humidities = self.map_all_to(temperatures, self.temperature_to_humidity)
        return self.map_all_to(humidities, self.humidity_to_location)
