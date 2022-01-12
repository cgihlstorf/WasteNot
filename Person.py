"""
Person Class
"""

from datetime import date

#person login

class Person:

    def __init__(self):

        # variables:

        # dictionary of all food entered (all time), key: food, value: servings 
        self.all_time_dict = {}

        # dictionary of all food entered by year, key: food, value: servings 
        self.year_dict = {}

        # dictionary of food entered by month, resets at beginning of the month, key: food, value: servings 
        self.month_dict = {}

        # dictionary of food entered by week, key: food, value: servings 
        self.week_dict = {}

        # dictionary of food entered by day, key: food, value: servings 
        self.day_dict = {}

        # dictionary for daily/weekly/monthly/yearly/overall carbon footprints
        self.co2_dict = {"day":0, "week":0, "month":0, "year":0, "all-time":0}

        # dictionary of dictionaries of dictionaries of dictionaries
        self.archive_dict = {}

        #dictionary for carbon footprints per single food/serving
        self.food_footprints_dict = {"apple":72, "banana":104, "grape":22, "strawberry":26, "cucumber":154, "tomato":232, "broccoli":43, "potato":280, "sweet potato":146, "cherry tomato":33}

        self.prev_login_day = date.today()


    # finish
    def input_function(self, food_item, amount):

        # building all time dict
        if food_item not in self.all_time_dict.keys():
            self.all_time_dict[food_item] = amount

        else:
            self.all_time_dict[food_item] += amount
            self.food_footprints_dict["all-time"] = self.calculate_footprint(amount, self.food_footprints_dict["all-time"])

        
        # building year dict
        if self.prev_login_day.year != date.year:
            self.reset_dict(self.year_dict)
            self.year_dict[food_item] = amount
        else:
            self.year_dict[food_item] += amount
            self.food_footprints_dict["year"] = self.calculate_footprint(amount, self.food_footprints_dict["year"])

        # building month dict
        if self.prev_login_day.month != date.month or self.prev_login_day.month == date.month and self.prev_login_day.year != date.year:
            self.reset_dict(self.month_dict)
            self.month_dict[food_item] = amount

        else:
            self.month_dict[food_item] += amount
            self.food_footprints_dict["month"] = self.calculate_footprint(amount, self.food_footprints_dict["month"])

        #building week dict
        if date.weekday == 0 and self.prev_login_day != 0: #reset if it's the first of any week and it's your first time logging in that day
            self.reset_dict(self.week_dict)
            self.week_dict[food_item] = amount
        
        else:
            self.week_dict[food_item] += amount
            self.food_footprints_dict["week"] = self.calculate_footprint(amount, self.food_footprints_dict["week"])
        
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
        else:
            self.day_dict[food_item] += amount
            self.food_footprints_dict["day"] = self.calculate_footprint(amount, self.food_footprints_dict["day"])
    

        # update the most recent login time to today  
        # keep near end (outside of all loops) to update previous login day to current day
        self.prev_login_day = date.today()
        

    def reset_dict(self, input_dict):
        input_dict.clear()

    
    #I don's actually think this is needed
    def compare_day(self):
        if str(self.prev_login_day) == str(date.today()):
            return True
        else:
            return False


    
    # takes in two dictionaries, outputs number (gCO2e)
    def calculate_footprint(self, amount, unit_val):
        #food_footprints_dict = single serving
        #co2_dict = cumulative total
        return amount * unit_val
        


def main():
    caroline = Person()
    print(caroline.prev_login_day)


#main()