import sys

def create_client_dict():
    purchases = sys.stdin.read().split('\n')
    purchases = [line.split() for line in purchases if line != '']
    
    client_dict = {}
    for client, product, number in purchases:
        if client in client_dict:
            if product not in client_dict[client]:
                client_dict[client][product] = 0
            client_dict[client][product] += int(number)
        else:
            client_dict[client] = {product: int(number)}
    return client_dict


def print_client_dict(client_dict):
    sorted_clients = sorted(client for client in client_dict)
    for client in sorted_clients:
        print(client, ':', sep='')
        sorted_products = sorted(product for product in client_dict[client])
        for product in sorted_products:
            print(product, client_dict[client][product])
        
    
client_dict = create_client_dict()
print_client_dict(client_dict)