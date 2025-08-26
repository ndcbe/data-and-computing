# Schedule

## Assignments

| Deadline     | Description |
| ----------- | ----------- |
TBD

## Class Meetings


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
