f_read = open("自嘲诗.txt", encoding="utf8")
f_write = open("自嘲诗2.txt", mode="w", encoding="utf8")

for line in f_read:
    new_line = line.replace("\n", ".\n")
    # print(repr(line.strip()+".\n"))
    # file = line.strip()+".\n"
    f_write.write(new_line)
f_read.close()
f_write.close()





