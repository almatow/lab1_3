def bubble_sort(arr: list[float], reverse: bool = False) -> list[float]:
    a = arr[:]  # копия
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if (a[j] > a[j + 1] and not reverse) or (a[j] < a[j + 1] and reverse):
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def main() -> None:
    n = int(input("Введите n: ").strip())
    nums = [float(input(f"Введите число #{i+1}: ").strip()) for i in range(n)]

    direction = input("Сортировка (воз/убыв): ").strip().lower()
    reverse = direction in ("desc", "d", "убыв", "убывание", "down")

    sorted_nums = bubble_sort(nums, reverse=reverse)
    print("Результат:", sorted_nums)


if __name__ == "__main__":
    main()
