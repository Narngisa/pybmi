def BMICalculate(weight: float, height: float) -> None:
    
    if height >= 50:
        height = height / 100

    return weight / (height * height)

def BMILevel(bmi: float) -> None:
    try:
        if bmi < 18.5:
            return "Level: Underweight"
        elif 18.5 <= bmi <= 24.9:
            return "Level: Normal"
        elif 25.0 <= bmi <= 29.9:
            return "Level: Overweight"
        elif 30.0 <= bmi <= 34.9:
            return "Level: Obesity class I"
        elif 35.0 <= bmi <= 39.9:
            return "Level: Obesity class II"
        else:
            return "Level: Obesity class III"
    except:
        return "Data is NoneType !!"

def BMITable() -> None:
    table = """\033[32m
        +---------------------+-------------------------+
        |        Level        |           BMI           |
        |---------------------+-------------------------|
        |   Underweight       |     less than 18.5      |
        |   Normal            |     18.5 - 24.9         |
        |   Overweight        |     18.5 - 24.9         |
        |   Obesity class I   |     18.5 - 24.9         |
        |   Obesity class II  |     18.5 - 24.9         |
        |   Obesity class III |     40 or more than     |
        +---------------------+-------------------------+
        \033[0m
    """
    return table