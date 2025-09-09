drivers = ["Lewis","Max","Lando"]
lap_times = {
    "Lewis" : 96.571,
    "Max" : 95.290,
    "Lando" : 94.261
}

while True:
    print("1.View All Drivers.")
    print("2. Add a Driver.")
    print("3. Quit Program.")

    choice = input("Please make an selection: ")

    if choice == "3":
        print("Goodbye!")
        break

    if choice == "1":
        for driver in drivers:
            if driver in lap_times:
                print(f"{driver} -> {lap_times[driver]}")
            else:
                print(f"Driver -> no Lap Time yet.")   
    if choice == "2":
     user_name = input("Enter New Driver: ")       
     lap_time = float(input("Enter Drivers Lap time: ")) 
     drivers.append(user_name)
     lap_times[user_name] = lap_time
     print(f"New Driver {user_name} -> Time {lap_time} added successfully!")