def GasStation(strArr):
    num_stations = int(strArr[0])

    for start_station in range(num_stations):
        gas = 0
        completed = True

        for i in range(num_stations):
            j = (start_station + i) % num_stations + 1
            # station_gas, distance = map(int, strArr[station_index].split(':'))
            station_gas = int(strArr[j].split(":")[0])
            distance = int(strArr[j].split(":")[1])

            gas += station_gas - distance

            if gas < 0:
                completed = False
                break

        if completed:
            return str(start_station + 1)

    return "impossible"


# Example usage
arr = ["4", "0:1", "2:2", "1:2", "3:1"]

# arr = ["4","3:1","2:2","1:2","0:1"]
# arr = ["4","1:1","2:2","1:2","0:1"]
arr = ["4","0:1","2:2","1:2","3:1"]
print(GasStation(arr))  # Output: "4"
