import struct
import numpy as np
import random
from scipy import signal as sg

f = 440                       ## Frequency (in Hz)
samplerate = 44100                ## Number of samples

x = np.arange(630840)/float(samplerate)

####### sine wave ###########
#y = np.int16(np.random.uniform(-20000,20000,630840) )
y = np.int16(np.random.randint(-20000,20000,630840) )

####### square wave ##########
# y = 100* sg.square(2 *np.pi * f *x / Fs )

####### square wave with Duty Cycle ##########
# y = 100* sg.square(2 *np.pi * f *x / Fs , duty = 0.8)

####### Sawtooth wave ########
# y = 100* sg.sawtooth(2 *np.pi * f *x / Fs )

import numpy as np
from scipy.io.wavfile import write

write('test.wav', samplerate, y)

'''
###### in jupyter, play generated audio #####
import numpy
import random
from IPython.display import Audio

print(random.randint(1,300))
Audio(numpy.sin(numpy.linspace(0, 3000, 20000)*random.randint(1,300)), rate=8000)
'''
