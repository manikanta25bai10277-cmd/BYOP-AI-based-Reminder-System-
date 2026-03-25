def log_data(message):
    with open("data.txt", "a") as file:
        file.write(message + "\n")