#!/usr/bin/env python
# riesa@isi.edu (Jason Riesa)
#
# Extract a weight vector from a particular training iteration
# from a weights file.
# Usage:
# ./extract-weights.py <weights_file> <iteration_number> <output_file>
# For example, to extract the weights from the 7th epoch of training:
# ./extract-weights.py training.weights 7 training.weights-7

import sys
import json
import pysvector as svector

if __name__ == "__main__":

  # Print usage.
  if len(sys.argv) != 4:
    sys.stderr.write("Usage: %s %s %s %s\n" %(sys.argv[0], "<weights>", "<iter>", "<output-name>"))
    sys.exit(1)

  # Open weights file for reading.
  try:
    wf = open(sys.argv[1],'r')
  except:
    sys.stderr.write("Could not open weights file %s for reading.\n" %(sys.argv[1]))
    sys.exit(1)

  # Get iteration number we are interested in.
  try:
    iter = int(sys.argv[2])
  except:
    sys.stderr.write("Argument <iter> must be an integer. Received: %s\n" %(sys.argv[2]))
    sys.exit(1)

  # Open output file for writing.
  try:
    filename = sys.argv[3]+'.weights-%d' %(iter)
    out = open(filename, 'w')
  except:
    sys.stderr.write("Could not open output file %s for writing.\n" %(filename))
    sys.exit(1)

  # one epoch per line
  for i,line in enumerate(wf):
    if i == iter:
       w = json.loads(line)
  if iter > i:
      sys.stderr.write("Error: %i epochs found in file, but epoch %i requested\n" %(i, iter))
      sys.exit(1)

  # Write weight vector to output file
  sys.stderr.write("%d components\n" %(len(w)))
  json.dump(w,out)
  out.close()
  wf.close()
