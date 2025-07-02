# Profit Targets

A financial analyst is responsible for a portfolio of profitable stocks represented in an array. Each item in the array represents the yearly profit of a corresponding stock. The analyst gathers all distinct pairs of stocks that reached the target profit. Distinct pairs are pairs that differ in at least one element.

Given the array of profits, find the number of distinct pairs of stocks where the sum of each pair’s profits is exactly equal to the target profit.

## Example

**Input:**

> `target = 12`<br>
> `stocksProfit = [5, 7, 9, 13, 11, 6, 6, 3, 3]`

**Explanation:**
- There are **4 pairs of stocks** that have the sum of their profits equal to the target `12`.  
- Note that because there are two instances of `3` in `stocksProfit`, there are two pairs matching `(9, 3)`:
  - `stocksProfit` indices `2` and `7`, and
  - `stocksProfit` indices `2` and `8`, but only **one** can be included.

- Therefore, the **3 distinct pairs** of stocks are:
  - `(5, 7)`, `(3, 9)`, and `(6, 6)`  
  - The return value is **3**.

## Function Description

Complete the function `stockPairs` in the editor below.

`stockPairs` has the following parameter(s):

- `int target`: an integer representing the yearly target profit
- `List<Integer> stocksProfit`:  a List of integers representing the stocks profits

Returns:

`int`: the total number of distinct pairs determined

## Constraints

- 1 <= `n` <= 5 <small>x</small> 10<sup>5</sup>
- 0 <= `stocksProfit[i]` <= 10<sup>9</sup>
- 0 <= `target` <= 5 <small>x</small> 10<sup>9</sup>
