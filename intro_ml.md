# Data Science and Machine Learning

## Introduction to Machine Learning

---

**Machine learning** is the subfield of Articial Intelligence within the realm of Computer Science focused on developing computational models learned from implicity patterns in the data for achieving results without being explicity programmed to achieve them.

### Basic Vocabulary

To learn patterns from data, a machine learning model requires a **dataset** ($\mathcal{D}$). A dataset is a collection of $N$ **observations** (also referred to as **instances**) represented as $\mathcal{D} = \{\mathbf{x}_i\}_{i=1}^N$ for unsupervised learning or $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^N$ for supervised learning.

Each instance ($\mathbf{x}_i$ or $(\mathbf{x}_i, y_i)$) is a individual observation in the dataset consisting of:
* **Feature Vector** ($\mathbf{x} \in \mathcal{X}$ or $\mathbf{x}^{(i)}$): An $d$-dimensional vector $\mathbf{x} = [x_1, x_2, \dots, x_d]^T$ of measurable features (independent / explanatory variables or values) with a well-defined order describing a given observation. Features are accessible at both training and inference time (including evaluation).
* **Target Variable** ($y \in \mathcal{Y}$): In (semi-)supervised learning, the dependent variable representing the ground-truth outcome that the model is optimized to infer. The target value for a given instance is called a **label**. Labels are present during training and evaluation to compute loss $\mathcal{L}(f(\mathbf{x}), y)$, but they are absent during unlabelled inference.

### Types of Machine Learning
There are different types of machine learning: supervised, semi-supervised, unsupervised and reinforcement learning. 

**Supervised Learning**
The model learns the functional relation $f: X \to Y$ using a dataset of input-output pairs $\mathcal{D} = \{(x^{(i)}, y^{(i)}\}_{i=1}^N$, where $x^{(i)}$ represents the feature vector and y^{(i)} represents the ground-truth label.

**Semi-Supervised Learning**
The model learns from a dataset containing a small fraction of labeled instances $\{(x_i, y_i)\}_{i=1}^l$ alongside a significantly larger fraction of unlabeled instances $\{x_j\}_{j=l+1}^{l+u}$ with $l \ll u$.

**Unsupervised Learning**
The model learns patterns from an unlabeled dataset $\mathcal{D} = \{(x^{(i)}\}_{i=1}^N$, such as: 
* *Underlying structures*: geometric-topological structures formed by the data points in the original space, $x_i \in \mathcal{X}$ = $\mathbb{R}^d$, such as clusters, connected graphs or low-dimensional sub-manifold (a smooth, continuous surface, space, where the data exist).
* *Latent features*: unobserved, compressed variables $Z \in \mathbb{R}^k$ with $k \ll d$ capturing the salient factors of variation that generate the observed high-dimensional feature vector $x \in \mathbb{R}^d$. 
* *Data distributions*: probability density function $p(x)$ across the sample space, defining the likelihood of any given observation $x \in \mathcal{X}$.

**Reinforcement Learning**
The model is an agent that learns to optimize a decision-making strategy (policy or value function) by maximazing an expected cumulative utility metric derived from evaluative feedback signals over a collection of trajectory.
* **Feedback**: Evaluative feedback signal is a non-instructive (as opposed to supervised learning) signal that measures the quality of executed behavior given the state(s) that it was taken.
* **Policy**: A function mapping the state space $\mathcal{S}$ to a probability distribution over the action space $\mathcal{A}$:
$$
\pi(a \mid s) = \mathbb{P}(A_t = a \mid S_t = s)
$$
* **Trajectory** $(\tau)$: A collection of states, actions and observations.
* **Value Function** ($V$ or $Q$): The estimated future returns from a given state $V(s)$ or state-action pair $Q(s,a)$. It may be also seen as the conditional expectation of the cumulative utility metric.
* **Utility**: The expected cumulative utility metric is the statistical expectation of aggregated return over an operational horizon, typically scaled by a discount factor $\gamma \in [0, 1)$ to bound infinite sums.
