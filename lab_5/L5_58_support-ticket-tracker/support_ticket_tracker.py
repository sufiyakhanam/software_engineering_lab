"""Support ticket tracker application."""

import json
import logging
import os

TICKETS = {}


def create_ticket(
    title,
    description,
    reporter,
    ticket_options=None,
    audit_log=None,
):
    """Create and store a new support ticket."""
    if not title:
        return None

    if ticket_options is None:
        ticket_options = {}

    if audit_log is None:
        audit_log = []

    priority = ticket_options.get("priority", "medium")
    category = ticket_options.get("category", "general")

    ticket_id = str(len(TICKETS) + 1)
    ticket = {
        "id": ticket_id,
        "title": title,
        "description": description,
        "priority": priority,
        "category": category,
        "status": "open",
        "reporter": reporter,
        "assignee": None,
    }
    TICKETS[ticket_id] = ticket
    audit_log.append(f"Created ticket {ticket_id} for {reporter}")
    return ticket


def assign_ticket(ticket_id, agent):
    """Assign a ticket to an agent."""
    try:
        TICKETS[ticket_id]["assignee"] = agent
        return True
    except KeyError:
        return False


def update_status(ticket_id, status):
    """Update the status of a ticket."""
    TICKETS[ticket_id]["status"] = status
    return TICKETS[ticket_id]


def search_tickets(status=None, priority=None):
    """Search tickets by status and/or priority."""
    results = []
    for ticket in TICKETS.values():
        if status is not None and ticket["status"] != status:
            continue
        if priority and ticket["priority"] != priority:
            continue
        results.append(ticket)
    return results


def save_tickets(path="tickets.json"):
    """Save all tickets to a JSON file."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(json.dumps(TICKETS))


def load_tickets(path="tickets.json"):
    """Load tickets from a JSON file."""
    with open(path, "r", encoding="utf-8") as file:
        return json.loads(file.read())


def print_ticket_report():
    """Print a summary of all support tickets."""
    print("Support Tickets")
    if not TICKETS:
        print("No tickets yet")
    for ticket_id, ticket in TICKETS.items():
        print(
            ticket_id,
            ticket["title"],
            ticket["status"],
        )


def close_ticket(ticket_id):
    """Close a support ticket."""
    TICKETS[ticket_id]["status"] = "closed"


def is_open(ticket_id):
    """Return whether a ticket is currently open."""
    return TICKETS[ticket_id]["status"] in ("open", "in_progress")


def main():
    """Run the support ticket tracker application."""
    logging.basicConfig(level=logging.INFO)
    create_ticket(
        "Cannot sign in",
        "Password reset link fails",
        "alex@example.com",
    )
    create_ticket(
        "Billing question",
        "Charged twice",
        "lee@example.com",
        {"priority": "high"},
    )
    assign_ticket("1", "agent-01")
    update_status("1", "in_progress")
    print_ticket_report()
    logging.info("Tickets created: %s", len(TICKETS))
    print("Ticket 1 open?", is_open("1"))
    ticket_id = input("Ticket id to close (Enter to skip): ")
    if ticket_id:
        close_ticket(ticket_id)
    save_tickets()

    if os.environ.get("RUN_UNSAFE_DEMO") == "1":
        print("unsafe demo")


if __name__ == "__main__":
    main()
