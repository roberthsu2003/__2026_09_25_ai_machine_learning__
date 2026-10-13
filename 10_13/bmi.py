def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)


def get_bmi_status(bmi: float) -> str:
    # 依衛福部標準
    if bmi < 18.5:
        return "過輕"
    elif bmi < 24:
        return "正常"
    elif bmi < 27:
        return "過重"
    elif bmi < 30:
        return "輕度肥胖"
    elif bmi < 35:
        return "中度肥胖"
    else:
        return "重度肥胖"


def main():
    print("=== BMI 計算機 ===")
    try:
        height = float(input("請輸入身高（公分 cm）："))
        weight = float(input("請輸入體重（公斤 kg）："))
    except ValueError:
        print("輸入錯誤！請輸入數字。")
        return

    if height <= 0 or weight <= 0:
        print("身高與體重必須大於 0！")
        return

    bmi = calculate_bmi(weight, height)
    status = get_bmi_status(bmi)

    print(f"\n身高：{height} cm，體重：{weight} kg")
    print(f"你的 BMI 是：{bmi:.2f}")
    print(f"體位判定：{status}")


if __name__ == "__main__":
    main()
