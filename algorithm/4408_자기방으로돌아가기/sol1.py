import sys
sys.stdin = open("input.txt")

T = int(input())

def run_to_room(room_list):
    corridor = [0]*200

    for i in range(len(room_list)):
        if room_list[i][0] > room_list[i][1]:
            room_list[i][0], room_list[i][1] = room_list[i][1], room_list[i][0]

        for j in range(2):
            if room_list[i][j] % 2 == 1:
                room_list[i][j] = room_list[i][j] // 2
            else:
                room_list[i][j] = room_list[i][j] // 2 - 1

    for room in room_list:
        for slice_of_bread in range(room[0], room[1]+1):
            corridor[slice_of_bread] += 1

    return max(corridor)

for tc in range(1, T+1):
    N = int(input())
    room_list =[]
    for _ in range(N):
        room_list += [list(map(int, input().split()))]

    result = run_to_room(room_list)
    print("#{} {}".format(tc, result))

