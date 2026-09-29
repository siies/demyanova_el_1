name_reactor = input()
count_reactor = input()
way = "C:/Users/demia/Desktop/demianova_el/project_2/task2_2/inventory.txt"
f = open(way, "w", encoding="utf-8")
print(f"реактив {name_reactor} поступил на склад в количстве {count_reactor} штук", file=f)
f.close()

f = open(way, "r", encoding="utf-8")
print(f.read())
f.close()