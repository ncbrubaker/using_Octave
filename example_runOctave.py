from run_octave import RunOctave
import numpy as np

# Create the RunOctave object and explicitly add the path to octave-gui.exe
# octave = RunOctave(octave_path='C:/Program Files/GNU Octave/Octave-6.2.0/mingw64/bin/octave-gui.exe')
octave = RunOctave(octave_path='C:/Program Files/GNU Octave/Octave-7.1.0/mingw64/bin/octave-gui.exe')

A = np.array([[2, 0, 1],
              [-1, 1, 0],
              [-1, 1, 0],
              [-3, 3, 0]])

# Start Testing
m, n = octave.run(nargout=2, target='size', args=(A,))
print(m, n)

N = octave.run(nargout=1, target='vecnorm', args=(A, 2, 2))
print(N)

# Inserting expressions directly
X = octave.run(nargout=1, target='ones(4, 3) * 255;')
print(X)