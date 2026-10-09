def main():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{i}x{j}={i * j:2d}", end="  ")
        print()


if __name__ == "__main__":
    main()
