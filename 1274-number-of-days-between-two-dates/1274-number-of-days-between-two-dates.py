class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isLeapYear(year: int) -> bool:
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        def daysInMonth(year: int, month: int) -> int:
            days = [31, 28 + int(isLeapYear(year)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return days[month - 1]

        def calcDays(date: str) -> int:
            year, month, day = map(int, date.split("-"))
            days = 0
            for y in range(1971, year):
                days += 365 + int(isLeapYear(y))
            for m in range(1, month):
                days += daysInMonth(year, m)
            days += day
            return days

        return abs(calcDays(date1) - calcDays(date2))

        # def set_feb(year):
        #     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        #         months[1] = 29
        #     else:
        #         months[1] = 28           

        # def cal_days_to_year_end(d):
        #     year = int(d[:4])
        #     set_feb(year)
        #     month = int(d[5:7]) - 1
        #     days = int(d[8:])
        #     n_days = months[month] - days
        #     for m in range(month+1, 12):
        #         n_days += months[m]       
        #     return n_days     

        # months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # if date1 > date2:
        #     date1, date2 = date2, date1
        # start_year = int(date1[:4])
        # end_year = int(date2[:4])
        # if start_year == end_year:
        #     return cal_days_to_year_end(date1) - cal_days_to_year_end(date2)

        # nums_days = cal_days_to_year_end(date1)
        # while start_year + 1 != end_year:
        #     set_feb(start_year + 1)
        #     nums_days += sum(months)            
        #     start_year += 1
        # set_feb(end_year)
        # month = int(date2[5:7])-1
        # days = int(date2[8:])
        # nums_days += days
        
        # for m in range(month):
        #     nums_days += months[m]        
        # return nums_days
        
           
            
            