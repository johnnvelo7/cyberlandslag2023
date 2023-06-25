import sys
import signal

flag = "That is more than enough! Here is your flag: flag{aaaaaaaaaaaaaaaaaaaaaaaaaaa}"

def ignore_me_init_buffering():
    sys.stdout = None
    sys.stdin = None
    sys.stderr = None

def kill_on_timeout(signum, frame):
    if signum == signal.SIGALRM:
        print("[!] Anti DoS Signal. Patch me out for testing.")
        sys.exit(0)

def ignore_me_init_signal():
    signal.signal(signal.SIGALRM, kill_on_timeout)
    signal.alarm(60)

def printFlag():
    print(flag)

def win(amount):
    if amount > 0x100000000: # 4294967296
        printFlag()
    else:
        print("sorry, %d is not enough to win in this game." % amount)

def main():
    ignore_me_init_buffering()
    ignore_me_init_signal()
    print("Welcome to pay2win, the classical game where you can pay your way to victory!")
    print("How much are you willing to pay > ")
    input_value = input()
    sum_value = int(input_value)
    win(sum_value)

if __name__ == '__main__':
    main()

