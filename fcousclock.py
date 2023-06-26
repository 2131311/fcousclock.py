import time

def start_focus_timer(minutes):
    seconds = minutes * 60
    print(f"Focus timer started for {minutes} minutes.")

    while seconds > 0:
        minutes_remaining = seconds // 60
        seconds_remaining = seconds % 60
        time_remaining = f"{minutes_remaining:02d}:{seconds_remaining:02d}"
        print(f"Time remaining: {time_remaining}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("\nFocus timer ended.")

# 使用示例，设置一个专注时钟为 25 分钟
start_focus_timer(25)
