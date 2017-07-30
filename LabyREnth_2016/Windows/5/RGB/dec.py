"""
int value = this.sbR.Value;
int value2 = this.sbG.Value;
int value3 = this.sbB.Value;
int num = value2 * value3;
int num2 = value * 3;
if (value + num - value2 + value * value * value2 - value3 == value2 * (value3 * 34 + (num2 - value)) + 3744 && value > 60)
"""

value = 1
value2 = 2
value3 = 3
for value in range(0, 256):
    for value2 in range(0, 256):
        for value3 in range(0, 256):
            num = value2 * value3
            num2 = value * 3
            a1 = value + num - value2 + value * value * value2 - value3
            a2 = value2 * (value3 * 34 + (num2 - value)) + 3744
            if a1 == a2:
                print(value, value2, value3),

