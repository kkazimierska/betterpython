import string
import random
from abc import ABC, abstractmethod
from typing import List


def generate_id(length:int=8)-> str:
    """Helper function for generating an id.

    :param length: lenght of id, defaults to 8
    :return: random string ascii id
    """

    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    """Class to support the ticket system.
    """

    def __init__(self, customer: str, issue: str):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class TicketOrderingStrategy(ABC):
    """"Abstract interface for creating ordering strategy"
    """
    @abstractmethod
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        """Create the ordering for the tickets

        :param ticket_list: support tickets
        :return: ordered support tickets
        """

class FIFOOrderingStrategy(TicketOrderingStrategy):
    """First in First out strategy.
    """
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        return ticket_list

class FILOOrderingStrategy(TicketOrderingStrategy):
    """First in Last out strategy.
    """
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        tickets_copy = ticket_list.copy()
        tickets_copy.reverse()
        return tickets_copy

class RandomOrderingStrategy(TicketOrderingStrategy):
    """Random strategy.
    """
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        tickets_copy = ticket_list.copy()
        random.shuffle(tickets_copy)
        return tickets_copy

class CustomerSupport:
    """ Maintain the list of tickets.
    """

    def __init__(self, processing_strategy: TicketOrderingStrategy):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer: str, issue: str)->None:
        """Append the instance of the SupportTicket class to the
        list of tickets.

        :param customer: Name of the customer.
        :param issue: Description of the issue.
        """
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        """ Process the list of tickets.
        If it's empty, don't do anything.
        Execute the function process ticket based on processing strategy.
        Different strategies are based on the order of processing tickets.
        First in, first out. First in, last out. Recall stack.
        """
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!")
            return

        tickets_ordered = self.processing_strategy.create_ordering(self.tickets)

        for ticket in tickets_ordered:
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


# create the application
app = CustomerSupport(FILOOrderingStrategy())

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets()
# "fifo"