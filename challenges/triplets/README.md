# Triplets

Given an array of `n` distinct integers, `d = [d[0], d[1], ...,d[n-1]]`, and an integer threshold, `t`, how many `(a, b, c)` index triplets exist that satisfy both of the following conditions?

- `d[a] < d[b] < d[c]`
- `d[a] + d[b] + d[c] <= t`

### Example
> `d = [1, 2, 3, 4, 5]`<br>
> `t = 8`
>
> The following 4 triplets satisfy the constraints:
> 
> - ```(1, 2, 3) -> 1 + 2 + 3 = 6 <= 8```
> - ```(1, 2, 4) -> 1 + 2 + 4 = 7 <= 8```
> - ```(1, 2, 5) -> 1 + 2 + 5 = 8 <= 8```
> - ```(1, 3, 4) -> 1 + 3 + 4 = 8 <= 8```

### Function Description

Complete the function `triplets` in the editor below.

`triplets` has the following parameter(s):

- `int t`: an integer threshold
- `int d[n]`: an array of integers

Returns:
- `long`: a long integer that denotes the number of `(a, b, c)` triplets that satisfy the given conditions.

### Constraints

- 1 <= `n` <= 10<sup>4</sup>
- 0 <= `d[i]` < 10<sup>9</sup>
- 0 < `t` < 3 <small>x</small> 10<sup>9</sup>
