"""
Student Name: Logan Kunz
Class: Computer Programming 1
Period: B6
Project 1: The Barbie Movie
"""

import math

def beach_day_challenge():
    print("\nBeach Day Challenge")
    print("Barbie and her friends are spending a day at the beach.")
    print("They want to manage their expenses.")

    # ---------------------------------------------- BEGIN CODE ----------------------------------------------------- #

    """
    Prompt the user for the following:
    -- Number of people in the group
    -- Cost of beach chairs
    -- Cost of sunscreen
    -- Cost of ice cream
    -- Cost of beach toys
    
    Convert the user input to the appropriate data type (int for number of people, float for costs).
    """

    num_people = float(input("How Many people in the group?: "))
    beach_chairs_cost = float(input("Cost of beach chairs?: "))
    sunscreen_cost = float(input("coast of sunscreen?: "))
    ice_cream_cost = float(input("cost of ice cream?: "))
    beach_toys_cost = float(input("coast of beach toys?: "))

    """
    Calculate the total cost of the beach day that includes all items.
    """
    beach_chairs_cost_total = beach_chairs_cost * num_people
    sunscreen_cost_total = sunscreen_cost * num_people
    ice_cream_cost_total = ice_cream_cost * num_people
    beach_toys_cost_total = beach_toys_cost * num_people

    

    total_cost = beach_chairs_cost_total + sunscreen_cost_total + ice_cream_cost_total + beach_toys_cost_total


    """
    Apply discounts:
    -- 20% discount on beach chairs
    -- 10% discount on ice cream
    Calculate the discounted costs and the new total cost including discounts.
    """
    beach_chairs_cost_discounted = beach_chairs_cost_total - (beach_chairs_cost_total * .20)

    ice_cream_cost_discounted = ice_cream_cost_total - (ice_cream_cost_total * .10)

    discounted_total_cost = beach_chairs_cost_discounted + sunscreen_cost_total + ice_cream_cost_discounted + beach_toys_cost_total

    """
    Calculate each person's share of the costs.
    """

    each_person_share = round(discounted_total_cost / num_people,2)

    # ----------------------------------------------- END CODE ------------------------------------------------------ #

    print(f"\nTotal cost before discounts: ${total_cost:.2f}")
    print(f"Total cost after discounts: ${discounted_total_cost:.2f}")
    print(f"Each person's share: ${each_person_share:.2f}")
    
    return total_cost, discounted_total_cost, each_person_share, num_people

def escape_plan_challenge():
    print("\nEscape Plan Challenge")
    print("Barbie, Ken, and Gloria need to devise an escape plan.")
    print("They have three escape routes to consider.")

    # ---------------------------------------------- BEGIN CODE ----------------------------------------------------- #

    """
    For each of the 3 escape routes, prompt the user to enter:
    -- Distance in miles
    -- Speed in mph
    
    Convert the input values to float.
    """

    route1_distance = float(input("Route 1 distance: "))
    route1_speed = float(input("Route 1 Speed: "))

    route2_distance = float(input("Route 2 distance: "))
    route2_speed = float(input("Route 2 Speed: "))

    route3_distance = float(input("Route 3 distance: "))
    route3_speed = float(input("Route 3 Speed: "))

    """
    Calculate the time taken for each escape route.
    Time taken is distance divided by speed.
    """

    time_route1 = round(route1_distance/route1_speed, 2)
    time_route2 = round(route2_distance/route2_speed, 2)
    time_route3 = round(route3_distance/route3_speed, 2)

    """
    Determine which escape route takes the shortest amount of time.
    """

    fastest_route = min(time_route1,time_route2,time_route3)

    """
    Calculate the time saved by choosing the fastest route compared to the slowest route.
    """

    slowest_route = max(time_route1,time_route2,time_route3)

    time_saved = slowest_route - fastest_route

    # ----------------------------------------------- END CODE ------------------------------------------------------ #

    print(f"\nTime required for Route 1: {time_route1:.2f} hours")
    print(f"Time required for Route 2: {time_route2:.2f} hours")
    print(f"Time required for Route 3: {time_route3:.2f} hours")
    print(f"The fastest route takes {fastest_route:.2f} hours.")
    print(f"Time saved by choosing the fastest route: {time_saved:.2f} hours")
    
    return time_route1, time_route2, time_route3, fastest_route, time_saved

def society_reformation_challenge():
    print("\nSociety Reformation Challenge")
    print("Barbie returns to Barbieland to reform the society.")
    print("She wants to implement changes to promote equality and fairness.")

    # ---------------------------------------------- BEGIN CODE ----------------------------------------------------- #

    """
    Prompt the user to enter:
    -- Number of proposed societal changes
    -- Number of successfully implemented changes
    
    Convert the user input values to int.
    """

    total_proposed_changes = int(input("Number of Proposed Changes: "))
    successful_changes = int(input("Number of Successful Changes: "))

    """
    Calculate the percentage of societal changes that were successfully implemented.
    """

    def success_rate_calc(total, succeeded):
        if succeeded != 0:
            return round(succeeded/total,2) * 100
        elif succeeded <= 0:
            return 0

    success_rate = success_rate_calc(total_proposed_changes,successful_changes)

    """
    Calculate how many additional changes need to be implemented to achieve a 75% success rate.
    """
    


    needed_changes = math.ceil((total_proposed_changes * .75) - successful_changes)

    """
    Calculate the remaining changes to be implemented.
    This is the difference between the total proposed changes and the successful changes.
    """

    remaining_changes = total_proposed_changes - successful_changes

    # ----------------------------------------------- END CODE ------------------------------------------------------ #

    print(f"\nPercentage of successful changes: {success_rate:.2f}%")
    print(f"Number of additional changes needed to achieve a 75% success rate: {needed_changes}")
    print(f"Remaining changes to be implemented: {remaining_changes}")
    
    return success_rate, needed_changes, remaining_changes
    
# Main program to run all challenges
def main():
    # beach_day_challenge()
    # escape_plan_challenge()
    society_reformation_challenge()


if __name__ == "__main__":
    main()
