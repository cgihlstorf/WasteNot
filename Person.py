"""
Tri-Co Hackathon Group 1: Person Class File
Authors:
Description:
"""

from datetime import date

# person login

class Person:

    # constructor
    def __init__(self):

        # initializing variables

        # dictionary of all food entered (all time), key: food, value: servings 
        self.all_time_dict = {"apple":0, "banana":0, "grape":0, "strawberry":0, "blueberries":0, "raspberries":0, "blackberries":0, "lemon":0, "lime":0, "cucumber":0, "tomato":0, "lettuce":0, "celery":0, "broccoli":0, "potato":0, "sweet potato":0, "cherry tomato":0, "avocado":0, "onion":0, "mango":0}

        # dictionary of all food entered by year, key: food, value: servings 
        self.year_dict = {"apple":0, "banana":0, "grape":0, "strawberry":0, "blueberries":0, "raspberries":0, "blackberries":0, "lemon":0, "lime":0, "cucumber":0, "tomato":0, "lettuce":0, "celery":0, "broccoli":0, "potato":0, "sweet potato":0, "cherry tomato":0, "avocado":0, "onion":0, "mango":0}

        # dictionary of food entered by month, resets at beginning of the month, key: food, value: servings 
        self.month_dict = {"apple":0, "banana":0, "grape":0, "strawberry":0, "blueberries":0, "raspberries":0, "blackberries":0, "lemon":0, "lime":0, "cucumber":0, "tomato":0, "lettuce":0, "celery":0, "broccoli":0, "potato":0, "sweet potato":0, "cherry tomato":0, "avocado":0, "onion":0, "mango":0}

        # dictionary of food entered by week, key: food, value: servings 
        self.week_dict = {"apple":0, "banana":0, "grape":0, "strawberry":0, "blueberries":0, "raspberries":0, "blackberries":0, "lemon":0, "lime":0, "cucumber":0, "tomato":0, "lettuce":0, "celery":0, "broccoli":0, "potato":0, "sweet potato":0, "cherry tomato":0, "avocado":0, "onion":0, "mango":0}

        # dictionary of food entered by day, key: food, value: servings 
        self.day_dict = {"apple":0, "banana":0, "grape":0, "strawberry":0, "blueberries":0, "raspberries":0, "blackberries":0, "lemon":0, "lime":0, "cucumber":0, "tomato":0, "lettuce":0, "celery":0, "broccoli":0, "potato":0, "sweet potato":0, "cherry tomato":0, "avocado":0, "onion":0, "mango":0}

        # dictionary for daily/weekly/monthly/yearly/overall carbon footprints
        self.co2_dict = {"day":0, "week":0, "month":0, "year":0, "all-time":0}

        #dictionary for carbon footprints per single food/serving
        self.food_footprints_dict = {"apple":72, "banana":104, "grape":22, "strawberry":26, "blueberries":486, "raspberries":437, "blackberries":486, "lemon":133, "lime":95, "cucumber":154, "tomato":232, "lettuce":885, "celery":42, "broccoli":43, "potato":280, "sweet potato":146, "cherry tomato":33, "avocado":408, "onion":179, "mango":880}

        # holds previous login day so we know how to update dictionaries
        self.prev_login_day = date(1700, 1, 1)

    # finish
    def input_function(self, food_item, amount):

        if food_item not in self.food_footprints_dict.keys():
            raise Exception("Food item entered is not valid")

        self.all_time_dict[food_item] += amount

        # no matter what, this will increment
        self.co2_dict["all-time"] += self.calculate_footprint(amount, self.food_footprints_dict[food_item])

        # building year dict
        if self.prev_login_day.year != date.today().year:
            self.reset_dict(self.year_dict)
            self.year_dict[food_item] = amount
            self.co2_dict["year"] = self.calculate_footprint(amount, self.food_footprints_dict[food_item])
       
        else:
            self.year_dict[food_item] += amount
            self.co2_dict["year"] += self.calculate_footprint(amount, self.food_footprints_dict[food_item])

        # building month dict
        if self.prev_login_day.month != date.today().month or self.prev_login_day.month == date.today().month and self.prev_login_day.year != date.today().year:
            self.reset_dict(self.month_dict)
            self.month_dict[food_item] = amount
            self.co2_dict["month"] = self.calculate_footprint(amount, self.food_footprints_dict[food_item])

        else:
            self.month_dict[food_item] += amount
            self.co2_dict["month"] += self.calculate_footprint(amount, self.food_footprints_dict[food_item])

        # building week dict
        # extra case to come back to: one year apart, same week (example: week 32 of 2019 and week 32 of 2020, week_dict would not reset)
        if self.prev_login_day.isocalendar()[1] != date.today().isocalendar()[1] or self.prev_login_day.isocalendar()[1] == date.today().isocalendar()[1] and date.today().year - self.prev_login_day.year > 1: 
            self.reset_dict(self.week_dict)
            self.week_dict[food_item] = amount
            self.co2_dict["week"] = self.calculate_footprint(amount, self.food_footprints_dict[food_item])
        
        else:
            self.week_dict[food_item] += amount
            self.co2_dict["week"] += self.calculate_footprint(amount, self.food_footprints_dict[food_item])
        
        # building day dict
        ##if date.day > self.prev_login_day.day and date.weekday() == self.prev_login_day.weekday() or 


        #if the day is different from the last day you logged in but the day of the week are the same, OR
        #if the day is the same numbered day as the day you logged in but the day of the week is different, OR
        #if the day and day of the week are the same but the month is different, OR
        #if the day and the day of the week and the month are the same but the year is different 
        # if ((date.day != self.prev_login_day.day) and (date.weekday() == self.prev_login_day.weekday())) or 
        #    ((date.day == self.prev_login_day.day) and (date.weekday != self.prev_login_day.weekday())) or
        #    ((date.day == self.prev_login_day.day) and (date.weekday = self.prev_login_day.weekday()) and date.month != prev_login_day.month) or

        #hang on, this might be easier and I think it covers all the bases:
        if self.compare_day() == False:
            self.reset_dict(self.day_dict)
            self.day_dict[food_item] = amount
            self.co2_dict["day"] = self.calculate_footprint(amount, self.food_footprints_dict[food_item])

        else:
            self.day_dict[food_item] += amount
            self.co2_dict["day"] += self.calculate_footprint(amount, self.food_footprints_dict[food_item])
    

        # update the most recent login time to today, as input was just made
        self.prev_login_day = date.today()
        

    def reset_dict(self, input_dict):
        input_dict.clear()

    
    def compare_day(self):
        if str(self.prev_login_day) == str(date.today()):
            return True
        else:
            return False


    # takes in amount of food, carbon footprint of one unit of that food, outputs total footprint number (unit: gCO2e)
    def calculate_footprint(self, amount, unit_val):
        #food_footprints_dict = single serving
        #co2_dict = cumulative total
        return amount * unit_val
        


def main():
    caroline = Person()
    print(caroline.prev_login_day.year)
    print(date.today().year)
    print("week:", caroline.prev_login_day.isocalendar()[1])
    caroline.input_function("apple", 6)
    print("all time:", caroline.all_time_dict)
    print("co2 dict:", caroline.co2_dict)


main()