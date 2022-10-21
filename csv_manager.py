import csv

### Constants ###
QUESTIONS_INDEX: int = 0
ANSWERS_OFFSET: int = 3
QUESTIONS_OFFSET: int = 3
ANS_ERROR: int = -1

ANS_STR: str = [
    "Siempre",
    "Casi siempre",
    "Algunas veces",
    "Casi nunca",
    "Nunca",
]

ANS_VAL_UP: int = 0
ANS_VAL_DOWN: int = 1
ANS_VAL_YESNO: int = 2

ANS_VAL_NAN: int = -1

# Indicates the numerical value of the string answers
ANS_VAL_TYPE: int = [
    ANS_VAL_UP,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_UP,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_DOWN,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_DOWN,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_UP,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_YESNO,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_YESNO,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
    ANS_VAL_DOWN,
]


class CsvManager:
    __file_name: str = ""
    __report_txt: str = ""
    __is_valid: bool = False
    __questions_raw_data: list
    __questions_max_length: int = 0
    __answers_raw_data: list
    __answers_num_data: list = []
    __answers_num_avg: list = []
    __answers_num_total: list = []
    __overall_avg: float = 0
    __overall_total: int = 0

    def __init__(self, file_name):
        self.__file_name = file_name
        self.__is_valid = True

    def get_file(self) -> str:
        """Get the CSV file name"""
        return self.__file_name

    def get_report(self) -> str:
        return self.__report_txt

    def valid(self) -> bool:
        """True if the file is valid"""
        return self.__is_valid

    def __add_to_report(self, line: str):
        self.__report_txt += f"{line}\n"

    def generate_report(self) -> bool:
        """Generate the report"""
        if not (self.__extract_data()):
            return False
        if not (self.process_answers_nums()):
            return False
        if not (self.process_average_nums()):
            return False
        if not (self.process_total_nums()):
            return False
        if not (self.__populate_report()):
            return False
        return True

    def __extract_data(self) -> bool:
        """Extract questions and answers from CSV"""
        try:
            with open(self.__file_name, newline='') as csv_file:
                self.__answers_raw_data = list(csv.reader(csv_file))
            self.__questions_raw_data = self.__answers_raw_data[QUESTIONS_INDEX]
            self.__answers_raw_data.pop(QUESTIONS_INDEX)
            # Remove non-question fields:
            for _ in range(QUESTIONS_OFFSET):
                self.__questions_raw_data.pop(0)
            self.__questions_max_length = len(max(
                self.__questions_raw_data,
                key=len
            ))

            print(f"Extracted {len(self.__answers_raw_data)} answers")
        except:
            print("Error extracting data from CSV")
            return False
        return True

    def process_answers_nums(self) -> bool:
        """Translate text answers to numerical answers"""
        for index, ans_str_list in enumerate(self.__answers_raw_data):
            ans_nums: list = []
            for ans_index in range(len(ANS_VAL_TYPE)):
                ans_str: str = ans_str_list[ans_index + ANSWERS_OFFSET]
                value: int = self.__get_answ_num(ans_str, ans_index)
                # print(f"Ans {ans_str} in index {index} has value of {value}")
                ans_nums.insert(ans_index, value)
            self.__answers_num_data.insert(index, ans_nums)
        return True

    def __get_answ_num(self, ans_str: str, index: int) -> int:
        """Get the numerical value of a string answer"""
        value: int = ANS_ERROR

        if (ANS_VAL_YESNO == ANS_VAL_TYPE[index]) or (ans_str == ''):
            value = 0
        else:
            try:
                if (ANS_VAL_UP == ANS_VAL_TYPE[index]):
                    value = ANS_STR.index(ans_str)
                elif (ANS_VAL_DOWN == ANS_VAL_TYPE[index]):
                    value = len(ANS_STR) - ANS_STR.index(ans_str) - 1
            except:
                pass
        if (ANS_ERROR == value):
            print(f"Answer {ans_str} not valid")
        return value

    def __is_question_numerical(self, index: int) -> bool:
        val_type: int = ANS_VAL_TYPE[index]
        if (val_type == ANS_VAL_UP) or (val_type == ANS_VAL_DOWN):
            return True
        else:
            return False

    def process_average_nums(self) -> bool:
        """Get the average numbers"""
        for ans_index in range(len(ANS_VAL_TYPE)):
            val_total: int = 0
            val_avg: float = 0
            val_num: int = 0
            if self.__is_question_numerical(ans_index):
                for ans_val in self.__answers_num_data:
                    val_total += ans_val[ans_index]
                    val_num += 1
                val_avg = val_total / val_num
            self.__answers_num_avg.insert(ans_index, val_avg)
            self.__answers_num_total.insert(ans_index, val_total)

            # message: str = f"Question {ans_index} "
            # message += f"avg: {self.__answers_num_avg[ans_index]:.2},\t"
            # message += f"total: {self.__answers_num_total[ans_index]}"
            # print(message)

        return True

    def process_total_nums(self) -> bool:
        """Get the overall numbers"""
        val_num: int = 0
        self.__overall_total = 0
        for index, value in enumerate(self.__answers_num_total):
            if (self.__is_question_numerical(index)):
                self.__overall_total += value
                val_num += 1
        self.__overall_avg = self.__overall_total / \
            len(self.__answers_raw_data)
        return True

    def __populate_report(self) -> bool:
        """Populate the text report"""
        # Write title
        line: str = self.__pad_text_1st_column("PREGUNTA,", "-")
        line += "PROM,---TOTAL\n"
        self.__add_to_report(line)

        for ans_index in range(len(ANS_VAL_TYPE)):
            # Write all the questions lines
            question_str: str = f"{self.__questions_raw_data[ans_index]},"
            line = f"{self.__pad_text_1st_column(question_str)}"
            if (self.__is_question_numerical(ans_index)):
                line += f"{self.__answers_num_avg[ans_index]:.4f}, "
                line += f"{self.__answers_num_total[ans_index]}"
            self.__add_to_report(line)

        # Write the TOTAL line
        self.__add_to_report("")
        line = self.__pad_text_1st_column("TOTAL,")
        line += f"{self.__overall_avg:.4f}, {self.__overall_total}"
        self.__add_to_report(line)

        return True

    def __pad_text_1st_column(self, text: str, pad_char: str = " ") -> str:
        # Add 2 to account for the comma, and an extra space
        pad_len: int = self.__questions_max_length - len(text) + 2
        for _ in range(pad_len):
            text += pad_char
        return text
