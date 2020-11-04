import random

def simple_fuzzer(max_length=100, char_start=32, char_range=32) -> str:
    string_length = random.randrange(0, max_length + 1)

    out = ""
    for _ in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))

    return out

####

if __name__ == "__main__":
    print(simple_fuzzer())
    # print(simple_fuzzer(1000, ord('a'), 26))