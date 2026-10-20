from datetime import date, datetime

def main():
    print("=" * 40)
    print("       GKS-UG 2027 ELIGIBILITY CHECKER")
    print("=" * 40)
    print()

    while True:
        try:
            birthdate = datetime.strptime(input("Enter your date of birth (DD/MM/YYYY): ").strip(), "%d/%m/%Y").date()

            if birthdate > date.today():
                print("date of birth cannot be in the future.")
            else:
                break
        except ValueError:
            print("please enter valid date of birth in DD/MM/YYYY format")
    age = check_age(birthdate)

    while True:
        try:
            grade = float(input("Enter your high school average score in percentage: "))

            if grade < 0 or grade > 100:
                print("Please enter a valid percentage between 0 and 100")
            else:
                break
        except ValueError:
            print("please enter valid percentage")
    percentage = check_grades(grade)


    country = input("Which country are you from?").strip().title()
    nationality = check_nationality(country)

    print("\nChecking your eligibility...\n")
    print("*" *40)
    print(age)
    print("*" *40)
    print(percentage)
    print("*" *40)
    print(nationality)
    print("✨" *3)


def check_age(birthdate):
    if birthdate >= date(2002, 3, 1):
        return "✓ Age requirement satisfied"
    else:
        return "✗ You must be born on or after 1 March 2002"


def check_grades(grade):
    if grade >= 90:
        return "✓ Excellent, you are well above the required percentage"
    elif grade >= 80:
        return "✓ Grade requirement satisfied"
    else:
        return "✗ Your score is below the required percentage"


def check_nationality(country):
  embassy_countries = {
                         "Afghanistan","Angola","Azerbaijan","Bahamas","Bangladesh","Bolivia","Brazil","Brunei","Bulgaria","Cambodia","Canada","Chile",
                         "Colombia","Costa Rica","Cuba","Czech Republic","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea",
                         "Ethiopia","Fiji","Gabon","Ghana","Guatemala","India","Indonesia","Iran","Iraq","Jordan","Kazakhstan","Kenya",
                         "Kyrgyzstan","Laos","Madagascar","Malaysia","Mexico","Mongolia","Morocco","Mozambique","Myanmar","Nepal","Nigeria",
                         "Pakistan","Panama","Paraguay","Peru","Philippines","Poland","Russia","Rwanda","Saudi Arabia","Singapore","South Africa",
                         "South Sudan","Sri Lanka","Sweden","Syria","Tajikistan","Tanzania","Thailand","Timor-Leste","Trinidad and Tobago",
                         "Turkiye","Turkmenistan","Uganda","Ukraine","Uruguay","Uzbekistan","Venezuela","Vietnam",
                         "Yemen", "Zimbabwe"
                     }
  if country in embassy_countries:
    return "✓ You can apply through both Embassy and University track"
  elif country == "South Korea":
    return "✗ Korean citizens cannot apply for this scholarship."
  else:
    return "✓ You can only apply through university track"

if __name__ == "__main__":
         main()
