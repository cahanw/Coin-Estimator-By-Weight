import math

#creates the coin class for us to assign attributes to each coin
class coin:
    def __init__(self, weight, value, per_roll):
        self.weight = weight
        self.value = value
        self.per_roll = per_roll

#instantiates a coin object for each coin type        
cent = coin(2.5, 1, 125.0)
nickel = coin(5.0, 5, 200.0)
dime = coin(2.268, 10, 113.4)
quarter = coin(5.670, 25, 226.8)

#asks user for the unit type - pounds or grams
def getUnits():
    global unit
    while True:
        unit = input("Do you wish to enter units in grams or pounds? \n Enter \"g\" for grams. \n Enter \"p\" for pounds. \n")
        if unit.lower() not in ["g","p"]:
            print("Invalid response. Please try again.")
            continue
        else:
            return unit
            

#ask user for the amount of each coin (and converts the amount to grams if needed)
def getAmounts(unit):
    global cent_amount
    global nickel_amount
    global dime_amount
    global quarter_amount 
    
    if unit == "g":
        cent_amount = int(input("How much do your cents weigh? "))
        nickel_amount = int(input("How much do your nickels weigh? "))
        dime_amount = int(input("How much do your dimes weigh? "))
        quarter_amount = int(input("How much do your quarters weigh? "))
        
    elif unit == "p":
        cent_amount = int(input("How much do your cents weigh? "))* 0.0022046244201838
        nickel_amount = int(input("How much do your nickels weigh? "))* 0.0022046244201838
        dime_amount = int(input("How much do your dimes weigh? "))* 0.0022046244201838
        quarter_amount = int(input("How much do your quarters weigh? "))* 0.0022046244201838

        
def getFinalValues():
    global total_amount
    global total_value
    total_value = 0
    total_amount = 0

    cent_wrappers_needed = math.ceil(cent_amount/ cent.per_roll)
    total_value += (cent_amount/cent.weight * cent.value)
    total_amount += round(cent_amount/cent.weight)

    nickel_wrappers_needed = math.ceil(nickel_amount / nickel.per_roll)
    total_value += (nickel_amount/nickel.weight * nickel.value)
    total_amount += round(nickel_amount/nickel.weight)

    dime_wrappers_needed = math.ceil(dime_amount/ dime.per_roll)
    total_value += (dime_amount/dime.weight * dime.value)
    total_amount += round(dime_amount/dime.weight)

    quarter_wrappers_needed = math.ceil(quarter_amount/ quarter.per_roll)
    total_value += (quarter_amount/quarter.weight * quarter.value)
    total_amount += round(quarter_amount/quarter.weight)

    total_value /= 100
    total_amount = round(total_amount)
    total_value = round(total_value)
    
    return(cent_wrappers_needed, nickel_wrappers_needed, dime_wrappers_needed, quarter_wrappers_needed, total_amount, total_value)

def Main():
    global final_values
    unit = getUnits()
    getAmounts(unit)
    final_values = getFinalValues()   
    print("Cent wrappers needed:", final_values[0])
    print("Nickel wrappers needed:", final_values[1])
    print("Dime wrappers needed:", final_values[2])
    print("Quarter wrappers needed:", final_values[3])
    print("Total Coins:", final_values[4])
    print("Total Value: $" + str(final_values[5]))
    
Main()