# n = input("Input n: ")
# socks = input("Enter Space Separated Socks:")
# socks = socks.split()
# print(socks)

socks = ['10', '20', '20', '10', '10', '30', '50', '10', '20']
individual_socks = list(set(socks))
# print(individual_socks)
socks_list = []

for individual_sock in individual_socks:
    socks_list.append({
        'sock': individual_sock,
        'count': socks.count(individual_sock)
    })

pairs = 0
for sock_item in socks_list:
    pairs += sock_item['count'] // 2

print(pairs)