# Class 9

---

## Monty Hall Simulations

[Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)

Suppose you're on a game show, and you're given the choice of three doors:<br>
Behind one door is a car; behind the others, goats.<br>

You pick a door, say No. 1, and the host, who knows what's behind the doors,
opens another door, say No. 3, which has a goat. He then says to you,<br>
"Do you want to pick door No. 2?" Is it to your advantage to switch your choice?<br>


#### We will simulate tree scenarios:


- player will not change his pick
 - `strategy: not_changing_pick, win chance: 0.341`
- player will change his pick after host shows him door with goat
 - `strategy: changing_pick, win chance: 0.676`
- player acts randomly, sometimes chaning pick and sometimes not (with problability 0.5)
 - `strategy: random_change_pick, win chance: 0.492`

Simulation is using `1000` iterations.<br>
[code](code/monty_hall.py)

---

## Random Numbers

`TODO`

---

## Central Limit Theorem

`TODO`

---

## Bayes Theorem and Simulations

`TODO`
