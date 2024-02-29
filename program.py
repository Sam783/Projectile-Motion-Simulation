import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.81

def calculate_trajectory(initial_velocity, angle, filename):
    angle = math.radians(angle)

    vx = initial_velocity * math.cos(angle)
    vy = initial_velocity * math.sin(angle)
    
    time_of_flight = (2 * vy) / g
    
    t = np.arange(0, time_of_flight + 0.2, 0.2)
    x = vx * t
    y = vy * t - 0.5 * g * t**2
    

    with open(filename, 'w') as file:
        file.write("Time(s)\t\tRange(m)\tHeight(m)\n")
        for i in range(len(t)):
            file.write("{:.2f}\t\t{:.2f}\t\t{:.2f}\n".format(t[i], x[i], y[i]))
    
    return t, x, y

def projectile_motion(initial_velocity, angle):
    angle = math.radians(angle)
    
    vx = initial_velocity * math.cos(angle)
    vy = initial_velocity * math.sin(angle)
    
    time_of_flight = round((2 * vy) / g, 2)
    maximum_range = round((vx * vy) / (0.5 * g), 2) 
    maximum_height = round((vy ** 2) / (2 * g), 2)
    
    return time_of_flight, maximum_range , maximum_height

initial_velocity = float(input("Enter the initial velocity (m/s): "))
angle = float(input("Enter the angle of projection (degrees): "))
filename = input("Enter the filename to save the data: ")

time_of_flight, maximum_range, maximum_height = projectile_motion(initial_velocity, angle)

print("Time of flight: {} s".format(time_of_flight))
print("Maximum range: {} m".format(maximum_range))
print("Maximum height: {} m".format(maximum_height))

t, x, y = calculate_trajectory(initial_velocity, angle, filename)

fig, ax = plt.subplots(figsize=(12, 5))

trajectory, = ax.plot([], [], label="Projectile path")
ax.set_xlabel("Range (m)")
ax.set_ylabel("Height (m)")
ax.set_title("Projectile Motion")
ax.legend()
ax.set_xlim(0, max(x) + 10)
ax.set_ylim(0, max(y) + 10)

def animate(i):
    trajectory.set_data(x[:i], y[:i])
    return trajectory,

ani = FuncAnimation(fig, animate, interval=20, blit=True, cache_frame_data=False)

plt.show()
