# Task 02 Tests: Ticket Price and Grade

Actual values recorded from a test run on 2026-11-19. All rows matched the expected values.

## Ticket tests

| # | Age | Student? | Expected | Actual | Pass? |
|---|---|---|---|---|---|
| 1 | 1 | yes | 200 | 200 | Pass |
| 2 | 1 | no | 300 | 300 | Pass |
| 3 | 17 | yes | 200 | 200 | Pass |
| 4 | 17 | no | 300 | 300 | Pass |
| 5 | 18 | yes | 400 | 400 | Pass |
| 6 | 18 | no | 500 | 500 | Pass |
| 7 | 59 | yes | 400 | 400 | Pass |
| 8 | 59 | no | 500 | 500 | Pass |
| 9 | 60 | yes | 600 | 600 | Pass |
| 10 | 60 | no | 700 | 700 | Pass |
| 11 | 61 | yes | 600 | 600 | Pass |
| 12 | 61 | no | 700 | 700 | Pass |
| 13 | 100 | yes | 600 | 600 | Pass |
| 14 | 100 | no | 700 | 700 | Pass |

## Grade tests

| # | Score | Expected | Actual | Pass? |
|---|---|---|---|---|
| 15 | 0 | F | F | Pass |
| 16 | 49 | F | F | Pass |
| 17 | 50 | E | E | Pass |
| 18 | 59 | E | E | Pass |
| 19 | 60 | D | D | Pass |
| 20 | 69 | D | D | Pass |
| 21 | 70 | C | C | Pass |
| 22 | 79 | C | C | Pass |
| 23 | 80 | B | B | Pass |
| 24 | 89 | B | B | Pass |
| 25 | 90 | A | A | Pass |
| 26 | 100 | A | A | Pass |

## Bad input tests

| # | Question | Input | Expected | Actual | Pass? |
|---|---|---|---|---|---|
| 27 | age | 0 | "between 1 and 150" message, asks again | same | Pass |
| 28 | age | 151 | "between 1 and 150" message, asks again | same | Pass |
| 29 | age | abc | "wholenumbers" message, asks again | same | Pass |
| 30 | age | 12.5 | "wholenumbers" message, asks again | same | Pass |
| 31 | age | (empty Enter) | "wholenumbers" message, asks again | same | Pass |
| 32 | student | maybe | "Yes or No" message, asks again | same | Pass |
| 33 | student | y | "Yes or No" message, asks again | same | Pass |
| 34 | student | (empty Enter) | "Yes or No" message, asks again | same | Pass |
| 35 | score | -1 | "between 0 and 100" message, asks again | same | Pass |
| 36 | score | 101 | "between 0 and 100" message, asks again | same | Pass |
| 37 | score | abc | "wholenumbers" message, asks again | same | Pass |