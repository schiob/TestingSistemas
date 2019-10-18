from joke import joke

def format(URL):
   
    r=joke(URL)

    print(type(r))

    # if 'delivery' in r:
    #     print('delivery: ',r.get('delivery'))
    # elif 'joke' in r:
    #     print('joke: ',r.get('joke'))
 
    # else:
    #     print(r)

if __name__ == '__main__':
	URL="https://sv443.net/jokeapi/category/Programming"
	format(URL)


