#1234
cho = "yes"
while(cho != "quit"):
    print("Enter four numbers")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    swap = "true"
    swamp = 0
    while (swap == "true"):
        if n1 < n2:
            swap = "false"
            if n2 < n3:
                swap = "false" 
                if n3 < n4:
                    swap = "false"
                else:
                    swamp = n4
                    n4 = n3
                    n3 = swamp
                    swap = "true"
            else:
                swamp = n3
                n3 = n2
                n2 = swamp
                swap = "true" 
        else:
            swamp = n2
            n2 = n1
            n1 = swamp
            swap = "true"
    print(n1, n2, n3, n4)
    cho = input()
