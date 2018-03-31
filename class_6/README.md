# Class 6

---

## Chaos Game

TODO

---

## Feigenbaum Diagram

TODO

---

## L-Systems


### Koch Snowflake
[code](https://github.com/examon/iv122_math_code/blob/4091dad0481f3196c27dbe586036528392617243/class_6/code/lsystems.py#L65)

[animation](code/img/koch_snowflake_animate.svg)

```
axiom = "F--F--F"
rules = {"F": "F+F--F+F"}
interpretation = {"F": ("forward", 1), "+": ("right", 60), "-": ("left", 60)}
depth = 6
```

![lines](code/img/koch_snowflake.svg)


### Sierpinski Triangle
[code](https://github.com/examon/iv122_math_code/blob/4091dad0481f3196c27dbe586036528392617243/class_6/code/lsystems.py#L78)

[animation](code/img/sierpinski_triangle_animate.svg)

```
axiom = "B"
rules = {"A": "B+A+B", "B": "A-B-A"}
interpretation = {"A": ("forward", 4), "B": ("forward", 4), "+": ("right", 60), "-": ("left", 60)}
depth = 8
```

![lines](code/img/sierpinski_triangle.svg)


### Hilbert Curve
[code](https://github.com/examon/iv122_math_code/blob/4091dad0481f3196c27dbe586036528392617243/class_6/code/lsystems.py#L91)

[animation](code/img/hilbert_curve_animate.svg)

```
axiom = "-L"
rules = {"L": "LF+RFR+FL-F-LFLFL-FRFR+", "R": "-LFLF+RFRFR+F+RF-LFL-FR"}
length = 10
interpretation = {"F": ("forward", length), "+": ("right", 90), "-": ("left", 90)}
depth = 4
```

![lines](code/img/hilbert_curve.svg)


### Trees

#### Basic Tree
[code](https://github.com/examon/iv122_math_code/blob/4091dad0481f3196c27dbe586036528392617243/class_6/code/lsystems.py#L105)

[animation](code/img/basic_tree_animate.svg)

```
axiom = "A"
rules = {"A": "F[+A]-A", "F": "FF"}
length = 1
angle = 30
interpretation = {"F": ("forward", length), "[": ("stack", "push"), "]": ("stack", "pop"), "+": ("right", angle), "-": ("left", angle)}
depth = 9
```

![basic_tree](code/img/basic_tree.svg)


#### Fancy Tree 1
[code](https://github.com/examon/iv122_math_code/blob/4091dad0481f3196c27dbe586036528392617243/class_6/code/lsystems.py#L120)

[animation](code/img/fancy_tree_1_animate.svg)

```
axiom = "F"
rules = {"F": "F[+F]F[-F]F"}
length = 3
angle = 25.7
interpretation = {"F": ("forward", length), "[": ("stack", "push"), "]": ("stack", "pop"), "+": ("right", angle), "-": ("left", angle)}
depth = 5
```

![fancy_tree_1](code/img/fancy_tree_1.svg)


#### Fancy Tree 2
[code](https://github.com/examon/iv122_math_code/blob/4091dad0481f3196c27dbe586036528392617243/class_6/code/lsystems.py#L134)

[animation](code/img/fancy_tree_2_animate.svg)

```
axiom = "F"
rules = {"F": "F[+FF]F[-FF]F"}
length = 3
angle = 25.7
interpretation = {"F": ("forward", length), "[": ("stack", "push"), "]": ("stack", "pop"), "+": ("right", angle), "-": ("left", angle)}
depth = 5
```

![fancy_tree_2](code/img/fancy_tree_2.svg)


#### Stochastic Tree
[code](https://github.com/examon/iv122_math_code/blob/4091dad0481f3196c27dbe586036528392617243/class_6/code/lsystems.py#L148)

```
axiom = "F"
rules = {"F": ["[+F]F[−F]", "F[+F]F", "F[-F]F"]}
length = 5
angle = [25, 30, 35]
interpretation = {"F": ("forward", length), "[": ("stack", "push"), "]": ("stack", "pop"), "+": ("right", angle), "-": ("left", angle)}
depth = 9
```

![stochastic](code/img/fancy_tree_3_stochastic.svg)
![stochastic_2](code/img/fancy_tree_3_stochastic_2.svg)
![stochastic_3](code/img/fancy_tree_3_stochastic_3.svg)
