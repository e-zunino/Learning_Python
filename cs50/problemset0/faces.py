def convert(message: str):
    mod = message.replace(':)','🙂').replace(':(','🙁')
    print(mod)
    

def main():
    message = input('Insert your string: ')
    convert(message)

if __name__ == "__main__":
    main()

                                                                 