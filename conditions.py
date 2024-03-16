def main():
    # user to input their age
    age = int(input("Enter your age: "))

    # Check eligibility to vote
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

if __name__ == "__main__":
    main()