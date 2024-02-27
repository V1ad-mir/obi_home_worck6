import subprocess
from validation import is_valid_ip, is_valid_domain
from result_writer import write_result
import logging
from datetime import datetime

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scan(target):
    try:
        start_time = datetime.now()

        if is_valid_ip(target) or is_valid_domain(target):
            command = f"nmap -p 1-65535 -sV -v {target}"
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()

            if process.returncode == 0:
                result = output.decode()
            else:
                result = f"An error occurred: {error.decode()}"
                logging.error(result)
        else:
            result = "Invalid input. Please enter a valid IP address or domain name."
            logging.error(result)


        filename = write_result(result)

        end_time = datetime.now()
        execution_time = end_time - start_time

        logging.info(f"Время начала выполнения: {start_time}")
        logging.info(f"Время окончания выполнения: {end_time}")
        logging.info(f"Время выполнения: {execution_time}")

        print(f"Результаты сканирования сохранены в файле: {filename}")
    except Exception as e:
        logging.exception("An error occurred:")
        raise e

target = input("Введите целевой IP-адрес или доменное имя: ")
scan(target)