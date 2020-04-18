# BFS algorithm is particularly useful for one thing:
# finding the shortest path on unweighted graphs

data1 = [
            [1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 0, 0, 1, 1, 1, 0],
            [0, 0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 1]
        ]


def BFS(input, output=[], index=0, start=0):
    pro_input = input[index]
    end_range = 8 - index
    if end_range <= 1:
        return 0
    for i in range(1, end_range):
        j = i+index
        if pro_input[j] == 1:
            if j not in output:
                output.append(j)
                print(start)
                print(output)
    start += 1
    BFS(input, output, index=output[start-1], start=start)
    print(output)

BFS(data1)
