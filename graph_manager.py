from matplotlib import pyplot as plt
from csv_manager import *
import pandas as pd
import os

MAX_TITLE_LEN: int = 60


def create_histogram(ans_list: list, title: str, index: int, is_numerical: bool) -> bool:
    values: list = []
    keys: list
    if is_numerical:
        keys = ANS_NUM_STR
    else:
        keys = ANS_YESNO_STR
    for ans_index, ans in enumerate(keys):
        values.insert(ans_index, ans_list.count(ans))

    plt.bar(keys, values)
    plt.title(multi_line_title(title))
    plt.savefig(f"graficas/pregunta_{index:02}.png")
    # plt.show()
    plt.clf()
    plt.close()

    return True


def create_all_histograms(csv_man: CsvManager) -> bool:
    try:
        for index in range(ANS_NUM):
            create_histogram(
                csv_man.get_answers_list(index),
                csv_man.get_question_str(index),
                index,
                csv_man.is_question_numerical(index)
            )
    except:
        return False
    return True


def multi_line_title(title: str) -> str:
    if len(title) <= MAX_TITLE_LEN:
        return title
    else:
        multi_line_title: str
        # Find the last space before the one line limit
        nl_pos: int = title[0:MAX_TITLE_LEN].rfind(" ")
        multi_line_title = title[0:nl_pos]
        # Insert a new line in that space
        multi_line_title += os.linesep
        multi_line_title += title[nl_pos+1:len(title)]
        return multi_line_title
