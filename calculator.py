def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("除数不能为 0")
    return a / b

def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("除数不能为 0")
    return a % b

def power(a, b):
    return a ** b

def calculator():
    print("Python 计算器")
    print("支持：+  -  *  /  %  **")
    print("输入 'q' 可退出\n")

    while True:
        try:
            user_input = input("请输入表达式（例如：3 + 5）：").strip()

            if user_input.lower() == 'q':
                print("已退出计算器。")
                break

            # 解析表达式：数字 + 运算符 + 数字
            parts = user_input.split()
            if len(parts) != 3:
                print("格式错误，请输入类似：3 + 5")
                continue

            a_str, op, b_str = parts
            a = float(a_str)
            b = float(b_str)

            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)
            elif op == '%':
                result = mod(a, b)
            elif op == '**':
                result = power(a, b)
            else:
                print("不支持的运算符：", op)
                continue

            print(f"结果：{result}\n")

        except ValueError:
            print("输入错误，请确保使用数字和正确运算符。\n")
        except ZeroDivisionError as e:
            print(e, "\n")
        except Exception as e:
            print("发生错误：", e, "\n")


if __name__ == "__main__":
    calculator()