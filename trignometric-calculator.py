import math

def main():
    print("Trigonometric Calculator (degrees)")
    print("Supported functions: sin, cos, tan, cot, sec, csc")

    while True:
        func = input("\nEnter function (e.g., sin, cos): ").strip().lower()
        angle_deg = float(input("Enter angle in degrees: "))
        angle_rad = math.radians(angle_deg)

        try:
            if func == "sin":
                result = math.sin(angle_rad)
            elif func == "cos":
                result = math.cos(angle_rad)
            elif func == "tan":
                result = math.tan(angle_rad)
            elif func == "cot":
                result = 1 / math.tan(angle_rad)
            elif func == "sec":
                result = 1 / math.cos(angle_rad)
            elif func == "csc":
                result = 1 / math.sin(angle_rad)
            else:
                print("Unsupported function.")
                continue

            print(f"{func}({angle_deg}°) = {result:.6f}")
        except ZeroDivisionError:
            print(f"{func}({angle_deg}°) is undefined (division by zero).")

        again = input("Do you want to compute another? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
