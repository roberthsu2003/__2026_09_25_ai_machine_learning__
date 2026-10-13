import random


def main():
    answer = random.randint(1, 100)
    attempts = 0
    minimum = 1
    maximum = 100

    print("猜數字遊戲！請猜一個 1 到 100 之間的整數。")

    while True:
        print(f"目前可猜範圍：{minimum} 到 {maximum}")
        try:
            guess = int(input("請輸入你的猜測："))
        except ValueError:
            print("請輸入有效的整數。")
            continue

        if not minimum <= guess <= maximum:
            print(f"請輸入目前範圍內的數字（{minimum} 到 {maximum}）。")
            continue

        attempts += 1

        if guess < answer:
            minimum = guess + 1
            print("太小了，再猜一次！")
        elif guess > answer:
            maximum = guess - 1
            print("太大了，再猜一次！")
        else:
            print(f"恭喜猜中了！答案是 {answer}，你總共猜了 {attempts} 次。")
            break


if __name__ == "__main__":
    main()