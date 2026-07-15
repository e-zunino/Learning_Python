def main():
    message = input('Please insert your string:').lower()
    print(message)

#To avoid calling the function twice when importing it
#in another file we can add a GUARD, namely a switch that decides whether
#to execute what is after it depending whether the current module is
# te entry point (in which case __name__==__main__) or not (in which case __name__==indoor) 

if __name__ == "__main__":
    main()