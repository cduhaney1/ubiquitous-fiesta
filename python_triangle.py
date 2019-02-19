size = 5
k = (2 * size) - 2
for i in range(0, size):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
                print("* ", end=" ")
        print("\r ")

