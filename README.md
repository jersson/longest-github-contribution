# longest-github-contribution
An easy way to check what was the longest contribution on GitHub for any public user. For acomplish my goal I'm using a class `HtmlParser` that I've created on my [web-scraping-intro](https://github.com/jersson/web-scraping-intro) repo, you can check that code also :smile: 

I'm open to suggestions, if you have any idea/comment/etc please let me know :innocent:

## Sumary
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Dependencies](#dependencies)
  - [how to run the code](#how-to-run-the-code)
  - [How to test the code](#how-to-test-the-code)
  - [References](#references)

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
  - 16 days in a row!
```

## How to test the code

We are using `pytest` so you can launch that command

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