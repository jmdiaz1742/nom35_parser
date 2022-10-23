from matplotlib import pyplot as plt
from csv_manager import *
import pandas as pd


def create_histogram(ans_list: list, title: str, index: int) -> bool:
    print(f"Creating plot for question #{index}: {title}")
    values: list = []
    for ans_index, ans in enumerate(ANS_STR):
        values.insert(ans_index, ans_list.count(ans))
    plt.bar(ANS_STR, values)
    plt.title(title)
    plt.savefig(f"graficas/pregunta_{index:02}.png")
    plt.clf()
    # plt.show()
    plt.close()

    return True


def create_all_histograms(csv_man: CsvManager) -> bool:
    try:
        for index in range(0, csv_man.ANS_NUM - 1, 1):
            create_histogram(
                csv_man.get_answers_list(index),
                csv_man.get_question_str(index),
                index
            )
    except:
        return False
    return True
