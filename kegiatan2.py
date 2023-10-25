data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


for value in data:
    list_data = value.split()
    integers = list(filter(is_int, list_data))
    print(integers)
