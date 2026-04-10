# 🧬 MenuEvolver — GA Restaurant Optimizer

A production-quality Genetic Algorithm web application that evolves the
optimal weekly restaurant menu across profit, satisfaction, nutrition, and efficiency.

## Project Structure

```
project/
├── app.py              ← Flask backend
├── ga.py               ← Genetic Algorithm engine
├── templates/
│   └── index.html      ← Full frontend (dark luxury UI)
└── requirements.txt
```

## Setup & Run

```bash
# 1. Install dependencies
pip install flask

# 2. Run the server
python app.py

# 3. Open in browser
http://localhost:5000
```

## What Was Improved

### ga.py
| Feature | Before | After |
|---|---|---|
| Dish pool | 10 dishes | 20 dishes with emojis |
| Selection | Random top-15 | Tournament (k=7) |
| Crossover | Basic uniform | Uniform + duplicate repair |
| Mutation | Single swap | Swap + random replace |
| Elitism | None | Top 5 preserved |
| Fitness | 4 raw terms | 4 normalized scores (0–100) |
| Output | Basic dict | Full breakdown + diversity metric |

### app.py
- Fixed `__name__` / `__main__` syntax errors
- Added CORS headers for local dev
- Added `/dishes` endpoint for catalog
- Clean JSON responses

### index.html + style.css
- Dark luxury editorial aesthetic (Playfair Display + DM Mono fonts)
- Animated hero with grid background
- 6 GA concept cards with hover effects
- KPI cards with animated counters + progress bars
- Fitness score breakdown with 4 animated bar fills
- Menu table with animated row reveals + calorie color coding
- 4 Chart.js charts: fitness convergence, metrics trend, diversity, radar
- Full 20-dish catalog grid
- DNA loader animation during evolution
- Toast notifications

## GA Concepts Demonstrated

| Concept | Implementation |
|---|---|
| **Chromosome** | 7 unique dish IDs (permutation encoding) |
| **Fitness** | Weighted: profit(30%) + rating(30%) + calories(25%) + efficiency(15%) |
| **Selection** | Tournament selection, k=7 |
| **Crossover** | Uniform crossover with repair (85% rate) |
| **Mutation** | Swap or replace, 15% per gene |
| **Elitism** | Top 5 survive unchanged |
| **Diversity** | Hamming distance metric tracked per generation |
