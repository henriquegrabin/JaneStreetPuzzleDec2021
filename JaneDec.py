# Robot Archery - https://www.janestreet.com/puzzles/robot-archery-index/
# After a grueling year filled with a wide variety of robot sporting events, 
# we have arrived at the final event of the year: Robot Archery. Four robots
# have qualified for this year’s finals, and have been seeded in the following order:

# Robot	Seed 
# Aaron	 1
# Barron 2
# Caren	 3
# Darrin 4

# The robots will take turns shooting arrows at a target1, starting with Aaron
# and proceeding in order by seed. When it is a given robot’s turn, they shoot
# a single arrow. If it is closer to the center of the target than all previous 
# arrows by all players, that robot remains in the tournament, going to the back 
# of the queue to await their next turn. Otherwise that robot is eliminated 
# immediately. The last robot remaining in the queue is the winner.

# For example, here is how last year’s finals went, in which Caren was the winner. 
# (Oddly enough it involved the same robots in the same seeding.)

# Turn  	Robot	Distance
# 1	Aaron	10nm
# 2	Barron  8nm
# 3	Caren	7nm
# 4	Darrin  1km
# 5	Aaron	9nm
# 6	Barron	2nm
# 7	Caren	1nm
# 8	Barron	1Ym2

# To ten decimal places, what is the probability that Darrin will 
# be this year’s winner? (Or, if you want to send in the exact 
# answer, that’s fine too!)

from collections import deque
MAX_TREE_LENGTH = 30
PLAYER = 4

def run_iteration(q: deque, i: int, p: float):
    if len(q) <= 1: return p
    if i >= MAX_TREE_LENGTH: return p

    i += 1
    
    item = q.pop()
    if item == PLAYER:
        q.appendleft(PLAYER)
        p = p * (1 / i)
        return run_iteration(q, i, p)

    # the case this player survives
    p1 = p * (1/i)
    q1 = q.copy()
    q1.appendleft(item)

    # the case it loses
    p2 = p * ((i-1)/i)
    q2 = q
    
    return run_iteration(q1, i, p1) + run_iteration(q2, i, p2)

def main():
    # from right to left
    q = deque([1, 4, 3, 2])

    res = run_iteration(q, 1, 1)

    print(res)

if __name__ == '__main__':
    main()