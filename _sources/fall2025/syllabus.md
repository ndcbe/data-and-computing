# Syllabus

*University of Notre Dame*
**Department of Chemical & Biomolecular Engineering**

## **CBE-60258-01: Advanced Data and Computing for Chemical Engineers**  
**Fall 2025**

**Meeting times & room:** Tue/Thu, 9:30–10:45 am, Nieuwland Hall 118  
**Instructor:** Brett Savoie ([bsavoie2@nd.edu](mailto:bsavoie2@nd.edu))  
**Teaching Assistant:** Bryan Piguave ([bpiguave@nd.edu](mailto:bpiguave@nd.edu))  
**Office hours:** *TBD (Instructor & TA will announce)*

---

## Course description
This graduate course develops practical computation for chemical engineers with a foundation in **linear algebra**, **probability & statistics**, and **modeling**, implemented in **Python**. We revisit core algorithms (LU/QR/SVD, least squares, GLMs, classification metrics, Newton/quasi-Newton, Gauss–Newton/Levenberg–Marquardt, constrained optimization) and apply them to realistic chemical‑engineering datasets and modeling tasks. Students will be required to complete assignments **in both Python and by hand**.

## Learning outcomes
By the end of the term, students will be able to:
- Model and solve linear systems robustly (pivoting, conditioning, reuse of factorizations).
- Use QR/SVD to diagnose rank deficiency; compute least‑squares and minimum‑norm solutions.
- Interpret covariance and PSD structure; apply statistical inference (MLE, MAP, Bayesian updating).
- Design and assess models (GLMs, classification) with AIC/BIC, cross‑validation, ROC/PR.
- Implement and compare nonlinear solvers (Newton, quasi‑Newton) and *nonlinear least squares*.
- Model noisy systems with realistic uncertainty and data.

## Software & computing
Python 3.x with NumPy, SciPy, Matplotlib, and Pandas; Jupyter recommended. **This is not an introductory Python class.** Class time will focus on theory, algorithms, and implementation. If you have no background in Python you can still succeed, but you will need to do extra work outside of class to complete many assignments.

## Class Materials
All class notes will be distributed via Canvas or the course web book: <https://ndcbe.github.io/data-and-computing>.

## Assessments & policies
**Quiz policy.** Short quizzes at the start of most classes. **Five lowest quiz scores are dropped.**  
**Homework.** Assigned regularly; **due weekly on Thursdays** (submission details announced in class/Canvas).  
**Exams.** Two in‑class exams plus a comprehensive final.  
**Late work.** Unless otherwise announced, late homework is not accepted; plan ahead.  
**Collaboration.** Discuss approaches with peers, but submit your own code/solutions.  
**Honor Code.** The University of Notre Dame Honor Code applies to all work.

### Grade breakdown (100%)
| Component   | Weight |
|-------------|--------|
| Exam 1      | 20%    |
| Exam 2      | 20%    |
| Final exam  | 30%    |
| Homework    | 25%    |
| Quizzes     | 5%     |

### Exam dates
- **Exam 1 (Linear Algebra):** Thu 2025‑10‑02 (in class)  
- **Exam 2 (Statistics):** Thu 2025‑11‑06 (in class)  
- **Final exam:** Monday December 15, 7:30 pm – 9:30 pm (Location TBD)

---

## Tentative schedule

