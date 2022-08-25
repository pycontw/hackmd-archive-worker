# Using Lucid to Visualize Neural Networks - Yufeng Guo

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

<iframe src="https://app.sli.do/event/h1o4f1dc" height=450 width=100%></iframe>

> 從這開始


### Optimization "Objectives": What activations are we optimizing for?


### Diversity through dataset examples

* "Square"-like grid shapes vs. circular stripings
* Curvy 

### Shortcomings: Does not always make sense

* Perhaps neurons aren't the right semantic units for understanding neural units
* Random Combinations
* Hand-crafted Combinations
* Interpolating between 2 Neurons

---
## Lucid

* Infrastructure and tools for research in NN

### Structure Dictionary

* Activation: a combination of *many* neurons

### Detection Across Layers

* Edge in earlier layers
* More sophisticated shapes and object parts in later layers

### Scale Images by Activation Magnitude

* How does information propagate through the layers?
* Where are the important portions of the image?

### Spatial Attritubes with Saliency Maps

---
## Activation Athlases

* Individual Neurons $\rightarrow$ Parewise Interactions $\rightarrow$ Spatial Activations $\rightarrow$ Activation Atlas
* Compute activation grid for each of your (1 million) images
* UMAP (Uniform Manifold Approximation and Projection) to project down to 2D
* Draw a grid over the projection, and averge the activations per grid
* (Optional) Size the grid cells according to the density 

### Understand one specific classification

* E.g., Fireboat vs. Streetcar

---
## Resources

* Lucid GitHub https://github.com/tensorflow/lucid
* Activation Atlas - Distill.pub  https://distill.pub/2019/activation-atlas/
* Exploring Neural Networks with Activation Atlases https://ai.googleblog.com/2019/03/exploring-neural-networks.html

###### tags: `PyConTW2019`
