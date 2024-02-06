# longest-github-contribution

An easy way (web and console) to check what is the longest contribution on GitHub for any public user.

For acomplish my goal I'm using the class `HtmlParser` that I've created on my [web-scraping-intro](https://github.com/jersson/web-scraping-intro) repo. You can check that code also :smile:

I'm open to suggestions, if you have any idea/comment/etc please let me know :innocent:

## Summary

- [longest-github-contribution](#longest-github-contribution)
  - [Summary](#summary)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Dependencies](#dependencies)
  - [Usage](#usage)
    - [How to run the code as a console program](#how-to-run-the-code-as-a-console-program)
    - [How to run the web app](#how-to-run-the-web-app)
    - [How to run the automated tests](#how-to-run-the-automated-tests)
  - [References](#references)

## Installation

### Prerequisites

- [Python](https://www.python.org/) >=3.7.7
- [pip](https://pypi.org/project/pip/) >=20.0.2

### Dependencies

```bash
  make prepare
```

## Usage

### How to run the code as a console program

```bash
  make start-console
```

You'll see something like this:

```
  What's your GithHub account?
  > jersson
  Your longest contribution is...
  - start date 2020-03-19
  - end date 2020-04-03
  - 16 days in a row!
```

### How to run the web app

```bash
  make start-web
```

If everything is okay, you'll see this message:

```
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

So can go and test it

### How to run the automated tests

We are using `pytest` so you can launch that command

```bash
  make test
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
