# GORUT-OUTBREAK AI v26 — Statistical Validation & Model Audit

v26 extends the v25 Research Studio with a browser-side model audit layer.

## Added
- Logistic model audit: n, events, events/parameter, log-likelihood, AIC, BIC.
- Brier score and simple 0.50 classification accuracy.
- Hosmer–Lemeshow-style calibration screening.
- VIF screening for numeric/coded covariates.
- Crude vs full nested logistic model comparison using a likelihood-ratio statistic.
- Persistent audit results in research state.

## Important limitations
This is a decision-support prototype, not a replacement for R/Stata/SAS/SPSS or independent statistical review. The audit does not automatically solve separation, non-linearity in the logit, clustering, survey weights, matching, informative missingness, multiple imputation, complex sampling, or external validation. Model assumptions and design-specific methods must be reviewed before thesis/dissertation/publication or official use.
