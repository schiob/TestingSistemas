from joke import joke
from format import format

def app(URL):
    the_joke=joke(URL)
    joke_formated=format(the_joke)
    return joke_formated

if __name__ == '__main__':
    URL="https://sv443.net/jokeapi/category/Programming"
    print(app(URL))
