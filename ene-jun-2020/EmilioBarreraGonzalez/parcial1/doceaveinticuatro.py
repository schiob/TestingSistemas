def transform(time: str):
    trans = time.split(":")
    ampm= trans[1]
    if ampm[2]=='a' and int(trans[0]) > 12:
        return 'NOT A VALID TIME, please try again'
    elif ampm[2]=='a' and int(trans[0])==12:
        trans[0]='00'
        return f"{trans[0]}:{ampm[0]}{ampm[1]}hrs"
    elif ampm[2]=='p' and int(trans[0])<12:
        trans[0]=int(trans[0])+12
        return f"{trans[0]}:{ampm[0]}{ampm[1]}hrs"
    else:
        return f"{trans[0]}:{ampm[0]}{ampm[1]}hrs"

           


if __name__=="__main__":
    print(transform("12:00am"))
