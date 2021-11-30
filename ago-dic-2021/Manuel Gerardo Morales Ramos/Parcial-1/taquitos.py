def calculate_price(orders: list[str]) -> int:
    tacos = {
        "cachete": 13,
        "lengua": 10,
        "tripitas": 9,
        "pastor": 15,
        "machito": 14,
    }

    total = 0

    for order in orders:
        total += tacos[order]

    return total



def main():
    n = input().split(" ")

    if 0 < len(n) <= 30:
        print(calculate_price(n))
    else:
        raise ValueError("Sólo puedes pedir un máximo de 30.")

if __name__ == '__main__':
    main()