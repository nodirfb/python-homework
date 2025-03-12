from datetime import date,datetime,timedelta
import re
import pytz
# 1. Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

def age_calculator(birthdate):
    birthdate = datetime.strptime(date_str, '%Y-%m-%d').date()
    today = date.today()
    print(today)

    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day 

    if months <= 0:
        months = 12 + months
        years = years -1


    if days < 0:
        # days += (birthdate - birthdate.replace(month=birthdate.month -1)).days
        months -= 1
        last_month = birthdate.replace(day=1) - timedelta(days=1)
        days += last_month.day

    print(f"You are {years} years, {months} months, and {days} days old.")
        
# date_str = input("Enter your birthdate (YYYY-MM-DD): \n")
# age_calculator(date_str)



# 2. Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.


def until_next_birthdate(birthdate):
    birthdate = datetime.strptime(date_str, '%Y-%m-%d').date()
    today = date.today()
    try:
        this_years_birthday = birthdate.replace(year=today.year)
    except ValueError:
        # If Feb 29 is invalid, set to Feb 28
        this_years_birthday = date(today.year, 2, 28)

    # this_years_birthday = birthdate.replace(year=today.year)

    n = (this_years_birthday - today).days

    if n <= 0:
        n = (this_years_birthday.replace(year= today.year + 1) - today).days
        next_birthdate = today + timedelta(days=n)
        print(f'Until your next birthday: {n} days {next_birthdate}')
    else:
        next_birthdate = today + timedelta(days=n)
        print(f'Until your next birthday: {n} days {next_birthdate}')

# date_str = input("Enter your birthdate (YYYY-MM-DD): ").strip()
# until_next_birthdate(date_str)



# 3. Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

def meeting_scheduler(cur_date_time, duration):
    try:
        
        duration = timedelta(hours=duration)
        cur_date_time = datetime.strptime(cur_date_time,"%Y-%m-%d %H %M %S")
        print(f'The meeting will end in: {cur_date_time + duration}')
    except:
        print('Please enter a valid datetime format')

# cur_date_time = input('Enter the current date and time(YYYY-MM-DD hh mm ss)').strip()
# duration = int (input('duration of meeting in hours: '))
# meeting_scheduler(cur_date_time,duration)



# 4. Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.




# 5. Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).




# 6. Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

def email_validator(email):
    # nodirfayz18@gmail.com
    if re.search(r'^[\w\.?]+@([a-z]+\.)?[a-z]+\.[a-z]+$',email):
        print('valid')
    else:
        print('invalid')

# email = input('Input an email: ').strip().lower()
# email_validator(email)



# 7. Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to 
# "(123) 456-7890".

def phone_number_formatter(phone_number):
    sub = re.sub(r'(\d{3})(\d{3})(\d{4})',r'(\1) \2-\3',phone_number)
    print(sub)
# phone_number = input('Input a phone number 10 digits: ').strip()
# phone_number_formatter(phone_number)

# 8. Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

def password_checker(password):
    len = len(password) >= 8
    match1 = re.search(r'[a-z]',password)
    match2 = re.search(r'[A-Z]',password)
    match3 = re.search(r'\d',password)

    if len and match1 and match2 and match3:
        print('valid')
    else:
        print("invalid")

# password = input('Create a password: ')
# password_checker(password)

# 9. Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.


text = 'Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word input all of '

def word_finder(word):
    l = re.findall(word,text)
    print(l)

# word = input('Input a word: ')
# word_finder(word)

# 10. Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.



def date_extractor(text):
    l = re.findall(r'(\d{4}/\d{2}/\d{2}|\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4})',text)
    print(l)
# text = input('Input a text: ')
# date_extractor(text)
