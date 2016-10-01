def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    cpdiff_low = 0
    cpdiff_high = 0
    closest_found = False
    power = 0
    while closest_found != True:
       exp = base**power
       cpdiff_low = abs(num-exp)
       prev_power = power
       power += 1
       exp = base**power
       cpdiff_high = abs(num-exp)
       if cpdiff_high >= cpdiff_low :
           return prev_power


print(closest_power(4, 1))
