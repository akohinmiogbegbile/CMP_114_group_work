def largest_number(numbers):

    biggest_num = numbers[0]

    for num in numbers:

        if num > biggest_num:

            biggest_num = num

    return biggest_num

print(largest_number([1,12,111,122,1222,1234,3]))
