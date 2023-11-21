## Motivation

You can make a code that depend on
- resources
- solution that you want to use.

You can use **Strategy Design** Pattern.
Design patterns are generic solutions that you may encounter as a **Developer**.
It helps to write code that is easier to change.

## Problem statment

Where is the problem? Problem lies in `if\else` statment. Because of that `process_tickets` is quite long.
Currently it has `weak cohesion`, because the function is responsible for both:
- processing tickets
- implementing each strategy

Strategy design pattern aims to solve exactly this kind of problem.

In strategy pattern we create a class for each of those strategies.
Each class has one method that is called in `process_tickets`.

## Task 1

Define the abstract interface for `processing_strategy` with method `create_ordering`,
that has an argument list of SupportTickets. Implement instances of processing strategies.

## Task 2
Rewrite replacing the classes with functions - more basic version of the **strategy pattern**.
Can be a bit shorter, quicker and cleaner.

We can add typying for function parameter using **Callable**.
[Callable](https://docs.python.org/3/library/typing.html#annotating-callable-objects)

## Real world analogy and structure of Strategy Pattern

[Structure](https://refactoring.guru/design-patterns/strategy)

## TO practise
[Variations of the Strategy Pattern](https://www.youtube.com/watch?v=n2b_Cxh20Fw)