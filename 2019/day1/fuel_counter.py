def get_fuel_required(mass: int):
    fuel_required = int(mass / 3) - 2
    if fuel_required <= 0:
        return 0
    else:
        return fuel_required + get_fuel_required(fuel_required)


def get_total_fuel_required(masses):
    return sum([get_fuel_required(int(mass)) for mass in masses])
