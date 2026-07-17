def main():
    camel_text = input('Insert your camelCase string: ')
    snake_text = camel_to_snake(camel_text)
    snake_text_compr = camel_to_snake_comprehension(camel_text)
    print(snake_text)
    print(snake_text_compr)


def camel_to_snake(camel_text: str) -> str:
    snake_chars = []

    for char in camel_text:
        if char.isupper():
            snake_chars.append('_' + char.lower())
        else:
            snake_chars.append(char)

    return "".join(snake_chars)


# Using list comprehension we can give a very succint solution
def camel_to_snake_comprehension(camel_text: str) -> str:
    return "".join('_' + camel_char.lower() if camel_char.isupper() else camel_char for camel_char in camel_text)


if __name__ == "__main__":
    main()