print("Hello, Git")

print("Hello from AI Vietnam")
print("Hello from AI Vietnam 2")

print("Hello from AI Viet nam 3")
def phan_loai_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
    
    def main():
        print("Chương trình tính BMI")
        weight = float(input("Nhập cân nặng (kg): "))
        height = float(input("Nhập chiều cao (m): "))
        bmi = weight / (height ** 2)
        category = phan_loai_bmi(bmi)
        print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
        print(f"Phân loại: {category}")
    if __name__ == "__main__":
        main()