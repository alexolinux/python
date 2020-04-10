def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city.capitalize() == "Charlotte":
        return 183.
    elif city.capitalize() == "Tampa":
        return 220.
    elif city.capitalize() == "Pittsburgh":
        return 222.
    elif city.capitalize() == "Los Angeles":
        return 475.

def rental_car_cost(days):
    day_cost = 40.
    if days >= 7:
        return (days * day_cost) - 50
    elif (days >= 3 and days < 7):
        return (days * day_cost) - 20
    else:
        return days * day_cost


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

#Getting city, number days...
#print(trip_cost("Los Angeles", 5, 600))

city = input("Inform your destination:\n (Charlotte/Tampa/Pittsburgh/Los Angeles): ")
n_days = int(input("Days of stay: "))
sp_money = float(input("Consumer Spending Forecast: "))

print(trip_cost(city, n_days, sp_money))