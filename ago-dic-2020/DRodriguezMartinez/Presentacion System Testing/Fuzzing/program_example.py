def program_example(sentence: str):
    ''' metodo que regresa el valor de la operacion numerica en forma de string'''

    return eval(sentence)
    
if __name__ == "__main__":
    sentence = input()

    # print(program_example(sentence))
    print("Valid sentence:", sentence, "\n")