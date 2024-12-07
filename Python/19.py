# calendar
import calendar
yy = 2025
mm= 12
#print(calendar.month(yy, mm))
print(calendar.calendar(yy))


print(".................................................................................")

import calendar
from colorama import Fore, Style
import colorama
colorama.init()

year = 2025
for month in range (1,13):
    month_name = calendar.month_name[month]
    print(Fore.GREEN + month_name + Style.RESET_ALL)
    print(calendar.month(year, month))