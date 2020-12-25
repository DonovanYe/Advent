def run():
    filename = 'input_1_1.txt'

    with open(filename, 'r') as infile:
        num_list = infile.readlines()

    complement = {}
    for num in num_list:
        n = int(num)
        if n in complement:
            return (n * complement[n])
        else:
            complement[2020-n] = n

if __name__ == '__main__':
    print(run())