data1 = [
            [1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 0, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 1]
        ]


def DFS(input, output, index=0):
    j = index + 1
    pro_input = input[index]
    while(1):
        if j > 7:
            break
        if pro_input[j] == 1:
            if j not in output:
                output.append(j)
                DFS(input, output, index=j)
        j += 1
    print(output)


output = []
DFS(data1, output, index=0)




