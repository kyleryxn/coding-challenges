# Wikipedia Article

Using an `HTTP GET` method, retrieve information from Wikipedia using a given topic. Query *https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=[topic]* to get the *topic* Wikipedia article. Return the total number of times that the string `[topic]` appears in the article's `text` field.

Note: the search is case-sensitive

The query response from the website is a JSON object described below:

- `parse`: A JSON object representing the article's parsed web page. It has the following three fields:
  1. `title`: The article's title, as specified by the argument passed as `topic`
  2. `pageid`: The article's page ID
  3. `text`: A JSON object that contains the Wikipedia article as an HTML dump

### Function Description

Complete the function `getTopicCount` in the editor below.

`getTopicCount` has the following parameter(s):
- `topic`: a string to query

Returns:
`int`: an integer, the number of times the search term `topic` appears in the returned `text` field