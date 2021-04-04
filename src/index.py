import unit
import math


def scientific_notation(value):
    return '{:e}'.format(value)


def coulombs_law(**given):
    F = given.get('F')
    q1 = given.get('q1')
    q2 = given.get('q2')
    r = given.get('r')
    k = given.get('k', 8.99 * 1e9)

    # Electric force is required to find
    if (q1 and q2 and r and not F):
        distance = unit.base(r) ** 2
        numerator = unit.base(q1) * unit.base(q2) * k

        electric_force = numerator / distance
        return electric_force
    # Both charges is required to find
    elif (F and r and not q1 and not q2):
        distance = unit.base(r) ** 2

        numerator = distance * unit.base(F)
        charge_product = numerator / k
        split_charge = math.sqrt(abs(charge_product))

        return {
            'product charges': charge_product,
            'each charge': split_charge,
        }
    # Charge 1 is required to find
    elif (F and r and q2 and not q1):

        distance = unit.base(r) ** 2
        numerator = unit.base(F) * distance
        denominator = unit.base(q2) * k

        first_charge = numerator / denominator
        return first_charge
    # Charge 2 is required to find
    elif (F and r and q1 and not q2):

        distance = unit.base(r) ** 2
        numerator = unit.base(F) * distance
        denominator = unit.base(q1) * k

        second_charge = numerator / denominator
        return second_charge
    # Distance is required to find
    elif (F and q1 and q2 and not r):
        numerator = unit.base(q1) * unit.base(q2) * k
        distance_raw = numerator / unit.base(F)

        distance = math.sqrt(abs(distance_raw))

        return distance
    # Unable to solve the problem
    else:
        pass
