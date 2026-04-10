# optirefine-benchmarks
# Optirefine: Python Optimization Benchmarks

## Objective
A benchmark suite demonstrating the performance delta between naive, LLM-generated Python scripts and production-grade $O(n)$ architecture. 

Frontier AI models frequently output syntactically correct code that fails at scale due to exponential time complexity or inefficient memory reallocation. These benchmarks serve as the baseline for the training datasets curated at [Optirefine](https://optirefine.carrd.co) to teach AI agents scalable implementation.

## Run Instructions
To run the benchmarks locally and verify the execution times on your own hardware:

bash
git clone https://github.com/yourusername/optirefine-benchmarks.git
cd optirefine-benchmarks
pip install -r requirements.txt
python main_benchmark.py


## The Benchmarks

### 01. State Dictionary Filtering
* **Bottleneck:** Inefficient $O(n \times m)$ dictionary rebuilding and missing key checks when loading custom model architecture.
* **Optimization:** $O(n)$ dictionary comprehensions and $O(1)$ Set difference lookups.

### 02. Contrastive Pair Matching
* **Bottleneck:** $O(n^2)$ nested batch loops comparing every label against every other label for positive pair generation.
* **Optimization:** $O(n)$ hash map grouping using `collections.defaultdict`.

### 03. Massive Sequence Tokenization
* **Bottleneck:** Dynamic memory reallocation causing CPU thrashing when processing 100k+ strings (e.g., NLP text or SMILES notation).
* **Optimization:** Pre-allocated C-level memory operations via `.join()`.

### 04. Custom PyTorch Dataloader
* **Bottleneck:** $O(n)$ line-by-line file reading inside the `__getitem__` method, which starves the GPU of data.
* **Optimization:** $O(1)$ byte-offset indexing computed during the `__init__` phase using `f.seek()`.

---
`// Maintained by Optirefine`
`// Specializing in Python optimization, custom transformer architecture, and high-volume dataset processing.`
