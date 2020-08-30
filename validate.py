import re

def validate_date(date_from,date_to):
    pattern = "^([0-9]{4})-(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|[0-9]{1,2})-[0-9]{1,2}$"
    if re.match(pattern,date_from) and re.match(pattern,date_to):
        date = date_from.split('-')
        if int(date[2]) > 0 and int(date[2]) <= 31 and int(date[0]) > 999:
            date2 = date_to.split('-')
            if int(date2[2]) > 0 and int(date2[2]) <= 31 and int(date2[0]) > 999:
                day_from = int(date[2])
                day_to = int(date2[2])
                mon_from = get_month(date[1])
                mon_to = get_month(date2[1])
                year_from = date[0]
                year_to = date2[0]
                if year_from < year_to:
                    return True
                elif year_from == year_to:
                    if mon_from < mon_to:
                        return True
                    elif mon_from == mon_to:
                        if day_from <= day_to:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

            else:
                return False
        else:
            return False
    else:
        return False

def get_month(month):
    if month == "jan" or month == "01":
        return 1
    elif month == "feb" or month == "02":
        return 2
    elif month == "mar"or month == "03":
        return 3
    elif month == "apr"or month == "04":
        return 4
    elif month == "may"or month == "05":
        return 5
    elif month == "jun"or month == "06":
        return 6
    elif month == "jul"or month == "07":
        return 7
    elif month == "aug"or month == "08":
        return 8
    elif month == "sep"or month == "09":
        return 9
    elif month == "oct"or month == "10":
        return 10
    elif month == "nov"or month == "11":
        return 11
    elif month == "dec"or month == "12":
        return 12
