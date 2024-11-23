from math import sin,cos
import matplotlib.pyplot as plt

class pedulum :
    G : float = 9.81
    size : float #en m
    masse : float #en gramme
    angle_initiale : float#en radians

    def __init__(self, size : float, masse : float, angle_initiale : float) -> None:
        self.size = size
        self.masse = masse
        self.angle_initiale = angle_initiale

    def newtone(self, time : float) -> float:
        return self.angle_initiale*cos((self.G/self.size)**0.5*time+0)
    
    def position(self, time : float) -> tuple[float,float] :
        tmp = self.newtone(time)
        return (cos(tmp),sin(tmp))
    
    def animation(self, duration : float, p : int = 16) -> None:
        if 0 < p <= 16 :
            teta = [self.newtone(simulation_time/16) for simulation_time in range(duration*16)]
            sinus = [sin(e) for e in teta]
            cosinus = [cos(self.newtone(e)) for e in teta]
            for x,y in zip(sinus,cosinus) :
                plt.scatter([x],[y])
                plt.show()
        else :
            raise Exception(f'Invalid p argument "{p}" was given but it must be like : 0 < p <= 16')

    def see(self, duration : float, p : int = 16) -> None:
        fig, (ax1, ax2) = plt.subplots(1, 2)
        teta = [self.newtone(simulation_time/10**p) for simulation_time in range(duration*10**p)]
        sinus = [sin(e) for e in teta]
        cosinus = [cos(self.newtone(e)) for e in teta]
        ax1.plot(range(duration*10**p),teta,label='0')
        ax1.plot(range(duration*10**p),sinus,label='sin(0)')
        ax1.plot(range(duration*10**p),cosinus,label='cos(0)')
        ax1.legend()
        ax1.set_title('Données')
        ax2.scatter(sinus,cosinus)
        ax2.set_title('Mouvement')
        plt.show()

import random
P = pedulum(100,random.random()*10,random.random())
P.see(10,1)
#P.animation(60,5)
