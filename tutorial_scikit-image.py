import numpy as np 
from skimage import data, io, filters
from skimage.filters import thresholding
from skimage.feature import peak_local_max, canny
from skimage.measure import regionprops
import matplotlib.patches as mpatches
from skimage.morphology import label
from matplotlib import pyplot as plt

image = data.coins()[0:95, 70:370]
fig, axes = plt.subplots(ncols=2, nrows=3, figsize=(8, 4))

ax0, ax1, ax2, ax3, ax4, ax5 = axes.flat
ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title('Original', fontsize=24)
ax0.axis('off')

# Histogram.
values, bins = np.histogram(image,
bins=np.arange(256))
ax1.plot(bins[:-1], values, lw=2, c='k')
ax1.set_xlim(xmax=256)
ax1.set_yticks([0, 400])
ax1.set_aspect(.2)
ax1.set_title('Histogram', fontsize=24)

# Apply threshold.
bw = thresholding.threshold_local(image, 95, offset=-15)
ax2.imshow(bw, cmap=plt.cm.gray)
ax2.set_title('Adaptive threshold', fontsize=24)
ax2.axis('off')

# Find maxima.
coordinates = peak_local_max(image, min_distance=20)
ax3.imshow(image, cmap=plt.cm.gray)
ax3.autoscale(False)
ax3.plot(coordinates[:, 1], coordinates[:, 0])
ax3.set_title('Peak local maxima', fontsize=24)
ax3.axis('off')

# Detect edges.
edges = canny(image, sigma=3, low_threshold=10, high_threshold=80)
ax4.imshow(edges, cmap=plt.cm.gray)
ax4.set_title('Edges', fontsize=24)
ax4.axis('off')

# Label image regions.
label_image = label(edges)
ax5.imshow(image, cmap=plt.cm.gray)
ax5.set_title('Labeled items', fontsize=24)
ax5.axis('off')
for region in regionprops(label_image):
  # Draw rectangle around segmented coins.
  minr, minc, maxr, maxc = region.bbox
  rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr, fill=False, edgecolor='red', linewidth=2)
  ax5.add_patch(rect)
  plt.tight_layout()

edges = filters.sobel(image)
io.imshow(image)
plt.show()