# Python Developer Internship Application for Bilal Software House

def main():
    print("Welcome to the Python Developer Internship Application for Bilal Software House")
    print("Please enter your details below:")

    # Collect applicant's personal information
    name = input("Enter your full name: ")
    email = input("Enter your email address:")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")

    # Collect education background
    print("\nEducational Background:")
    highest_degree = input("Enter your highest degree obtained: ")
    university = input("Enter the name of the university: ")
    graduation_year = input("Enter your year of graduation: ")

    # Previous experience
    print("\nPrevious Experience:")
    experience = input("Do you have previous experience in Python? (yes/no): ")
    if experience.lower() == 'yes':
        experience_years = input("How many years of experience do you have with Python? ")
        last_job = input("What was your last job position? ")
    else:
        experience_years = 0
        last_job = "No previous job experience."

    # Display the application summary
    print("\nApplication Summary:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Address: {address}")
    print(f"Highest Degree: {highest_degree} from {university}, {graduation_year}")
    if experience.lower() == 'yes':
        print(f"Experience in Python: {experience_years} years")
        print(f"Last Job Position: {last_job}")
    else:
        print("Experience in Python: No previous experience.")

    # Confirmation
    print("\nThank you for applying. We will review your application and contact you via email.")

if __name__ == "__main__":
    main()
