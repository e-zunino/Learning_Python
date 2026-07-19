def main():
    counts = {}

    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            break

        counts[item] = counts.get(item, 0) + 1

    for item in sorted(counts):
        print(counts[item], item)


if __name__ == "__main__":
    main()