# Pybmi

<p align="center">
 <img width="1000" src="./pybmi.png" alt="PyBMI"/>
</p>

Pybmi is python module for calculate BMI, check level from BMI and table BMI on command line.

* Developed by Natthanan © 2024

# How to using python script ??

### BMICalculate

```python
import pybmi

weight = 70
height = 1.73

# height is centimeters or meters
print(pybmi.BMICalculate(weight, height))
```

### Output

```
23.38868655818771
```

### BMILevel

```python
import pybmi

bmi = 23.38868655818771

print(pybmi.BMILevel(bmi))
```

### Output

```
Level: Normal
```

### BMITable

```python
import pybmi

print(pybmi.BMITable())
```

### Output
```
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
```