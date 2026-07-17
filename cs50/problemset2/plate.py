# In this case, some conditions imply others, so it is better to start checking the most stringent to avoid errors

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    # Length must be between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # First two characters must be letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    number_started = False

    for char in s:
        # Only letters and numbers allowed
        if not char.isalnum():
            return False

        if char.isdigit():
            # First number cannot be 0
            if not number_started:
                if char == "0":
                    return False
                number_started = True
        else:
            # Once numbers start, no letters can appear
            if number_started:
                return False

    return True


main()