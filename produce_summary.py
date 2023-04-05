def melon_count (day_number,path): #create function and pass the day number and the path to the produce deliveries report

    print("Day" , day_number) #print each day
    print()

    delivery_log = open(path) #open de deliveries file

    for line in delivery_log: #go over each line in the file
        line = line.rstrip() #removes whitespace
        words = line.split('|') #creates a list of strings


        # assigned a variable to each item from the list
        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")  #prints out the information

    delivery_log.close()

#function calls using the given reports
melon_count(1,"um-deliveries-day-1.txt")
print()
melon_count(2,"um-deliveries-day-2.txt")
print()
melon_count(3,"um-deliveries-day-3.txt")
