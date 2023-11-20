import string
import random


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


class CustomerSupport:
    """ Maintain the list of tickets.
    """

    def __init__(self, processing_strategy: str = "fifo"):
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

        if self.processing_strategy == "fifo":
            for ticket in self.tickets:
                self.process_ticket(ticket)
        elif self.processing_strategy == "filo":
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)
        elif self.processing_strategy == "random":
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
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
app = CustomerSupport("filo")

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets()
# "fifo"