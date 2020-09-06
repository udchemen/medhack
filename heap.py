import heapq

# In order to use heapq and have a maxheap, every number is converted to a negative value
# ex: 34 becomes -34

bleeding_dict = {"No": 0, "Little": 1, "Mild": 2, "Important": 3}

def sum_values(patients, i):
    bleeding_value = patients[i]['bleeding']
    # print(f"bleeding_value: {bleeding_value}")
    # print(patients[i]['breathing_difficulty'])
    # print(int(patients[i]['conscious'] != True))
    # print(patients[i]['pain'])
    # print(bleeding_dict[bleeding_value])
    # if conscious == False, give 1
    sum = patients[i]['breathing_difficulty']  + int(patients[i]['conscious'] == False) + patients[i]['pain'] + bleeding_dict[bleeding_value]
    return sum

# creating a dictionary with key: patient id and value: the sum of the
# numbers indicating patient health

order_patient = {}
def arrange_into_heap(patients):

    for i in range(len(patients)):
        print(patients[i])
        # make all values negative so that it's a max heap
        order_patient[patients[i]['id']] = - sum_values(patients, i)
    print(f"order_patient: {order_patient}")
    #heapify values of order_patient dict
    list_values = list(order_patient.values())
    arranged = heapq.heapify(list_values)
    # heapified values
    print(list_values)

    for l in list_values:
        print(l.get)
    #return person of highest priority
    priority = heapq.heappop(list_values)
    #print(pr)
    return priority





