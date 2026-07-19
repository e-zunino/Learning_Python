# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, 
# wherein the month in the latter might be any of the values in the list below:

# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. 
# Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        input_date = input('Date: ').strip()
        
        try:
            month_str, day_str, year_str = input_date.split('/')
        except ValueError:
            try:
                month_day , year_str = input_date.split(', ')
            except ValueError:
                continue
            else:
                month_str, day_str = month_day.split()
                
                if month_str.capitalize() not in MONTHS:
                    continue
                else:
                    try:
                        year = int(year_str)
                        month = MONTHS.index(month_str.capitalize()) + 1
                        day = int(day_str)
                    except ValueError:
                        continue
                    else:
                        if not (0 < day <= 31 and 0 < month <= 12):
                            continue
                        else:
                            break
        else:
            try:
                year = int(year_str)
                month = int(month_str)
                day = int(day_str)
            except ValueError:
                continue
            else:
                if not (0 < day <= 31 and 0 < month <= 12):
                    continue
                else:
                    break
            
    print(f'{year:04}-{month:02}-{day:02}')


    

main()