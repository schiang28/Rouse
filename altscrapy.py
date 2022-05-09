from csv import writer


def append_list_as_row(file_name, list_of_elem):
    with open(file_name, "a+", newline="") as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)
        write_obj.close()


fields = [
    "Name",
    "%pts won-serve",
    "%pts won-receive",
    "%pts won-shortrally",
    "%pts won-longrally",
    "%pts won-FH",
    "%pts won-BH",
    "rank",
    "won",
]

with open("testdata.txt") as f:
    file = [i for i in f.read().splitlines() if i]
file = file[: file.index("ALL STROKES")]
# print(file)

p1, p2 = file[2], file[3]

winnings = file.index("WINNINGS")
p1_serve_win_percent = round(float(file[winnings + 2].split()[0][:-1]) / 100, 3)
p1_receive_win_percent = round(1 - p1_serve_win_percent, 3)
p2_serve_win_percent = round(float(file[winnings + 6].split()[0][:-1]) / 100, 3)
p2_receive_win_percent = round(1 - p2_serve_win_percent, 3)

# print(p1_serve_win_percent, p1_receive_win_percent)
# print(p2_serve_win_percent, p2_receive_win_percent)

rally_type = file.index("WINNINGS IN SHORT/LONG RALLY")
p1_short_rally = round(float(file[rally_type + 2].split()[0][:-1]) / 100, 3)
p1_long_rally = round(1 - p1_short_rally, 3)
p2_short_rally = round(float(file[rally_type + 6].split()[0][:-1]) / 100, 3)
p2_long_rally = round(1 - p2_short_rally, 3)

# print(p1_short_rally, p1_long_rally)
# print(p2_short_rally, p2_long_rally)

stroke = file.index("WINNING STROKES SIDE")
p1_fore_win = round(float(file[stroke + 2].split()[0][:-1]) / 100, 3)
p1_back_win = round(1 - p1_fore_win, 3)
p2_fore_win = round(float(file[stroke + 6].split()[0][:-1]) / 100, 3)
p2_back_win = round(1 - p2_fore_win, 3)

# print(p1_fore_win, p1_back_win)
# print(p2_fore_win, p2_back_win)

rank = file.index("RATING")
p1_rank = int(file[rank + 1])
p2_rank = int(file[rank + 2])

p1set, p2set = int(file[4]), int(file[6])
if p1set > p2set:
    p1win = 1
    p2win = 0
else:
    p2win = 1
    p1win = 0

p1_info = [
    p1,
    p1_serve_win_percent,
    p1_receive_win_percent,
    p1_short_rally,
    p1_long_rally,
    p1_fore_win,
    p1_back_win,
    p1_rank,
    p1win,
]
p2_info = [
    p2,
    p2_serve_win_percent,
    p2_receive_win_percent,
    p2_short_rally,
    p2_long_rally,
    p2_fore_win,
    p2_back_win,
    p2_rank,
    p2win,
]


append_list_as_row("testtable.csv", p1_info)
append_list_as_row("testtable.csv", p2_info)
