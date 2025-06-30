from datetime import datetime, timedelta

now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print(f"Current Date and Time:")
print(f"Day: {day}, Month: {month}, Year: {year}")
print(f"Hour: {hour}, Minute: {minute}")
print(f"Timestamp: {timestamp}")

formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

date_str = "5 December, 2019"
date_obj = datetime.strptime(date_str, "%d %B, %Y")
print(f"Converted datetime object: {date_obj}")
new_year = datetime(year=now.year + 1, month=1, day=1)
time_to_new_year = new_year - now
print(f"Time until New Year: {time_to_new_year}")

unix_epoch = datetime(year=1970, month=1, day=1)
time_since_epoch = now - unix_epoch
print(f"Time since Unix epoch: {time_since_epoch}")

print("\nPractical uses of datetime module include:")
print("- Time series analysis for financial or sensor data")
print("- Timestamping activities in applications (e.g., logging user actions)")
print("- Scheduling and managing posts or events (e.g., blog posts, reminders)")
print("- Calculating durations and intervals (e.g., countdown timers, age calculations)")
print("- Formatting dates/times for display in various locales and formats")