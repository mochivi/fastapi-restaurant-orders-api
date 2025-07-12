from enum import StrEnum

class UserRole(StrEnum):
    customer = "customer"
    restaurant = "restaurant"
    admin = "admin"

class OrderStatus(StrEnum):
    pending_payment = "pending_payment" # pending customer payment
    pending = "pending" # restaurant received the order

    rejected = "rejected" # restaurant rejected the order
    confirmed = "confirmed" # restaurant confirmed the order

    pending_driver = "pending_driver" # order is complete, waiting for driver pick up

    sent = "sent" # driver is carrying the order

    driver_failed = "driver_failed" # something happened along the way
    customer_failed = "customer_failed" # customer did not respond
    
    received = "received" # customer has received the order