import pyautogui
import time

# Function to send a message a specific number of times

def spam_message(message, repeat_count, delay=0.5):
    for _ in range(repeat_count):
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        time.sleep(delay)

# Main function to get user input and call the spam function
def main():
    message = input("Enter the message you want to print: ")
    repeat_count = int(input("Enter the number of times to repeat the message: "))
    delay = float(input("Enter the delay between messages in seconds: "))
    print("You have 5 seconds to focus the target application window...")
    time.sleep(5)  # Give the user time to focus the target application window
    spam_message(message, repeat_count, delay)

# Run the main function
if __name__ == "__main__":
    main()

