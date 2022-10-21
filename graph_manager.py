from matplotlib import pyplot as plt

def create_histogram(ans_list: list) -> bool:

    plt.hist(ans_list)
    plt.show()

    return True
