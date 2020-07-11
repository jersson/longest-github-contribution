# longest-github-contribution
An easy way to check what was your longest contribution on GitHub. For acomplish my goal I'm using the class `HtmlParser` I've created on my [web-scraping-intro](https://github.com/jersson/web-scraping-intro) repo, you can check that code too :smile: 

I'm open to suggestions, if you have any please let me know :innocent:

## Installation

### Prerequisites

- [Python](https://www.python.org/) >=3.7.7
- [pip](https://pypi.org/project/pip/) >=20.0.2

### Dependencies

```
 $ pip install -r requirements.txt
```

## how to run the code
```
  $ python program.py
```

You'll see something like this:
```
  What's your GithHub account?
  > jersson
  Your longest contribution is...
  - start date 2020-03-19 with 1 contributions
  - end date 2020-04-03 with 2 contributions
  - total days 16
  ...
```

## How to test the code

We are using `pytest` so you can run the `pytest` command

```
 $ pytest
```

You'll see something like this:

```
 ========================= test session starts =========================
 platform darwin -- Python 3.7.7, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
 rootdir: /Users/jersson/src/development/longest-github-contribution
 collected 5 items

 test_GitHubClient.py ...                                         [ 60%]
 test_HtmlParser.py ..                                            [100%]

 ========================== 5 passed in 3.02s ==========================
```

## References
TBD