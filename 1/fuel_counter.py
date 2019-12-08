def get_fuel_required(mass: int):
    fuel_required = int(mass / 3) - 2
    return max(0, fuel_required)


def get_total_fuel_required(masses):
    return sum([get_fuel_required(int(mass)) for mass in masses])
