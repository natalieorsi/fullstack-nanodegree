import cgi

#dates
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    if month.title() in months:
        return month.title()

def valid_day(day):
    if day.isdigit():
        day = int(day)
        if day>0 and day<32:
            return int(day)

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year>1899 and year<2021:
            return year

#validation
def escape_html(s):
  return cgi.escape(s, quote = True)