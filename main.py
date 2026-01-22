def bubble_sort(arr: list[float]) -> list[float]:
    a = arr[:]  # копия
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def main() -> None:
    n = int(input("Введите n: ").strip())
    nums = []
    for i in range(n):
        nums.append(float(input(f"Введите число #{i+1}: ").strip()))

    sorted_nums = bubble_sort(nums)
    print("Отсортировано по возрастанию:", sorted_nums)


if __name__ == "__main__":
    main()
