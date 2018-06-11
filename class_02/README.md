# Class 2

## Permutations, Variations, Combinations

[code](code/combinatorics.py)

---

## Pascals Triangle

[code](code/pascals.py)

Pascals triangle with depth level `30` and modulus `5`.

Different shades of grey represent different result after `mod 5`.

![pascals](code/img/pascals.bmp)

---

## Exponentiation Implementations Benchmark

[code](code/exponentiation.py)

We are going to compute `x = n^e mod m`, where `e` is going to be large (from `10^2` to `10^8`).
Four methods are going to be tested:
- `python_pow`, is `pow` function from the standard `math` python library
- `binary_exp`, is not very efficient implementation of the binary exponentiation (see https://en.wikipedia.org/wiki/Modular_exponentiation)
- `binary_exp_v2`, is faster version of the `binary_exp`
- `naive_pow`, is very naive exponentiation

As we can see from the following results. `naive_pow` is really only good for
very small exponents.
Badly written `binary_exp` can handle little more, but still does not scale
well at all.

`python_pow` and `binary_exp_v2` are scaling very well.
`binary_exp_v2` is around 3 times slower than `python_pow`.

```
exponent zeroes: 4
     python_pow: 0.0 ms
     binary_exp: 0.1 ms
  binary_exp_v2: 0.0 ms
      naive_pow: 4.4 ms

exponent zeroes: 5
     python_pow: 0.0 ms
     binary_exp: 2.0 ms
  binary_exp_v2: 0.0 ms
      naive_pow: 372.4 ms

exponent zeroes: 6
     python_pow: 0.0 ms
     binary_exp: 59.5 ms
  binary_exp_v2: 0.0 ms
      naive_pow: 36724.5 ms

exponent zeroes: 7
     python_pow: 0.0 ms
     binary_exp: 3356.4 ms
  binary_exp_v2: 0.0 ms

exponent zeroes: 8
     python_pow: 0.0 ms
  binary_exp_v2: 0.0 ms

exponent zeroes: 100
     python_pow: 0.0 ms
  binary_exp_v2: 0.0 ms

exponent zeroes: 10000
     python_pow: 1.1 ms
  binary_exp_v2: 2.8 ms

exponent zeroes: 100000
     python_pow: 10.8 ms
  binary_exp_v2: 27.8 ms

exponent zeroes: 1000000
     python_pow: 107.6 ms
  binary_exp_v2: 278.9 ms

exponent zeroes: 10000000
     python_pow: 1075.1 ms
  binary_exp_v2: 2792.1 ms
```

---

## Pi Computation

[code](code/pi_computation.py)

Here we can compare different methods for computing `pi`.

Each method was running for 1 second while producing different precision.

`Archimedes` and `Gauss-Legendre` methods we able to produce the best precision
after 1 second of computation.

```
=== running each method for 1 seconds ===
 pi (50 digits): 3.1415926535897932384626433832795028841971693993751
Leubniz formula: 3.14159*
     Archimedes: 3.14159265358979*
   Monter Carlo: 3.14*
 Gauss-Legendre: 3.141592653589793*
```
