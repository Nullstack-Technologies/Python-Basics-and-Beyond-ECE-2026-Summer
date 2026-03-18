people = [
    'Soumodeep', 'Monjit', 'Sayan',
    'Madhav', 'Sayandeep', 'Asik',
    'Arup', 'Chiroshmita', 'Nandini',
    'Krishna', 'Sayandip', 'Ayushman',
    'Om'
    ]


n = len(people)
k = 2
result = 0

for i in range(2, n + 1):
    result = (result + k) % i

# print(people[result + 1])
print(people[result])