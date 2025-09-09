while True:
    print("1) Add Lap")
    print("2) View Laps")
    print("3) Quit")

    choice = input("Please make an selection: ")


    if choice == "3":
        print("GoodBye!")
        break

    if choice == "1":
        driver_name = input("Enter Driver Name: ")
        lap_time = float(input("Enter Lap Time: "))
        
        with open("laps.txt", "a") as file:
             file.write(f"{driver_name} -> {lap_time}\n")
             print(f"Lap added: {driver_name} -> {lap_time}")


    if choice == "2":  
        try:
            with open("laps.txt", "r") as file:
                content = file.read()
                if content.strip() == "":
                    print("No laps recorded yet.")
                else: 
                    print(content.rstrip())
                    print("--- End Of Lap Log ---")   
        except FileNotFoundError:
         print("No lap log found yet.")        

