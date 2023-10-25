data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]


def konversi_menit(minggu, hari, jam, menit):
    total_menit = (minggu * 7 * 24 * 60) + \
        (hari * 24 * 60) + (jam * 60) + menit
    return total_menit


def proses(data):
    value = data.split()
    minggu = int(value[0])
    hari = int(value[2])
    jam = int(value[4])
    menit = int(value[6])
    return konversi_menit(minggu, hari, jam, menit)


konvert = [proses(d) for d in data]

print(konvert)
