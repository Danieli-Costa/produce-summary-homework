def melon_count (day_number,path):

    print("Day" , day_number)
    print()

    delivery_log = open(path)

    for line in delivery_log:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")

    delivery_log.close()


melon_count(1,"um-deliveries-day-1.txt")
print()
melon_count(2,"um-deliveries-day-2.txt")
print()
melon_count(3,"um-deliveries-day-3.txt")
