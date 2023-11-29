from dataclasses import dataclass, field
import string
import random
from typing import List, Callable


def generate_id(length:int=8)-> str:
    """Helper function for generating an id.

    :param length: lenght of id, defaults to 8
    :return: random string ascii id
    """

    return ''.join(random.choices(string.ascii_uppercase, k=length))


@dataclass
class SupportTicket:
    """Class to support the ticket system.
    """
    id: str = field(init=False, default_factory=generate_id)
    customer: str
    issue: str


SupportTickets = List[SupportTicket]

Ordering = Callable[[SupportTickets], SupportTickets]


def fifo_ordering(tickets_list: SupportTickets) -> SupportTickets:
    """First In, First Out Ordering Strategy
    """
    return tickets_list.copy()


def filo_ordering(tickets_list: SupportTickets) -> SupportTickets:
    """First In, Last Out Ordering Strategy
    """
    list_copy = tickets_list.copy()
    list_copy.reverse()
    return list_copy


def random_ordering(tickets_list: SupportTickets) -> SupportTickets:
    """Radom Ordering Strategy
    """
    list_copy = tickets_list.copy()
    random.shuffle(list_copy)
    return list_copy

class CustomerSupport:
    """ Maintain the list of tickets.
    """

    def __init__(self):
        self.tickets: SupportTickets = []

    def create_ticket(self, customer: str, issue: str)->None:
        """Append the instance of the SupportTicket class to the
        list of tickets.

        :param customer: Name of the customer.
        :param issue: Description of the issue.
        """
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, ordering: Ordering):
        """ Process the list of tickets.
        If it's empty, don't do anything.
        Execute the function process ticket based on processing strategy.
        Different strategies are based on the order of processing tickets.
        First in, first out. First in, last out. Recall stack.
        """
        ticket_list = ordering(self.tickets)
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket)-> None:
        """ Print the information about the ticket id, customer and isssue.

        :param ticket: Ticket to process.
        """
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


def main() -> None:
    """Create the application, register and process tickets.
    """
    app = CustomerSupport()

    app.create_ticket("John Smith", "My computer makes strange sounds!")
    app.create_ticket("Linus Sebastian",
                      "I can't upload any videos, please help.")
    app.create_ticket(
        "Arjan Egges", "VSCode doesn't automatically solve my bugs.")

    app.process_tickets(random_ordering)


if __name__ == '__main__':
    main()
