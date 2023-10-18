def intersection_set():
    #elementi pervogo mnojestva
    n = int(input())
    m = int(input())

    #elementi vtorogo mnojestva
    set1 = set("perviy")
    print()
    for _ in range(n):
        element = int(input())
        set1.add(element)

    #elementi vtorogo mnojestva
    set2 = set()
    print("vtoroy")
    for _ in range(m):
        element = int(input())
        set2.add(element)

    #ishem peresechenie
    intersection = sorted(set1.intersection(set2))

    #result
    print("resultat peresecheniya")
    for element in intersection:
        print(element)

#vizov funkcii
intersection_set()