Raj = ["Radha", "Nikhil", "Amala", "Ashwin"]
Suresh = ["Shreya", "Manu", "Geetha", "Suresh"]
Thothadri = ["Arjun", "Arya", "Deepa", "Mani"]
Josyula =  ["Rhea", "Rohan", "Radhika", "Ravi"]
f = open("fams.txt", "r")
bop = f.read()
print("Enter your name")
name = input()
if name in Raj:
    print("You are in the Raj family")
elif name in Suresh:
    print("You are in the Suresh family")
elif name in Thothadri: 
    print("You are in the Thothadri family")
elif name in Josyula:
    print("You are in the Josyula family")
else:
    print("I don't know you")
