import serial
import time
import pandas as pd
import numpy as np
from io import StringIO

class esp32Communication:
    def __init__(self, port='COM4', baudrate=115200, timeout=0.1):
        self.esp32 = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)

    def read_port(self):
        packet = self.esp32.readline()
        return packet.decode('utf').rstrip('\n')
        
    def close(self):
        self.esp32.close()

def file_treat(data_recieve):
    data = np.array(data_recieve)
    data_div = data.astype(float)
    colunms_name = ['Angle']
    df = pd.DataFrame(data_div, columns=colunms_name)
    return df

if __name__ == "__main__":
    esp32_comm = esp32Communication()
    try:
        data_list = []
        while True:
            try:
                value = esp32_comm.read_port()
                time.sleep(0.5)
                data_list.append(value)
            except KeyboardInterrupt:
                print("\nProgram interrupted by user. Exiting...")
                break
    finally:
        pass
    # Convertir los datos en un df
    df = file_treat(data_list)

    # Guarda los archivos en un csv
    csv_filename = 'angle_data.csv'
    df.to_csv(csv_filename, index=False)
    print(f'Data saved to {csv_filename}')
