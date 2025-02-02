def tower_of_hanoi(no_of_rings, source, target, auxillary):
    if no_of_rings == 1: #base case
        print(f"Moved ring {no_of_rings} from {source} to {target}")
        return
    tower_of_hanoi(no_of_rings -1 , source, auxillary, target)
    print(f"Moved ring {no_of_rings} from {source} to {target}")
    tower_of_hanoi(no_of_rings-1, auxillary, target, source)

tower_of_hanoi(5, 'A','C','B')