import streamlit as st
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.81

def calculate_trajectory(initial_velocity, angle, filename):
    angle = math.radians(angle)

    vx = initial_velocity * math.cos(angle)
    vy = initial_velocity * math.sin(angle)
    
    time_of_flight = (2 * vy) / g
    
    t = np.round(np.arange(0, time_of_flight + 0.2, 0.2), 2)
    x = np.round(vx * t, 2)
    y = np.round(vy * t - 0.5 * g * t**2, 2)
    
    with open(filename, 'w') as file:
        file.write("Time(s)\t\tRange(m)\tHeight(m)\n")
        for i in range(len(t)):
            file.write("{:}\t\t{:}\t\t{:}\n".format(t[i], x[i], y[i]))
    
    return t, x, y

def projectile_motion(initial_velocity, angle):
    g = 9.81
    angle = math.radians(angle)
    
    vx = initial_velocity * math.cos(angle)
    vy = initial_velocity * math.sin(angle)
    
    time_of_flight = round((2 * vy) / g, 2)
    
    maximum_range = round((vx * vy) / (0.5 * g), 2) 
    maximum_height = round((vy ** 2) / (2 * g), 2)
    
    return time_of_flight, maximum_range , maximum_height


st.title("Projectile Motion Simulation")

initial_velocity = st.number_input("Enter the initial velocity (m/s): ", value=None)
angle = st.number_input("Enter the angle of projection (degrees): ", value=None)
filename = st.text_input("Enter filename to save data: ", value=None)


if st.button("Calculate"):
    time_of_flight, maximum_range, maximum_height = projectile_motion(initial_velocity, angle)

    st.subheader("Time of flight: {} s".format(time_of_flight))
    st.subheader("Maximum range: {} m".format(maximum_range))
    st.subheader("Maximum height: {} m".format(maximum_height))

    t, x, y = calculate_trajectory(initial_velocity, angle, filename)
    fig, ax = plt.subplots(figsize=(7, 4))
    # fig.subplots_adjust(left=0.07)

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

    ani = FuncAnimation(fig, animate, frames=len(t)+10, interval=40, blit=True, repeat=False)
        
    html_video = ani.to_html5_video()

    html_video = html_video.replace('<video ', '<video autoplay playsinline>')

    st.markdown(html_video, unsafe_allow_html=True)

    df = pd.DataFrame({
        "Time(s)": t,
        "Range(m)": x,
        "Height(m)": y
    })
    st.subheader("Projectile Details")
    st.dataframe(df, use_container_width=True, hide_index=True,)