| Date       | Topic | Brief Description |
|------------|-------|-------------------|
| 2025-08-26 | Python review. | Fundamental objects and syntax. Common packages. |
| 2025-08-28 | Basic definitions in linear algebra: vectors, matrices, determinant, inner product | Core objects and operations in linear algebra; norms and orthogonality; geometric interpretations. Conditioning and why it matters in computation. |
| 2025-09-02 | Gaussian elimination & solving linear systems | Elimination, back‑substitution, and residual/error checks. Numerical stability, pivoting idea (preview), and interpreting solutions in `Ax=b` problems. |
| 2025-09-04 | LU (partial pivoting) & Cholesky | Stable factorization for general matrices (`PA = LU`) and efficient solvers for symmetric positive definite (SPD) matrices (`A = LL^T`). When to use each in practice; complexity and reuse of factors. |
| 2025-09-09 | Matrix spaces: column space, null space | Rank, independence, and the structure of solution sets. Interpreting tall systems and consistency via column space; null space as degrees of freedom. |
| 2025-09-11 | Row space, orthogonal complements, bases, Gram–Schmidt | Building orthonormal bases; geometry of orthogonal complements. Modified Gram–Schmidt and the link to QR for stable projections. |
| 2025-09-16 | Rank‑deficient problems: tall `A` in `Ax=b` | Least‑squares formulation; normal equations vs. QR/SVD solutions. Regularization preview and diagnostics for ill‑conditioning. |
| 2025-09-18 | Eigendecomposition, matrix functions & orthogonal matrices | Spectral theorem, diagonalization, and matrix functions (polynomials, exponential). Orthogonal matrices and stability. |
| 2025-09-23 | SVD & underdetermined problems: wide `A` in `Ax=b` | SVD for pseudoinverses, minimal‑norm solutions, and low‑rank structure. Connections to compression, noise filtering, and constrained degrees of freedom. |
| 2025-09-25 | Positive definite matrices & applications | Quadratic forms, PD/PSD tests, and energy/convexity interpretations. Why PD matters in optimization, estimation, and numerical stability. |
| 2025-09-30 | Probability & random vectors: expectation, covariance, PSD | Random vectors, moments, and covariance as a PSD operator. Linear transformations, sample vs. population quantities, and empirical estimation. |
| 2025-10-02 | **In‑class exam #1 (Linear Algebra)** | Cumulative in‑class assessment covering the linear algebra module. |
| 2025-10-07 | Common distributions; linear transformations | Gaussian and exponential family basics; multivariate normal geometry. Transformations of random vectors and propagation of mean/covariance. |
| 2025-10-09 | Change of variables, Jacobians, uncertainty propagation | Jacobians and volume scaling; practical change‑of‑variables examples. First‑order and Monte‑Carlo uncertainty propagation in models. |
| 2025-10-14 | Maximum entropy & chemical‑engineering applications | Entropy as uncertainty; deriving distributions from constraints (maxent → exponential family). Links to statistical thermodynamics and prior modeling. |
| 2025-10-16 | Estimation theory: moments, MLE, Fisher information | Principles of parameter estimation; identifiability and variance bounds (Cramér–Rao). Using information matrices to reason about parameter precision. |
| 2025-10-21 | No class | Fall Break. |
| 2025-10-23 | No class | Fall Break. |
| 2025-10-28 | Hypothesis testing: LRTs, confidence ellipsoids | Likelihood‑based tests; interpreting p‑values and power. Multivariate confidence regions (ellipsoids) and Hotelling’s T² perspective. |
| 2025-10-30 | Bayesian inference: conjugacy, Maximum a Posteriori (MAP), updating | Prior → posterior mechanics for common models; MAP as regularization. Predictive distributions and sequential updating. |
| 2025-11-04 | Statistics capstone (incl. experimental design) | End‑to‑end inference on a chemical‑engineering case: objectives, efficient designs (D/A/E‑optimality), data collection/analysis, and communicating uncertainty. |
| 2025-11-06 | **In‑class exam #2 (Statistics)** | Cumulative in‑class assessment covering the statistics module. |
| 2025-11-11 | Generalized linear models (GLMs) & model assessment; Akaike and Bayesian Information Criteria (AIC/BIC) & CV | Link functions, deviance, and when GLMs are appropriate. Model comparison and validation under realistic data conditions. Heteroscedastic/Homoscedastic. |
| 2025-11-13 | Classification overview; Receiver Operator Characteristic (ROC) & precision–recall | Linear Discriminant Analysis (LDA), logistic classifier, SVM concepts. Evaluation under imbalance with ROC/PR and calibration. |
| 2025-11-18 | Newton–Raphson & quasi‑Newton for nonlinear equations | Root‑finding for vector systems; Jacobians/Hessians, line search vs. trust‑region ideas. Convergence behavior and practical safeguards. |
| 2025-11-20 | Nonlinear least squares: Gauss–Newton & Levenberg–Marquardt | Parameter estimation for nonlinear models; weighting, scaling, and robust losses. Implementation details that affect convergence. |
| 2025-11-25 | Constrained optimization: Lagrange multipliers & KKT | Equality/inequality constraints; optimality conditions and sensitivities. Brief look at QPs and engineering design constraints. (May opt for global optimization: genetic algorithms/particle swarm optimization instead). |
| 2025-11-27 | Thanksgiving Break — no class | No meeting (university holiday). |
| 2025-12-02 | MAP estimation & Bayesian nonlinear models (MCMC overview) | Priors as regularization in nonlinear settings; Laplace approximation intuition. Overview of MCMC (Metropolis–Hastings/HMC). |
| 2025-12-04 | Gaussian process regression & surrogate modeling | Nonparametric regression with kernels; posterior mean/variance and hyperparameter learning. Emulation of expensive ODE/PDE models for design and UQ. |
| 2025-12-09 | Capstone integration: parameter estimation + UQ | Full pipeline: model specification → estimation (deterministic/Bayesian) → validation → uncertainty propagation/sensitivity → decision support. Emphasis on reproducible computation. |

---

## Accessibility & well‑being
Students needing accommodations are encouraged to contact the instructor early. If challenges affect your well‑being or coursework, please reach out; we will help connect you with campus resources.

## AI Use Policy
**For home assignments:** By default you *can* use AI assistance on any home assignment/project. There may be assignments where the instructor will forbid AI use.  

**In class quizzes and exams:** By default you *cannot* use AI assistance for in‑person assignments and exams. There may be times that AI use is explicitly allowed.

## Updates
This syllabus may be adjusted to improve pacing/learning; changes will be announced in class and on the course site.
