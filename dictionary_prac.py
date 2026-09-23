#this is dictionary practice, the first term is called the key, and the other item associated with it is called a value.


my_dict = {
    "keny":20,
    "ken":21,
    "hi":67
}


print(f"funny number {my_dict["hi"]}")

#the .get method requires a key in order to work. if it doesnt have one it will return none.  But if you enter a valid key it will return its value

print("keny's age is", my_dict.get("keny"))

#if you want to search for a key and its value inside a dictionary, python has a built in searcher kist using a if statement 

if "keny" in my_dict:
    print(my_dict["hi"])



# practice problem

device = {
    "hostname": "lab-ws-07",
    "os": "Ubuntu 22.04",
    "open_ports": [22, 80, 443],
    "risk_score": 12
}


print(f"host: {device['hostname']} running {device['os']}")
print(f"fields stored: {len(device)}")
print(device.keys)
name = input('username?: ')
device["owner"] = name
print(len(device))

new_port = int(input("enter a new port: "))
device["open_ports"].append(new_port)

num_of_extra_ports = len(device["open_ports"]) - 3

device["risk_score"] += num_of_extra_ports * 5
