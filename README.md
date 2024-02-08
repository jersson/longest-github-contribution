# longest-github-contribution

Easy way to check see is the longest contribution on GitHub for any public user (console and web mode)

For acomplish my goal I'm using the class `HtmlParser` that I've created on my [web-scraping-intro](https://github.com/jersson/web-scraping-intro) repo. You can check that old code too :smile:

I'm open to suggestions, if you have any idea/comment/etc please let me know :innocent:

## Installation

### Prerequisites

- [Python](https://www.python.org/) >=3.7.7
- [pip](https://pypi.org/project/pip/) >=20.0.2

### Dependencies

```bash
  make prepare
```

## Usage

### Folder structure

I'm working a lot to make this code cleaner, so please go ahead and shot some issues if you want :smile:

```bash
.
├── requirements.txt
├── src
│   ├── console.py
│   ├── infrastructure
│   ├── server.py
│   ├── templates
│   └── utils
└── tests
    └── infrastructure

```

### How to run the code as a console program

```bash
  make start-console
```

You'll see something like this:

```bash
  What's your GitHub account?
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

```bash
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

So can go and test it

### How to run the automated tests

I'm using `pytest` so you can launch that command

```bash
  make test
```

You'll see something like this:

```bash
======================================= test session starts =======================================
platform darwin -- Python 3.11.6, pytest-8.0.0, pluggy-1.4.0
rootdir: /Users/jersson/src/dev/longest-github-contribution
collected 6 items                                                                                 

tests/infrastructure/test_github_client.py ..                                               [ 33%]
tests/infrastructure/test_html_parser.py ....                                               [100%]

======================================== 6 passed in 0.07s ========================================
```

> In some cases I'm using [mocks](https://docs.python.org/3/library/unittest.mock.html), please be my guest to see the code :smile:
>
## References

TBD
