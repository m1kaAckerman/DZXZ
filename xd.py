def max_berry_harvest(bushes):
    n = len(bushes)
    
    #esli na gryadke net kustov to vozvrashaem 0
    if n == 0:
        return 0

    #esli odin kust to kol-vo yagod
    if n == 1:
        return bushes[0]

    #spisok dlya max kol-va yagod
    max_harvest = [0] * n

    #init znacheniy dlya kustov chezazadacha)
    max_harvest[0] = bushes[0]
    max_harvest[1] = max(bushes[0], bushes[1])

    #max kol-vo yagod
    for i in range(2, n):
        max_harvest[i] = max(max_harvest[i-2] + bushes[i], max_harvest[i-1])

    #vozvat max kol-vo yagod
    return max_harvest[n-1]



bushes = [4, 1, 2, 9, 7, 3]
max_harvest = max_berry_harvest(bushes)
print(max_harvest)