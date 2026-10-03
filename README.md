# Machine Learning with Python for Power Engineering

This repository contains the materials, examples, and practical exercises for a graduate-level course on **Machine Learning with Python for Electrical Power Engineering**.

The course is designed primarily for **M.Sc. and Ph.D. students in Electrical Engineering, especially Power Engineering**, who want to learn how Python, machine learning, scientific computing, optimization, simulation, and data analysis can be applied to modern power and energy systems.

The objective of this course is not only to teach machine learning algorithms, but also to introduce a practical Python ecosystem that can support research in power systems, renewable energy, smart grids, power electronics, optimization, fault diagnosis, forecasting, and related areas.

---

## Course Objectives

By the end of this course, students should be able to:

- Use Python for scientific and engineering computing.
- Work efficiently with NumPy, Pandas, Matplotlib, and SciPy.
- Prepare, clean, visualize, and analyze engineering datasets.
- Understand the fundamental concepts of machine learning.
- Implement regression and classification algorithms.
- Evaluate machine learning models using appropriate performance metrics.
- Apply machine learning to electrical power engineering problems.
- Build reproducible data-processing and simulation workflows.
- Use Python libraries related to power system analysis and optimization.
- Connect Python to external engineering and mathematical environments.
- Develop research-oriented computational projects using Python.

---

# Course Structure

The repository is organized into several modules.

## 1. Python Fundamentals

Topics include:

- Python syntax
- Variables and data types
- Lists, tuples, dictionaries, and sets
- Conditional statements
- Loops
- Functions
- Classes and object-oriented programming
- File handling
- Exception handling
- Python modules and packages
- Virtual environments

---

## 2. Scientific Computing with Python

Main libraries:

### NumPy

Numerical computing and multidimensional arrays.

Topics:

- Arrays and matrices
- Vectorized operations
- Linear algebra
- Eigenvalues and eigenvectors
- Random number generation
- Matrix manipulation

### SciPy

Scientific and engineering computation.

Applications include:

- Numerical integration
- Differential equations
- Optimization
- Signal processing
- Interpolation
- Statistics

### Pandas

Data processing and analysis.

Topics include:

- DataFrames
- CSV and Excel files
- Missing data
- Filtering
- Grouping
- Statistical analysis
- Time-series data

### Matplotlib

Scientific visualization.

Examples include:

- Line plots
- Scatter plots
- Histograms
- Bar charts
- Contour plots
- Engineering figures suitable for research papers

---

# 3. Machine Learning Fundamentals

This section introduces the main concepts of machine learning.

Topics include:

- Supervised learning
- Unsupervised learning
- Training, validation, and testing
- Feature engineering
- Feature scaling
- Overfitting and underfitting
- Bias and variance
- Cross-validation
- Hyperparameter tuning
- Model evaluation

---

# 4. Regression

Regression algorithms covered in the course include:

- Linear Regression
- Polynomial Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regression
- Random Forest Regression
- Support Vector Regression
- K-Nearest Neighbors Regression

Typical power engineering applications may include:

- Load forecasting
- Renewable power prediction
- Voltage estimation
- Power loss estimation
- State estimation
- Battery state estimation

---

# 5. Classification

Classification algorithms include:

- Logistic Regression
- K-Nearest Neighbors
- Support Vector Machines
- Decision Trees
- Random Forests
- Naive Bayes
- Ensemble methods

Example applications:

- Power system fault classification
- Equipment condition monitoring
- Cyberattack detection
- Transformer fault diagnosis
- Power quality disturbance classification
- Protection system applications

---

# 6. Unsupervised Learning

Topics include:

- K-Means
- DBSCAN
- Hierarchical Clustering
- Principal Component Analysis
- Dimensionality reduction
- Anomaly detection

Possible applications:

- Operating-state identification
- Event clustering
- Customer load profiling
- Power system anomaly detection
- Fault pattern discovery

---

# 7. Neural Networks and Deep Learning

An introduction to deep learning concepts and applications.

Topics may include:

- Artificial Neural Networks
- Multilayer Perceptrons
- Backpropagation
- Activation functions
- Training neural networks
- Convolutional Neural Networks
- Recurrent Neural Networks
- LSTM networks
- Deep learning for time-series analysis

Possible power engineering applications include:

- Load forecasting
- Renewable energy forecasting
- Fault detection
- Predictive maintenance
- Cyberattack detection
- Power quality analysis

---

# 8. Optimization in Python

Optimization is an important part of power and energy engineering.

Topics include:

- Linear Programming
- Mixed-Integer Linear Programming
- Nonlinear Optimization
- Constrained Optimization
- Multi-objective Optimization

Possible libraries include:

- SciPy Optimization
- PuLP
- Pyomo
- CVXPY
- Wolfram Language through `wolframclient`

Applications may include:

- Economic dispatch
- Unit commitment
- Optimal power flow
- Energy management
- Distributed generation planning
- Battery scheduling
- Electric vehicle scheduling

---

# 9. Python for Power System Analysis

Several Python libraries can be used for power system studies.

Examples include:

### pandapower

Power system modeling and analysis.

Possible studies:

- Power flow
- Optimal power flow
- Short-circuit analysis
- State estimation
- Network topology studies

### PyPSA

Python for Power System Analysis.

Applications include:

- Power system planning
- Renewable energy integration
- Energy system optimization
- Storage modeling
- Transmission planning

### GridCal

