# Class 6

---

## L-Systems


### Koch Snowflake
[code](https://github.com/examon/iv122_math_code/blob/4091dad0481f3196c27dbe586036528392617243/class_6/code/lsystems.py#L40)

[animation](code/img/koch_snowflake_animate.svg)

```
axiom = "F--F--F"
rules = {"F": "F+F--F+F"}
interpretation = {"F": ("forward", 1), "+": ("right", 60), "-": ("left", 60)}
depth = 6
```

![lines](code/img/koch_snowflake.svg)


### Sierpinski Triangle
[code](https://github.com/examon/iv122_math_code/blob/4091dad0481f3196c27dbe586036528392617243/class_6/code/lsystems.py#L52)

[animation](code/img/sierpinski_triangle_animate.svg)

```
axiom = "B"
rules = {"A": "B+A+B", "B": "A-B-A"}
interpretation = {"A": ("forward", 4), "B": ("forward", 4), "+": ("right", 60), "-": ("left", 60)}
depth = 8
```

![lines](code/img/sierpinski_triangle.svg)


### Hilbert Curve
[code](https://github.com/examon/iv122_math_code/blob/4091dad0481f3196c27dbe586036528392617243/class_6/code/lsystems.py#L65)

[animation](code/img/hilbert_curve_animate.svg)

```
axiom = "-L"
rules = {"L": "LF+RFR+FL-F-LFLFL-FRFR+", "R": "-LFLF+RFRFR+F+RF-LFL-FR"}
length = 10
interpretation = {"F": ("forward", length), "+": ("right", 90), "-": ("left", 90)}
depth = 4
```

![lines](code/img/hilbert_curve.svg)


