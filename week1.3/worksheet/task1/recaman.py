# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
sequence = []

for n in range(0,L):
    if n == 0:
        sequence.append(n)
    else:
        prev_n = sequence[n-1]
        n_case_1 = prev_n - n
        if n_case_1 > 0 and n_case_1 not in sequence:
            sequence.append(n_case_1)
        else:
            n_case_2 = prev_n + n
            sequence.append(n_case_2)

# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence