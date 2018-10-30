import time

beeper = 3


def beeper_bomb():
    timing = 1
    timing_times = 0
    timing_max = 3
    timing_acc = 2
    total_loops = 0
    max_loops = 1
    while True:
        if timing > 0.01 and timing_times != timing_max:
            print("sound on")
            time.sleep(timing)
            print("sound off")
            time.sleep(timing)
            timing_times += 1
        elif timing_times == timing_max:
            timing = timing / timing_acc
            timing_times = 0

        elif total_loops == max_loops:
            timing = 1
            total_loops += 1
            print(f"Bombs exploded: {total_loops}")
        else:
            print(f"Bombs exploded: {total_loops}")
            break
beeper_bomb()