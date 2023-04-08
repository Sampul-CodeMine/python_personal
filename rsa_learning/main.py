def factorize(val: int) -> list | bool:
    local_factor = []
    i_fact = 2    
    if val < 2:
        return    
    for i in range(2, val + 1):
        for j in range(2, val//2):
            if i * j == val:
                local_factor.append((j, i))
    return local_factor


def is_prime(val: int) -> bool:
    for num in range(2, val):
        if val % num == 0:
            return False
    return val > 1


def get_factors(val: int) -> list:
    if is_prime(val):
        factor = val, 1
        return [(factor)]
    local_factor = factorize(val)
    return local_factor


def factors_are_prime(val: list) -> list | None:
    if len(val) == 1:
        return val
    for i in val:
        if is_prime(i[0]) and is_prime(i[1]):
            return i
    return


def read_from_file(file_name: str) -> None:
    try:
        with open(file_name) as file:
            line = file.readline()
            while line != "":
                number = int(line.split('\n')[0])
                factors = get_factors(number)
                prime_mult_fact = factors_are_prime(factors)
                print(f"Generated Number: {number}: ")
                print(f"The list of factor(s):\n{factors}")

                if prime_mult_fact is None:
                        print(f"{number} has no multiple factors that are both prime.\n")
                else:
                    print(f"{number} has prime multiple factors: {prime_mult_fact}\n")

                line = file.readline()
    except (FileNotFoundError, ValueError, TypeError) as err:
        print(err)


def use_random() -> None:
    lower_range = r.randint(5, 10)
    upper_range = r.randint(100, 1000)
    number_gen = r.randint(lower_range, upper_range)
    factors = get_factors(number_gen)
    prime_mult_fact = factors_are_prime(factors)
    print(f"Generated Number: {number_gen}: ")
    print(f"The list of factor(s):\n{factors}")

    if prime_mult_fact is None:
        print(f"{number_gen} has no multiple factors that are both prime.\n")
    else:
        print(f"{number_gen} has prime multiple factors: {prime_mult_fact}\n")



if __name__ == "__main__":
    from sys import argv
    import random as r

    if len(argv) == 2:
        filename = argv[1]
        read_from_file(filename)
    else:    
        use_random()
                
