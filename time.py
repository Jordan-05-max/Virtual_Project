from datetime import datetime

def Time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Current Time = {current_time}")

def Date():
    import datetime
    current_date = datetime.date.today().strftime("%d/%m/%Y")
    print(f"Current Date = {current_date}")

Time()
Date()