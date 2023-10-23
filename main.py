import psutil
import requests
import time

MEMORY_THRESHOLD_PERCENTAGE = 90

ALARM_API_URL = "http://example.com/api/alarm"


def check_memory_usage():
    memory_usage_percentage = psutil.virtual_memory().percent
    print(f"Текущее использование памяти: {memory_usage_percentage}%")

    if memory_usage_percentage > MEMORY_THRESHOLD_PERCENTAGE:
        response = requests.post(ALARM_API_URL, data={"message": "Использование памяти превысило порог!"})
        print(f"Предупреждение отправлено! Ответ: {response.status_code}")
    else:
        print("Текущее использование памяти в допустимых пределах.")


while True:
    check_memory_usage()
    time.sleep(60)
