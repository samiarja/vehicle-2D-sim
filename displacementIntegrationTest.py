acceleration = [0.11, 0.11, 0.11, 0.11, 0.35,0.8,1,2,3,2,1 ]
velocity = [0]
displacement = [0]
time = 0
for acc in acceleration:
    time = time + 1
    velocity.append(velocity[-1] + acc * time)
    displacement.append(displacement[-1] * time + 0.5 * acc * time**2)
    print(displacement[-1])
del velocity[0]
del displacement[0]