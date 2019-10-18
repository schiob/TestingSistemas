def format(the_joke):

    if 'delivery' in the_joke:
        jokestr=""
        jokestr=jokestr+(str(the_joke.get('setup')))
        jokestr=jokestr+"\n"
        jokestr=jokestr+(str(the_joke.get('delivery')))
        return jokestr
    elif 'joke' in the_joke:
        return (str(the_joke.get('joke')))

    else:
        retrun(the_joke)
