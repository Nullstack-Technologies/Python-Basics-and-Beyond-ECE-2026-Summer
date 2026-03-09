def tower_of_hanoi(disks, source, aux, dest):
    if disks == 1:
        print(f"Move 1 disk from {source} to {dest}")
    
    else:
        tower_of_hanoi(disks -1, source, dest, aux)
        print(f"Move {disks} disk from {source} to {dest}")
        tower_of_hanoi(disks -1, aux, source, dest)

disks = int(input("Enter the number of disks: "))
tower_of_hanoi(disks, 'A', 'B', 'C')