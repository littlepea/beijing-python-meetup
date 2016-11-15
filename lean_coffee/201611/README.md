# Beijing Python Meetup Lean Coffee Notes (Oct 14, 2016)

* Date: [Oct 14, 2016](https://www.meetup.com/Beijing-Python/events/227473438/)
* Location: [Maan Coffee (Gongti)](https://maps.google.com/maps?f=q&hl=en&q=Corner+of+Worker%27s+Stadium+North%2FWest+Roads%2C+Beijing%2C+cn)
* Organizer: [Evgeny Demchenko](https://github.com/littlepea/)

It was the first time we've tried to use a [Lean Coffee](http://leancoffee.org/) format for our Python meetup and it worked pretty well.
We've used 8 minutes base time box and at the end of it decide to extend for 4 more minutes or move on to the next subject via a "Roman vote".
We've manage to cover 10 topics in about 1.5 hours which is pretty efficient. 

## Background

> "Lean Coffee is a structured, but agenda-less meeting. Participants gather, build an agenda, and begin talking. Conversations are directed and productive because the agenda for the meeting was democratically generated."

Each person can write a topic (or multiple topics) on an index card (example: "What's the best way to filter lists in python?"), then we "dot-vote" on all topics (5 votes limit per person), 
prioritize and have a time-boxed discussion on each topic in order of priority. 

We do this for 1.5 hours and try to get through as many topics as we can and then  sitch to a regular informal chat like we usually do. :)

Some topics were pre-submitted on our [Meetup Trello board](https://trello.com/b/415wH9ll/beijing-monthly-python-meetup).

## Topics Discussed

### Functional Programming in Python

While it's [possible to do functional programming](https://docs.python.org/2/howto/functional.html) in Python, the [language was not created with functional use cases in mind](http://stackoverflow.com/a/1017937/2045725).

If you really want to write the whole application in a strictly functional way, it's possible to do in Python, but it would be a better idea to actually use a real functional language.

At the same time, [classes are often over-used](https://www.youtube.com/watch?v=o9pEzgHorH0) 
and functional programming provides a lot of advantages by [removing the problems of state and increasing simplicity](https://www.youtube.com/watch?v=7Zlp9rKHGD4).

It's a good idea to try to combine both OO and functional approaches in our applications, 
and try to use functions as much as possible for the logic of the application 
while still using classes for use cases where classes are perfectly suitable (like Domain modelling). 

A good way to describe this is presented in [The Clean Architecture in Python](http://rhodesmill.org/brandon/slides/2013-10-pyconie/) talk by Brandon Rhodes.

### Best Python WEB framework for Microservice architecture

[Microservice architecture](https://www.fullstackpython.com/microservices.html) is becoming a bigger trend every year 
and there's a [big discussion on what frameworks to use for it in Python[(https://news.ycombinator.com/item?id=8421493).

The most common opinion is that "batteries included" frameworks like Django are more suitable for monolithic applications 
while [microservices require something light-weight like Flask/nameko/web.py/etc](https://github.com/mfornos/awesome-microservices#python).

It does make sense from the performance perspective, at the same time, it's possible to make an argument for the opposite: 
that Django is actually more suitable for rapidly developing small services rather than large monolithic applications 
because it's actually hard to scale to a very large codebase. 
And the performance difference in a distributed architecture (where I/O is the biggest bottleneck) is actually not that significant, 
but the developers productivity when using Django can be the key when building up new services quickly.

At the same time, a non-intrusive framework like Flask allows to easier scale a large codebase 
and keep the framework away from the business logic as long as the application is build using a [Clean Architecture](http://rhodesmill.org/brandon/slides/2013-10-pyconie/). 

### ORM vs. Raw SQL

There are [pros and cons](https://www.quora.com/What-are-the-pros-and-cons-of-using-raw-SQL-versus-ORM-for-database-development) of using [ORM or Raw SQL](http://stackoverflow.com/questions/494816/using-an-orm-or-plain-sql) in Pyhon applications.
 
Some OO advocates (including Uncle Bob) think that [ORM is a bad practice](http://www.yegor256.com/2014/12/01/orm-offensive-anti-pattern.html), others suggest that [ORM is very practical](http://karwin.blogspot.jp/2009/01/why-should-you-use-orm.html).

It might be a good idea to use ORM most of the time because it solves a few important issues:

* Abstracting the database from the code
* Providing a convenient Data Persistence layer in the code
* Allowing to write DB queries in a readable "pythonic" way
* Simplifying data modelling and validation

But in cases where queries get really complex (or slow) 
it's still possible to [fall back to Raw SQL through the ORM](https://docs.djangoproject.com/en/1.10/topics/db/sql/) when it's better to express a certain query in SQL.

### Lightweight way of dealing with structured data

Sometimes when an application is dealing with structured data (ex: read from CSV file) 
but it's not core domain entities and rather local data manipulation / business logic (within the same module for example) 
it can be hard to choose the right data structure to use in this case, because:

1. Creating classes seems to be an overkill
2. Dictionaries feel unreliable (too dynamic) and not as clean to deal with in the code

Dictionaries are perfect to map things of one type (keys) to other things on one type (values), this is what they are for. 
And not to use as data objects. Also, dict/JSON can have performance issues in data-heavy workloads.

Classes are good for important domain entities, 
but for local computation or simple data transfer objects [namedtuple](https://docs.python.org/2/library/collections.html#collections.namedtuple) can be a perfect solution.
It makes code [more readable](https://pythontips.com/2015/06/06/why-should-you-use-namedtuple-instead-of-a-tuple/) and has a high-performance of a tuple.

Of course, it's important to know that, like tuples, namedtuples are immutable, so if you need to change their state it's better to use classes.

### Early detection of errors (type hinting, etc...)

Coming from strongly-types languages to Python it can be scary or at least counter-intuitive to not have type checking during compile time 
which can catch a lot of very silly errors that should not get out into a production application.

The solution for this is implemented in Python 3.5 via [Type Hints](https://www.python.org/dev/peps/pep-0484/).

It provides a standard syntax for type annotations, opening up Python code to easier static analysis and refactoring, potential runtime type checking, and (perhaps, in some contexts) code generation utilizing type information.

Of these goals, static analysis is the most important. This includes support for off-line type checkers such as [mypy](http://mypy-lang.org/), as well as providing a standard notation that can be used by IDEs for code completion and refactoring.

While this is not as powerful as static typing these optional type annotations give us a perfect balance between static and dynamic languages 
and allow us to enjoy advantages of both in Python and helps to scale large codebases in a dynamically typed language.

In JavaScript world similar benefits are achieved by [TypeScript](https://www.typescriptlang.org/) language.

It's also important to remember that the real answer for making sure errors don't get out to production code and applications work as expected are Unit Tests, 
type checking is just gravy. ;)

### BDD in Python

[Behavior-driven development (or BDD)](http://pythonhosted.org/behave/philosophy.html) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project.

BDD focuses on obtaining a clear understanding of desired software behavior through discussion with stakeholders. It extends TDD by writing test cases in a natural language that non-programmers can read. Behavior-driven developers use their native language in combination with the ubiquitous language of domain-driven design to describe the purpose and benefit of their code. This allows the developers to focus on why the code should be created, rather than the technical details, and minimizes translation between the technical language in which the code is written and the domain language spoken by the business, users, stakeholders, project management, etc.

BDD scenarios use [The Gherkin language](http://pythonhosted.org/behave/philosophy.html#the-gherkin-language) to express the requirements in a domain language while still making it structures and possible to be executed as an "acceptance test".

In Python BDD can be used via tools like [behave](http://pythonhosted.org/behave/), [pytest-bdd](https://pypi.python.org/pypi/pytest-bdd), [Robot Framework](http://robotframework.org/) and others.

### "Design Patterns" relevancy in Python

### Open-source Business Software (ERP) writtenin Python in China

### Machine Learning Frameworks

### Thoughts on front-end / back-end separation and frameworks


