def primeraparte(inom):
    if inom <= 0:
        return 'error'
    
    else:
        inomq = inom * ( inom + 1 ) / 2
        return inomq

if __name__ == "__main__":
    d= str("d")
    print( primeraparte(d))