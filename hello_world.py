# hello_world.py
import os
import datetime

def main():
    message = os.getenv('MESSAGE', 'No message provided')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Hello World at {current_time}!")
    print(f"Received message: {message}")

if __name__ == "__main__":
    main()
