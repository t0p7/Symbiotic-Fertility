# Analysis Methods

## IDW Phosphorus Gradient Interpolation

Inverse-distance-weighted interpolation is applied to map phosphorus
concentration across the sample grid. Each measurement point contributes
to neighbouring estimates inversely proportional to its distance squared.

## SF-3 Kinetics Model

The SF-3 model predicts reproductive phase onset from hyphal density and
ambient phosphorus levels using a three-parameter sigmoid fit calibrated
against longitudinal field data.

## Hyphal Density Calculation

Density estimates use a sliding-window kernel approach, optimised for
datasets exceeding 100,000 sample points via vectorised NumPy operations.
