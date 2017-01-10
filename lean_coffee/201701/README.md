# Beijing Python Meetup Lean Coffee Notes (Jan 9, 2017)

* Date: [Jan 9, 2017](https://www.meetup.com/Beijing-Python/events/232653326/)
* Location: [Maan Coffee (Gongti)](https://maps.google.com/maps?f=q&hl=en&q=Corner+of+Worker%27s+Stadium+North%2FWest+Roads%2C+Beijing%2C+cn)
* Organizer: [Evgeny Demchenko](https://github.com/littlepea/)

It was the second time we've used [Lean Coffee](http://leancoffee.org/) format for our Python meetup and it worked to everyone's satisfaction.
We've used 8 minutes base time box and at the end of it decide to extend for 4 more minutes or move on to the next subject via a "Roman vote".
Because of high member turnout we've split in two groups and managed to cover ~ 20 topics in about 1.5 hours which is pretty efficient. 

## Background

> "Lean Coffee is a structured, but agenda-less meeting. Participants gather, build an agenda, and begin talking. Conversations are directed and productive because the agenda for the meeting was democratically generated."

Each person can write a topic (or multiple topics) on an index card (example: "What's the best way to filter lists in python?"), then we "dot-vote" on all topics (5 votes limit per person), 
prioritize and have a time-boxed discussion on each topic in order of priority. 

We do this for 1.5 hours and try to get through as many topics as we can and then  sitch to a regular informal chat like we usually do. :)

## Topics Discussed

### Grumpy – good or bad?

Hint: [Grumpy](https://github.com/google/grumpy) Google’s latest language to bridge Python with Go, technically speaking a source code transpiler and runtime.

- So far only for 2.7, no ambition yet for 3.6 (since Google mostly uses 2.7)
- Could be interpreted as a move to transition away from Python
- Might not need much effort to also port for Python 3

### What is the fastest path to productivity for a novice to become a Python/Django-developer?

- Individual development plan based on current skills and interest in problems to solve
- Self-study of tutorials  
- Pairing with an experienced developer
- Have them focus on part of the stack at first (e.g., HTML/CSS or database)

### Best practice to configure Python 2 and Python 3 on one system?

Just go with standard setup on Linux, Mac or Win and then use either containerization (e.g. Docker or [LXD](https://github.com/lxc/lxd)) 
or, on a higher level, using [pyenv](https://github.com/yyuu/pyenv) which can automate the handling of virtualenv.

### Relative Import vs Explicit Import?

Relative imports are not good for refactoring and not suggested by the Python documentation. It’s advised to use explicit imports.

### Neural Network software in Python?

Python is strong in that field with several libraries available. Many are historically grown with focus on function. Yet there is a new strong player called [TensorFlow](https://github.com/tensorflow/tensorflow). Some group members had tested it and found it outperforming the existing players in performance and architectural scalability.

### Recommended e-commerce payment solutions in Python?  

An established cart is [Django Oscar](https://github.com/django-oscar). This option and also other carts that are on other frameworks than Django can easily get propped up for payments in China (Tenpay/WeChat Pay, AliPay) via gateway [Ping++](https://github.com/PingPlusPlus/pingpp-python), a Shanghai-based startup. 

### Python 3.6 – what’s new?

- See [release notes](https://docs.python.org/3/whatsnew/3.6.html)
- Most notably [asincio](https://docs.python.org/3/library/asyncio.html#module-asyncio), the herewith standardized new module as a synthesis of asynchronous I/O, event loop, coroutines and tasks. asincio provides infrastructure for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives. 
- An early adopter of asincio and other improvements since 3.5 is for example the new Flask-like web server [Sanic](https://github.com/channelcat/sanic), which goes faster than Wheezy and much faster then Flask or Tornado.
- Formatted string literals (something like `f"He said his name is {name}."`)
- Optional type annotations

### Python trends?

- In general Python is staying strong where a language is needed that is easy to get in. That’s for example why Python is well established in science field or DevOps.
- [Ansible](https://github.com/ansible/ansible) and [Salt](https://github.com/saltstack/salt) automation / configuration management increasingly popular (over Ruby-based Chef and Puppet).
- Rather losing at CMS and e-commerce web applications (e.g. to Node.js backend & React frontend)
