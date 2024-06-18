import sys


class Solution:
    def __init__(self, number_of_days_allowed_to_miss_class):
        self.prob_to_miss_grad = 0
        self.last_day_miss = 0
        self.number_of_days_allowed_to_miss_class = number_of_days_allowed_to_miss_class

    def get_probability_of_attendance(self,prev_attendance, curr_attendance, missing_attendance, number_of_days, attendance, miss_flag):

        # If missed days exceed allowed missed days, set miss flag to True and return
        if missing_attendance >= number_of_days_allowed_to_miss_class:
            miss_flag = True
            return

        # If reached the total number of days, evaluate the attendance string
        if number_of_days == attendance:
            attendance_str = prev_attendance + curr_attendance
            if miss_flag:
                return
            if curr_attendance == 'A':
                self.last_day_miss += 1
            self.prob_to_miss_grad += 1
            return

        # Recursive calls for both present ('P') and absent ('A') scenarios
        self.get_probability_of_attendance(prev_attendance=prev_attendance+curr_attendance, curr_attendance="P",
                                missing_attendance=0, number_of_days=number_of_days+1, attendance=attendance, miss_flag=miss_flag)

        self.get_probability_of_attendance(prev_attendance=prev_attendance+curr_attendance, curr_attendance="A",
                                missing_attendance=missing_attendance+1, number_of_days=number_of_days+1, attendance=attendance, miss_flag=miss_flag)
        return

def read_cmd_argument(arg_index, arg_name):
    try:
        value = int(sys.argv[arg_index])
    except (IndexError, ValueError):
        print(f"Please pass valid {arg_name} argument in command line")
        sys.exit(0)
    
    return value
    

if __name__ == "__main__":
        number_of_days_allowed_to_miss_class = 4
        days = read_cmd_argument(arg_name='days', arg_index=1)

        if len(sys.argv) > 2:
            number_of_days_allowed_to_miss_class = read_cmd_argument(arg_name='number_of_days_allowed_to_miss_class', arg_index=2)

        print("Number of days is {}".format(days))
        print("Number of days allowed to miss class is {}".format(number_of_days_allowed_to_miss_class))

        solution = Solution(number_of_days_allowed_to_miss_class=number_of_days_allowed_to_miss_class)
        result = solution.get_probability_of_attendance("", "", 0, 0, days, False)
        
        print(str(solution.last_day_miss)+'/'+str(solution.prob_to_miss_grad))

