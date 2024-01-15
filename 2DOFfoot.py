import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('classic')



def dh_matrix(theta1, theta2, a1, a2):
    return np.array([
        [np.cos(theta1 + theta2), -np.sin(theta1 + theta2), 0, a1*np.cos(theta1) + a2*np.cos(theta1 + theta2)],
        [np.sin(theta1 + theta2), np.cos(theta1 + theta2), 0, a1*np.sin(theta1) + a2*np.sin(theta1 + theta2)],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def forward_kinematics(theta1, theta2, L1, L2):
    T1 = dh_matrix(theta1, theta2, L1, L2)
    
    return T1[:2, -1]

def joint_pos(theta1, L1):
    x_p2 = L1*np.cos(theta1)
    y_p2 = L1*np.sin(theta1)
    pos = np.array([x_p2, y_p2])

    return pos

# Define the joint angles for the animation
k = -20

theta1_values = np.linspace(np.radians(k), np.radians(k), 100)

theta2_values = np.linspace(0 - k, np.radians(90) - k, 100)

offset_angle = np.radians(-90)

fig, ax = plt.subplots()
ax.set_xlim([-0.5, 0.5])
ax.set_ylim([-0.5, 0.5])

# Create lines for the links
link1, = ax.plot([], [], 'o-', lw=2)
link2, = ax.plot([], [], 'o-', lw=2)

# Create points for the joints
joint1, = ax.plot([], [], 'ro')
joint2, = ax.plot([], [], 'ro')
end_effector, = ax.plot([], [], 'go')

def animate(i):
    theta1 = theta1_values[i] + offset_angle
    theta2 = theta2_values[i] + offset_angle


    end_effector_pos = forward_kinematics(theta1, theta2, 0.3, 0.2)
    joint2_pos = joint_pos(theta1, L1=0.3)

    # Update the plot
    link1.set_data([0, joint2_pos[0]], [0, joint2_pos[1]])
    link2.set_data([joint2_pos[0], end_effector_pos[0]], [joint2_pos[1], end_effector_pos[1]])

    joint1.set_data(0, 0)
    joint2.set_data(joint2_pos[0], joint2_pos[1])
    end_effector.set_data(end_effector_pos[0], end_effector_pos[1])


    return link1, link2, joint1, joint2, end_effector


ani = FuncAnimation(fig, animate, frames=len(theta1_values), interval=50, blit=True)
plt.ylim([-0.5, 0.1])
plt.title('2 DOF Simulation Kinetic')
plt.xlabel('x (m)')
plt.xlabel('y (m)')
plt.grid()

plt.show()
