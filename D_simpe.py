"""wg forge task-D"""
#!/usr/bin/python2
import sys

from IPython import embed

def add_hours_girl(stay_hours, start_interval_number):
    for count_hours in range(stay_hours, 0, -1):
        for index in range(start_interval_number, int(K)):
            range_list = INPUT_RANGES[index]
            if count_hours in range(int(range_list[0]), int(range_list[-1]) + 1):
                if WORKED[-1] == 'Vika':
                    SECOND_GIRL['worked_hours'].append(
                        count_hours - sum(FIRST_GIRL['worked_hours'])
                    )
                    WORKED.append('Alisa')
                    return index
                else:
                    FIRST_GIRL['worked_hours'].append(
                        count_hours - sum(SECOND_GIRL['worked_hours'])
                    )
                    WORKED.append('Vika')
                    return index
            elif int(range_list[0]) > count_hours:
                break

if __name__ == "__main__":
    N, K = raw_input().split(' ')

    INPUT_RANGES = []
    for index in range(int(K)):
        range_list = raw_input().split(' ')
        INPUT_RANGES.append(range_list)

    FIRST_GIRL = {'worked_hours': [], 'name': 'Vika'}
    SECOND_GIRL = {'worked_hours': [], 'name': 'Alisa'}
    WORKED = ['Vika']

    finded_hours = int(N)
    start_interval_number = 0

    while True:
        index = add_hours_girl(finded_hours, start_interval_number)

        if (sum(FIRST_GIRL['worked_hours']) == int(N)
            or sum(SECOND_GIRL['worked_hours']) == int(N)):
            print('Yes')
            print(len(WORKED) - 1)
            sys.exit(0)

        start_interval_number = index + 1

        girl_stay_hours = None
        if WORKED[-1] == 'Vika':
            girl_stay_hours = int(N) - sum(SECOND_GIRL['worked_hours'])
        else:
            girl_stay_hours = int(N) - sum(FIRST_GIRL['worked_hours'])


        finded_hours = (
            sum(FIRST_GIRL['worked_hours']) + 
            sum(SECOND_GIRL['worked_hours']) + 
            girl_stay_hours
        )

        if (start_interval_number == int(K)
            and sum(FIRST_GIRL['worked_hours']) != int(N) 
            and sum(SECOND_GIRL['worked_hours']) != int(N)):

            # if int(INPUT_RANGES[0][0]) == int(N) - girl_stay_hours:
            #     print('No')
            #     sys.exit(0)

            last_worked_hours = None
            last_girl_name = WORKED[-1]
            if FIRST_GIRL['name'] == last_girl_name:
                last_worked_hours = FIRST_GIRL['worked_hours']
                FIRST_GIRL['worked_hours'][-1] -= 1
            elif SECOND_GIRL['name'] == last_girl_name:
                last_worked_hours = SECOND_GIRL['worked_hours']
                SECOND_GIRL['worked_hours'][-1] -= 1

            if last_worked_hours >= 1:
                finded_hours -= 1
