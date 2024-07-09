class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))

        # List to represent the number of days in each month
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Check if the year is a leap year and update days_in_month for February
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[2] = 29

        # Calculate the day number
        day_number = sum(days_in_month[:month]) + day

        return day_number