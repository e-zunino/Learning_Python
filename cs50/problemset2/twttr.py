# When texting or tweeting, it’s not uncommon to shorten words to save time or space, 
# as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py,
#  implement a program that prompts the user for a str of text and then outputs that same text 
# but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():
    # Using a set makes the membership check particularly fast
    vowels = set('aeiouAEIOU')
    text = input('Insert a tweet: ')
    tweet = ''.join('' if letter in vowels else letter for letter in text)

    print(tweet)


main()