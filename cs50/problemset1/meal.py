def main():
    time_str = input("What time is it? ").strip()

    try:
        current_time = convert(time_str)
    except ValueError:
        print("The time format is not correct.")
        return

    if 7.0 <= current_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= current_time <= 13.0:
        print("lunch time")
    elif 18.0 <= current_time <= 19.0:
        print("dinner time")


def convert(time_str: str) -> float:
    t = time_str.lower().strip()

    # check whether 12h format is used
    is_am = t.endswith("a.m.")
    is_pm = t.endswith("p.m.")

    # if 12h format is used then remove 'a.m.' or 'p.m.'
    if is_am or is_pm:
        t = t[:-4].strip()

    hours_str, sep, minutes_str = t.partition(":")
    if sep != ":": #if there is no : then raise an error
        raise ValueError("Missing ':'")

    hours = int(hours_str)
    minutes = int(minutes_str)

    # if minutes is more than 60 raise an error
    if not (0 <= minutes < 60):
        raise ValueError("Invalid minutes")

    # handle the hours conversion
    if is_am:
        if hours == 12:
            hours = 0
    elif is_pm:
        if hours != 12:
            hours += 12

    # handle hours error
    if not (0 <= hours <= 23):
        raise ValueError("Invalid hour")

    return hours + minutes / 60


if __name__ == "__main__":
    main()