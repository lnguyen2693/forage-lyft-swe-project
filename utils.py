from datetime import date

def add_year_to_date(date: date, year_to_add: int):
    return date.replace(year= date.year + year_to_add)