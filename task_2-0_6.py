way = "C:/Users/demia/Desktop/demianova_el/task2/task_2-0_6/output.txt"
f = open(way, "w", encoding="utf-8")
print("инфа о себе: зайцы топ, физика фу, хочу кота, люблю апельсиновый сок", file=f)
f.close()

f = open(way, "r", encoding="utf-8")
print(f.read())
f.close()