import pyautogui
import time
import pyperclip
from openai import OpenAI

# • pyautogui: To control the mouse and
# keyboard automatically.
# • time: add elays in code
# • pyperclip:to copy paste text easily
# • openai:to connect api




client = OpenAI(
  api_key="sk-proj-e-8A1PS4uHjhlQwWfsqDH5kvMPezfHP7qZNXolYYtHzGEQL1j19cxUe1P9VLB_T3BlbkFJjmOx6phViv-OM5RnCuV_W_XQlZg8X7CsHIXpZA6lEnn4yl8pp6TVPQWwDFTcW6dSiCrAA", #your_api_key
)

def is_last_message_from_sender(chat_log, sender_name="Prerak"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False
    
        

    #  Click on the chrome icon at coordinates (1639, 1412)
pyautogui.click(1208,1043)

time.sleep(1)  
while True:
    time.sleep(5)
    # Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(922,307)
    pyautogui.dragTo(1875,886, duration=2.0, button='left')  # Drag for 1 second

    #Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  
    pyautogui.click(894, 364)

    # Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named Rishabh who speaks hindi as well as english.you are currently in BVCOE college in 4th year. You are from India and you are a coder. You analyze chat history and talk with others in formal manner. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Rohan Das: "},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)


        #  Click at coordinates (1808, 1328)
        pyautogui.click(1240, 960)
        time.sleep(1)  

        # Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  
        #  Press Enter
        pyautogui.press('enter')