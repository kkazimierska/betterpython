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

## Step 1

Define the abstract interface for `processing_strategy` with method `create_ordering`,
that has an argument list of SupportTickets. Implement instances of processing strategies.