import pandas as pd
import matplotlib.pyplot as plt
from collections import deque
import random
from loguru import logger

logger.add("testdata.log")

def read_my_data():
    try:
        mydata = pd.read_csv("EE411-012303-000742-eeg.txt", delimiter=" ", header=None)
        del mydata[10]
    except Exception:
        mydata = pd.DataFrame()
    finally:
        return mydata

que = deque(maxlen = 40)

while True:
    perc = random.random()
    que.append(perc)
	
	# PLOTTING THE POINTS
    plt.plot(que)
    plt.scatter(range(len(que)),que)

	# SET Y AXIS RANGE
    plt.ylim(-1,4)
	
	# DRAW, PAUSE AND CLEAR
    logger.info(f"{len(que)}")
    plt.draw()
    plt.pause(0.1)
    plt.clf()