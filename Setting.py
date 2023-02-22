import math
def generate_prob(weights):
    sum = 0
    for x in weights:
        sum+=x
    div = sum
    sum = 0
    # math.floor(a * 100)/100.0
    for i in range(len(weights)):
        weights[i] = math.floor((weights[i]/div)*10000)/10000.0
        sum+=weights[i]
    # print(sum)
    sum = round(1.000-sum,4)
    # print(sum)
    weights[0] = round(weights[0]+sum,4)
    return weights

# cords = [[12,16,19],[14,17,21],[16,19,23],[17,21,24],[19,23,26],[21,24,28],[23,26,29]]
cords = [[12,16,19],[14,17,21],[16,19,23],[17,21,24],[19,23,26],[21,24,28]]
first_inv = [[cord[1],cord[2],cord[0]+12]for cord in cords]
second_inv = [[cord[2]-12,cord[0],cord[1]]for cord in cords]
cords = cords + first_inv[0:len(first_inv)] + second_inv[0:len(second_inv)]
cord_prob = generate_prob([10 for x in range(len(cords))])
cord_durations = [1,2,4]
cord_duration_prob = generate_prob([1,5,10])


notes = [5,7,9,11,12,14,16,17,19,21,23,24,26,28,29]
note_prob = generate_prob([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])


note_durations = [0.25,0.5,0.75,1.0,2.0]
note_duration_prob = generate_prob([40,40,30,20,10])