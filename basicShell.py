import os
import psutil
import time


while True:
    command = input("> ")

    if command == "exit":
        break

    elif command == "pwd":
        print (os.getcwd())

    elif command == "ls":
        print (os.listdir(os.getcwd()))

    elif command.startswith('echo "') and command.endswith('"'):
        output = command.split('echo "', 1)[1][:-1]
        print (output)

    elif command == "top":
        try:
            while True:
                os.system('cls')
                print ("process name        pid        mem        cpu")
                for proc in psutil.process_iter():
                    try:
                        print(f"{proc.name()}      {proc.pid}       {proc.memory_percent()}       {proc.cpu_percent()}")
                    except (psutil.NoSuchProcess):
                        pass
                time.sleep(4)


        except KeyboardInterrupt:
            print("You pressed ctrl + c")

    else:
        print ("Command not found")
















