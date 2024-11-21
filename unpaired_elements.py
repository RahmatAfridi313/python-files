def soultion(list_A):
    unpaired_elements = []
    for i in range(len(list_A)):
        count = 0
        for j in range(len(list_A)):
            if list_A[i] == list_A[j]:
                count += 1
        if count % 2 != 0 and list_A[i] not in unpaired_elements:
            unpaired_elements.append(list_A[i])
    print(f"the unpaired elements are {unpaired_elements}")
list_A = [1, 3, 1, 4, 3, 4, 5, 6, 6,]

soultion(list_A)
        