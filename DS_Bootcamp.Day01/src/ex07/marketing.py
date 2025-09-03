import sys

def call_center(clients, recipients):
    return (set(clients) - set(recipients))

def potential_clients(participants, clients):
    return (set(participants) - set(clients))

def loly_program(clients, participants):
    return (set(clients) - set(participants))

def marketing(goal):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
'elon@paypal.com', 'jessica@gmail.com'] # Все клиенты
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com'] # Участники мероприятия
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is'] # Видели письмо

    if goal[0] == "call_center":
        print(*call_center(clients, recipients), sep='\n')
    elif goal[0] == "potential_clients":
        print(*potential_clients(participants, clients), sep='\n')
    elif goal[0] == "loly_program":
        print(*loly_program(clients, participants), sep='\n')
    else:
        raise Exception("Exception")



if __name__ == '__main__':
    marketing(sys.argv[1:])