import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')

def calcular_punto(x, y, radio, angulo):
    x_nuevo = x + radio * np.cos(angulo)
    y_nuevo = y - radio * np.sin(angulo)  # Se cambia el signo para orientar hacia abajo
    return x_nuevo, y_nuevo

def dibujar_brazo(punto1, punto2, punto3, angulo_min, angulo_max):
    fig, ax = plt.subplots()

    # Calcular radio entre puntos 1 y 2
    radio_1_2 = np.linalg.norm(np.array(punto2) - np.array(punto1))
    
    # Calcular radio entre puntos 2 y 3
    radio_2_3 = np.linalg.norm(np.array(punto3) - np.array(punto2))

    # Calcular radio entre puntos 1 y 3
    radio_1_3 = np.linalg.norm(np.array(punto3) - np.array(punto1))

    # Ángulos
    theta = np.linspace(angulo_min, angulo_max, 100)

    # Dibujar arco entre puntos 1 y 2 con área difuminada
    x_arc_1_2, y_arc_1_2 = calcular_punto(punto1[0], punto1[1], radio_1_2, theta)
    ax.fill_between(x_arc_1_2, y_arc_1_2, punto2[1], color='blue', alpha=0.2, label='Área 1-2')

    # Dibujar arco entre puntos 2 y 3 con área difuminada
    angles_2 = np.linspace(np.radians(90), np.pi - np.radians(20), 100)
    x_arc_2_3, y_arc_2_3 = calcular_punto(punto2[0], punto2[1], radio_2_3, angles_2)
    ax.fill_between(x_arc_2_3, y_arc_2_3, punto3[1], color='green', alpha=0.2, label='Área 2-3')

    # Dibujar arco entre puntos 1 y 3 con área difuminada
    x_arc_1_3, y_arc_1_3 = calcular_punto(punto1[0], punto1[1], radio_1_3, theta)
    ax.fill_between(x_arc_1_3, y_arc_1_3, punto3[1], color='red', alpha=0.2, label='Área 1-3')

    # Dibujar líneas entre los puntos
    ax.plot([punto1[0], punto2[0]], [punto1[1], punto2[1]], color='blue')
    ax.plot([punto2[0], punto3[0]], [punto2[1], punto3[1]], color='green')
    ax.plot([punto1[0], punto3[0]], [punto1[1], punto3[1]], color='red')

    # Añadir joints en los puntos
    ax.plot(punto1[0], punto1[1], 'ro', color='blue',  label='Cadera')
    ax.plot(punto2[0], punto2[1], 'ro', color='green', label='Rodilla')
    ax.plot(punto3[0], punto3[1], 'ro', color='red',label='Tobillo')

    # Configuraciones adicionales
    ax.set_aspect('equal', adjustable='datalim')
    plt.xlabel('X (m)')
    plt.ylabel('Y (m) ')
    plt.title('Área de trabajo de una pierna')
    plt.legend()
    plt.grid(True)
    plt.show()

# Definir puntos
punto1 = np.array([0, 0])
punto2 = np.array([0, -0.43])
punto3 = np.array([0, (-0.43 -0.36)])

# Ángulos máximos y mínimos
angulo_min = np.radians(70)
angulo_max = np.pi - np.radians(70)

# Dibujar el área de trabajo con joints y arcos con áreas difuminadas
dibujar_brazo(punto1, punto2, punto3, angulo_min, angulo_max)
