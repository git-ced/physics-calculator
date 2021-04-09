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


def electric_field_2d(F1, F2, angle, position_x='center', position_y='middle'):
    if (position_x == 'right'):
        exp = math.cos(angle) * F1
        exn = math.cos(angle) * F2
    elif (position_x == 'left'):
        exp = -(math.cos(angle) * F1)
        exn = -(math.cos(angle) * F2)
    else:
        exp = math.cos(angle) * F1
        exn = -(math.cos(angle) * F2)

    if (position_y == 'top'):
        eyp = math.sin(angle) * F1
        eyn = math.sin(angle) * F2
    elif (position_y == 'bottom'):
        eyp = -(math.sin(angle) * F1)
        eyn = -(math.sin(angle) * F2)
    else:
        eyp = math.sin(angle) * F1
        eyn = -(math.sin(angle) * F2)

    esumx = exp + exn
    esumy = eyp + eyn

    enet_magni = math.sqrt((esumx ** 2) + (esumy ** 2))
    enet_angle = math.atan(esumy / esumx)

    return {
        'EP': F1,
        'EN': F2,
        'ANGLE': angle,
        'EXP': exp,
        'EYP': eyp,
        'EXN': exn,
        'EYN': eyn,
        'ESUMX': esumx,
        'ESUMY': esumy,
        'ENET MAGNITUDE': enet_magni,
        'ENET ANGLE': enet_angle,
    }


def gauss_law(**given):
    Eo = given.get('Eo', 8.854 * 1e-12)
    Flux = given.get('I')
    Q = given.get('Q')

    # Flux is missing
    if (Q and not Flux):
        return unit.base(Q) / Eo
    # Charge is missing
    if (Flux and not Q):
        return Flux * Eo
    # Unable to solve the problem
    else:
        pass


def electric_flux(**given):
    Flux = given.get('I')
    E = given.get('E')
    A = given.get('A')
    phi = given.get('phi')

    # Flux is missing
    if (E and A and phi and not Flux):
        flux = unit.base(E) * unit.base(A) * math.cos(math.radians(phi))
        return flux
    # Area is missing
    elif (Flux and E and phi and not A):
        denominator = unit.base(E) * math.cos(math.radians(phi))
        area = Flux / denominator
        return area
    # Magnitude of the electric field is missing
    elif (Flux and A and phi and not E):
        denominator = unit.base(A) * math.cos(math.radians(phi))
        magnitude = Flux / denominator
        return magnitude
    # Unable to solve the problem
    else:
        pass


def line_of_charge(**given):
    Eo = given.get('Eo', 8.854 * 1e-12)
    Q = given.get('Q')
    L = given.get('L')
    r = given.get('r')
    E = given.get('E')

    # Electric field is missing
    if (not E and Q and L and r):
        line_charge_density = unit.base(Q) / unit.base(L)
        denominator = 2 * math.pi * Eo * unit.base(r)
        return line_charge_density / denominator
    # Charge is missing
    elif (not Q and E and L and r):
        return E * 2 * math.pi * Eo * unit.base(r) * unit.base(L)
    # Length is missing
    elif (not L and Q and E and r):
        denominator = E * 2 * math.pi * Eo * unit.base(r)
        return unit.base(Q) / denominator
    # distance is missing
    elif (not r and Q and E and L):
        line_charge_density = unit.base(Q) / unit.base(L)
        denominator = E * 2 * math.pi * Eo
        return line_charge_density / denominator
    # Unable to solve the problem
    else:
        pass
