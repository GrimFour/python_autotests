# func 1
def multiplication_table(number: int) -> list[str]:
    multiplier = 1
    result = []

    while multiplier * number <= 25:
        result.append(f"{number}x{multiplier}={number * multiplier}")
        multiplier += 1

    return result


# func 2
def plus(first_number: int, second_number: int) -> int:
    return first_number + second_number


# func 3
def avarage_func(some_list: list[float]) -> float:
    if not some_list:
        raise ValueError("List cannot be empty")

    total = sum(some_list)
    return total / len(some_list)


# func 4
def reverse_string(s: str) -> str:
    return s[::-1]


# func 5
def longest_word(list_of_words: list[str]) -> str | None:
    if not list_of_words:
        return None
    return max(list_of_words, key=len)


# func 6
def find_substring(str1: str, str2: str) -> int:
    if str2 == "":
        return 0

    for i in range(len(str1) - len(str2) + 1):
        if str1[i:i + len(str2)] == str2:
            return i
    return -1


# func 7
def final_temperature(
    first_part_of_the_day: int,
    second_part_of_the_day: int,
    third_part_of_the_day: int,
) -> int:
    return (
        first_part_of_the_day
        + second_part_of_the_day
        + third_part_of_the_day
    )


# func 8
def perimeter(
    first_side: int,
    second_side: int,
    third_side: int,
    fourth_side: int,
) -> int:
    return first_side + second_side + third_side + fourth_side


# func 9
def recordswaper(
    some_list: list,
    first_index: int,
    second_index: int,
) -> list:
    new_list = some_list.copy()
    new_list[first_index], new_list[second_index] = (
        new_list[second_index],
        new_list[first_index],
    )
    return new_list


# func 10
def has_more_than_10_unique_chars(text: str) -> bool:
    return len(set(text)) > 10
