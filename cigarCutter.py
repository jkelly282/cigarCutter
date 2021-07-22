import re


def create_sequence(total_sequence):
    top_sequnece = []
    bottom_sequnece = []
    for i in total_sequence:
        if i[0] =='M':
            for i in range(int(i[1])):
                top_sequnece.append('M')
                bottom_sequnece.append('M')

        elif i[0] == 'D':
            for i in range(int(i[1])):
                top_sequnece.append('D')
                bottom_sequnece.append(' ')
        elif i[0] == 'I':
            for i in range(int(i[1])):
                top_sequnece.append(' ')
                bottom_sequnece.append('I')

    print('A representation of the sequence:\n')

    print(''.join(top_sequnece))
    print(''.join(bottom_sequnece))



def calculate_matching_sequences(parsed_cigar, total_length):
    total_matching = 0
    for i in parsed_cigar:
        if i[0] == 'M':
            total_matching += i[1]
    total_matching_percentage = total_matching/total_length
    return total_matching_percentage


def cigarcutter(cigar_string: str):
    all_integer  = re.findall('[0-9]\d*', cigar_string)
    all_character = re.findall('[a-zA-Z]', cigar_string)
    all_integer = list(map(int, all_integer))
    total_matching = calculate_matching_sequences(zip(all_character, all_integer), sum(all_integer))
    print(f'The total length of the sequence is {sum(all_integer)} bases'
          f'\n\nThe total percentage of matching bases is: {total_matching*100}%\n\n')
    create_sequence(zip(all_character, all_integer))

if __name__ == '__main__':
    test_cigar = '8M4I4M1D3M'
    cigarcutter(test_cigar)