import threading
import time

class Banco():
    def __init__(self, turno = 0):
        self.locked = threading.Lock()
        self.turn_send = turno
        
    def asignar_turno(self):
        self.locked.acquire()
        
        try:
            self.turn_send += 1
            print('Turno a pasar: ',self.turn_send)
            print('Tiempo a esperar 10 min aprox')
            time.sleep(10)
        finally:
            self.locked.release()
            
def solicitar_turno(x):
    
    for y in range(2):
        x.asignar_turno()
        
        
if __name__ == '__main__':
    banco = Banco()
    for y in range(2):
        tstart = threading.Thread(target=solicitar_turno, args=(banco,))
        tstart.start()