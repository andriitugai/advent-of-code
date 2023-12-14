
class  IntervalMap:
    def __init__(self) -> None:
        self.intervals = []

    def put(self, line: str) -> None:
        dst, src, rng = map(int, line.strip().split())
        delta = dst - src
        self.intervals.append((src, src+rng, delta))

    def get(self, key: int) -> int:
        for interval in self.intervals:
            if interval[0] <= key < interval[1]:
                return key + interval[2]
        return key
    

def solution(filename: str) -> int:
    seeds = []
    seed_to_soil = IntervalMap()
    soil_to_fertilizer = IntervalMap()
    fertilizer_to_water = IntervalMap()
    water_to_light = IntervalMap()
    light_to_temperature = IntervalMap()
    temperature_to_humidity = IntervalMap()
    humidity_to_location = IntervalMap()
    
    current_map = seed_to_soil

    with open(filename) as input:
        for line in input:
            if not line.strip():
                continue
            if line.startswith("seeds:"):
                seeds = map(int, line.strip().split()[1:])
                continue
            if line.startswith("seed-to-soil"):
                print("seed-to-soil")
                current_map = seed_to_soil
            elif line.startswith("soil-to-fertilizer"):
                print("soil-to-fertilizer")
                current_map = soil_to_fertilizer
            elif line.startswith("fertilizer-to-water"):
                print("fertilizer-to-water")
                current_map = fertilizer_to_water
            elif line.startswith("water-to-light"):
                print("water-to-light")
                current_map = water_to_light
            elif line.startswith("light-to-temperature"):
                print("light-to-temperature")
                current_map = light_to_temperature
            elif line.startswith("temperature-to-humidity"):
                print("temperature-to-humidity")
                current_map = temperature_to_humidity
            elif line.startswith("humidity-to-location"):
                print("humidity-to-location")
                current_map = humidity_to_location
            else:
                current_map.put(line=line)

    min_dist = float('inf')
    for seed in seeds:
        dist = humidity_to_location.get(
                    temperature_to_humidity.get(
                        light_to_temperature.get(
                            water_to_light.get(
                                fertilizer_to_water.get(
                                    soil_to_fertilizer.get(
                                        seed_to_soil.get(seed)
                )))))) 
        
        if dist < min_dist:
            min_dist = dist

    return min_dist


if __name__ == '__main__':
    print(solution('2023/day-05/input.txt'))
