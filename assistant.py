from datetime import datetime
import webbrowser

greet=["hi","hello","hii","hey","hi there","hello there"]
chat=True

while chat:
    user_msg=input("Enter your message : ").lower()
    if user_msg in greet:
        print("Hello user, how may I help you?")
    elif "calculate" in user_msg or "evaluate" in user_msg or "solve" in user_msg:
        eq=user_msg.split()[1]
        print(eval(eq))
    elif "date" in user_msg:
        print(f"Today's date is : {datetime.now().date()}")
    elif "time" in user_msg:
        current_time=datetime.now().time()
        print(f"Time is :",current_time.strftime("%I:%M:%S %p"))
    elif "open" in user_msg:
        site=user_msg.split()[1]
        webbrowser.open(f"https://www.{site}.com")
    elif "bye" in user_msg:
        chat=False
    else:
        print("I cannot understand")
