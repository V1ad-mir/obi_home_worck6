from datetime import datetime

def write_result(result):

    now = datetime.now()
    filename = now.strftime("%Y-%m-%d_%H-%M-%S.txt")


    with open(filename, "w") as file:
        file.write(result)

    return filename