A Python-based power system analysis framework supporting several network analysis and optimization tools.

---

# 10. Real-Time and Event-Based Simulation

Python can also be used to demonstrate real-time and discrete-event simulation concepts.

## SimPy

SimPy is a process-based discrete-event simulation framework.

The course includes examples using:

```python
from simpy.rt import RealtimeEnvironment
```

Students will learn how simulation time can be synchronized with real wall-clock time.

Possible applications include:

- Energy management simulation
- Load scheduling
- EV charging events
- Communication delays
- Smart-grid event simulation
- Cyber-physical system demonstrations

---

# 11. Python and Wolfram Language

Python can communicate directly with the Wolfram Engine using the official:

```text
wolframclient
```

library.

Installation:

```bash
pip install wolframclient
```

Example:

```python
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr

session = WolframLanguageSession()

result = session.evaluate(
    wlexpr("N[Integrate[Sin[x]^2, {x, 0, Pi}]]")
)

print(result)

session.terminate()
```

This allows Python applications to use Wolfram Language capabilities such as:

- Symbolic mathematics
- Equation solving
- Differential equations
- Optimization
- Mixed-Integer Linear Programming
- Analytical modeling
- Mathematical simplification

A typical workflow can be:

```text
Python
   |
   | wolframclient
   v
Wolfram Kernel
   |
   | Symbolic / Numerical Computation
   v
Results
   |
   v
Python
   |
   +-- NumPy
   +-- Pandas
   +-- Matplotlib
   +-- Machine Learning
```

---

# 12. Signal Processing

Signal processing is particularly important in electrical engineering applications.

Possible topics include:

- FFT
- Spectral analysis
- Digital filtering
- Time-frequency analysis
- Feature extraction
- Wavelet transforms

Libraries may include:

- SciPy Signal
- PyWavelets
- NumPy
- Matplotlib

Applications include:

- Fault signal analysis
- Power quality analysis
- Harmonic analysis
- Condition monitoring
- Protection systems

---

# 13. Data Acquisition and Communication

Depending on the course projects, Python may also be used for communication with external systems.

Possible topics include:

- Serial communication
- TCP/IP communication
- Modbus
- MQTT
- Data logging
- Sensor data acquisition
- Real-time monitoring

Useful libraries may include:

```text
pyserial
pymodbus
paho-mqtt
socket
```

---

# 14. Research-Oriented Applications

Students are encouraged to apply the methods introduced in the course to research problems such as:

- Load forecasting
- Renewable energy forecasting
- Power system fault detection
- Transformer diagnosis
- Power quality classification
- Cyberattack detection
- Smart grid monitoring
- Energy management
- Optimal power flow
- Unit commitment
- Battery management
- Electric vehicle integration
- Microgrid control
- Power system stability assessment
- Predictive maintenance
- Anomaly detection

---


# Installation

It is recommended to use a dedicated Python virtual environment.

Create a virtual environment:

```bash
python -m venv power_ml_env
```

Activate it on Windows:

```bash
power_ml_env\Scripts\activate
```

Activate it on Linux or macOS:

```bash
source power_ml_env/bin/activate
```

Install the basic scientific Python packages:

```bash
pip install numpy pandas scipy matplotlib scikit-learn
```

Additional packages can be installed depending on the examples:

```bash
pip install simpy pandapower pypsa pyomo pulp cvxpy wolframclient
```

---

# Recommended Development Environment

The recommended environment for this course is:

- Python
- Visual Studio Code
- Jupyter Notebook
- Git
- GitHub

Useful VS Code extensions include:

- Python
- Jupyter
- GitHub integration
- Wolfram Language

---

# Example Workflow

A typical engineering machine learning workflow used throughout the course is:

```text
Engineering System
       |
       v
Data Acquisition / Simulation
       |
       v
Data Preprocessing
       |
       v
Feature Engineering
       |
       v
Machine Learning Model
       |
       v
Training and Validation
       |
       v
Performance Evaluation
       |
       v
Engineering Interpretation
```

The emphasis of the course is not only on obtaining high machine learning accuracy, but also on understanding the **engineering meaning of the data, features, model outputs, and limitations**.

---

# Prerequisites

Students are expected to have basic knowledge of:

- Electrical engineering
- Power systems
- Engineering mathematics

Previous programming experience is helpful but not strictly required.

The required Python concepts will be introduced progressively throughout the course.

---

# Target Audience

This course is primarily intended for:

- M.Sc. students in Electrical Engineering
- Ph.D. students in Electrical Engineering
- Researchers in Power and Energy Systems
- Students working on Smart Grids
- Researchers working on Renewable Energy
- Researchers interested in AI applications in Electrical Engineering

---

# Course Philosophy

The main philosophy of this course is:

> **Python should be treated not only as a machine learning language, but as a complete research and engineering environment.**

Therefore, the course combines:

```text
Python Programming
        +
Scientific Computing
        +
Machine Learning
        +
Optimization
        +
Simulation
        +
Power Engineering
        =
Research-Oriented Engineering Workflow
```

---

# License

This repository is intended for educational and research purposes.

Please provide appropriate citation or acknowledgment when using course materials in academic work.

---

# Instructor

**Dr. Behrooz Taheri**

behrooztaheri1372@gmail.com

---

## Contributions

Suggestions, corrections, and contributions that improve the educational materials are welcome.

Students are encouraged to explore the examples, modify the codes, test alternative methods, and develop their own research-oriented applications.
