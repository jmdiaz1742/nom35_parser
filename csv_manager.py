import csv

### Constants ###
QUESTIONS_INDEX: int = 0
ANSWERS_OFFSET: int = 3
ANS_ERROR: int = -1

ANS_STR: str = [
    "Siempre",
    "Casi siempre",
    "Algunas veces",
    "Casi nunca",
    "Nunca",
]

# Indicates the numerical value of the string answers
ANS_VAL_SIGN: bool = [
    True,
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
]


class CsvManager:
    __file_name: str = ""
    __is_valid: bool = False
    __questions_raw_data: list
    __answers_raw_data: list
    __answers_num_data: list = []

    def __init__(self, file_name):
        self.__file_name = file_name
        self.__is_valid = True

    def get_file(self) -> str:
        """Get the CSV file name"""
        return self.__file_name

    def valid(self) -> bool:
        """True if the file is valid"""
        return self.__is_valid

    def generate_report(self) -> bool:
        """Generate the report"""
        if not (self.__extract_data()):
            return False
        if not (self.__process_answers_nums()):
            return False
        return True

    def __extract_data(self) -> bool:
        """Extract questions and answers from CSV"""
        try:
            with open(self.__file_name, newline='') as csv_file:
                self.__answers_raw_data = list(csv.reader(csv_file))
            self.__questions_raw_data = self.__answers_raw_data[QUESTIONS_INDEX]
            self.__answers_raw_data.pop(QUESTIONS_INDEX)

            print(f"Extracted {len(self.__answers_raw_data)} answers")
        except:
            print("Error extracting data from CSV")
            return False
        return True

    def __process_answers_nums(self) -> bool:
        """Translate text answers to numerical answers"""
        for index, ans_str_list in enumerate(self.__answers_raw_data):
            ans_nums: list = []
            for ans_index in range(len(ANS_VAL_SIGN)):
                ans_str: str = ans_str_list[ANSWERS_OFFSET + ans_index]
                value: int = self.__get_answ_num(ans_str, ans_index)
                # print(f"Ans {ans_str} in index {index} has value of {value}")
                ans_nums.insert(ans_index, value)
            self.__answers_num_data.insert(index, ans_nums)
        return True

    def __get_answ_num(self, ans_str: str, index: int) -> int:
        value: int = ANS_ERROR

        if (ans_str in ANS_STR):
            if(ANS_VAL_SIGN[index]):
                value = ANS_STR.index(ans_str)
            else:
                value = len(ANS_STR) - ANS_STR.index(ans_str)
        else:
            print(f"Answer {ans_str} not valid")
        return value
