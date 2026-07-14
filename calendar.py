import calendar
import datetime

def render_month():
    now = datetime.datetime.now()
    month = now.month
    year = now.year
    month_calendar = calendar.monthcalendar(year, month)
    print("Mo Tu We Th Fr Sa Su")
    for week in month_calendar:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "
            else:
                if day == now.day:
                    week_str += f"*{day:2} "
                else:
                    week_str += f" {day:2} "
        print(week_str.strip())

if __name__ == "__main__":
    render_month()