# [2.8] PDP Page Size & Total Blocking Time Reduction

## Overview

This document covers the performance engineering work carried out in Release 2.8 to reduce page size and total blocking time (TBT) on the Product Detail Page (PDP). The original request covered PDP, Homepage, and PLP; however, under this ticket only PDP 2.0 was updated. Homepage and PLP optimizations are not included in this release.

Performance was measured using Lighthouse in a controlled test configuration across 5 runs per phase (Initial baseline and After AI Update), on both desktop and mobile. The results are compared below across all Core Web Vital metrics.

## Test Configuration

All tests were run in a consistent environment to ensure comparability between the Initial and After AI Update phases.

| Setting | Value |
|---|---|
| Theme version | 2.8 |
| PDP version | PDP 2.0 |
| User state | Not logged in |
| Product type | Not a bundle product |
| Browser mode | Incognito |
| Test URL | `https://appstaging-demo.dev/products/15-inch-macbook-air-mryr3ll-a` |
| Test runs | 5 runs per phase (Initial + After AI Update) |

## Initial Results (Baseline)

### DESKTOP — Initial (5 Runs)

| Run | Performance | FCP | LCP | TBT | CLS | Speed Index |
|---|---|---|---|---|---|---|
| 1 | 82 | 1.1s | 2.3s | 0ms | 0.001 | 2.3s |
| 2 | 76 | 1.1s | 3.0s | 0ms | 0.001 | 2.5s |
| 3 | 84 | 1.2s | 1.8s | 0ms | 0.004 | 2.5s |
| 4 | 83 | 1.0s | 2.0s | 0ms | 0.001 | 2.5s |
| 5 | 91 | 1.0s | 1.3s | 0ms | 0.011 | 2.0s |

### Desktop Initial — Averages

| Metric | Average |
|---|---|
| Performance Score | 83.2 |
| First Contentful Paint (FCP) | 1.08s |
| Largest Contentful Paint (LCP) | 2.08s |
| Total Blocking Time (TBT) | 0ms |
| Cumulative Layout Shift (CLS) | 0.0036 |
| Speed Index | 2.36s |

### MOBILE — Initial (5 Runs)

| Run | Performance | FCP | LCP | TBT | CLS | Speed Index |
|---|---|---|---|---|---|---|
| 1 | 60 | 3.0s | 8.1s | 180ms | 0 | 7.9s |
| 2 | 59 | 3.1s | 8.5s | 190ms | 0 | 8.2s |
| 3 | 61 | 3.2s | 6.4s | 210ms | 0 | 7.2s |
| 4 | 61 | 3.1s | 8.3s | 190ms | 0 | 6.6s |
| 5 | 63 | 2.8s | 6.1s | 190ms | 0 | 8.1s |

### Mobile Initial — Averages

| Metric | Average |
|---|---|
| Performance Score | 60.8 |
| First Contentful Paint (FCP) | 3.04s |
| Largest Contentful Paint (LCP) | 7.48s |
| Total Blocking Time (TBT) | 192ms |
| Cumulative Layout Shift (CLS) | 0 |
| Speed Index | 7.6s |

## After AI Update Results

### DESKTOP — After AI Update (5 Runs)

| Run | Performance | FCP | LCP | TBT | CLS | Speed Index |
|---|---|---|---|---|---|---|
| 1 | 88 | 0.9s | 1.4s | 0ms | 0.097 | 2.2s |
| 2 | 89 | 1.1s | 1.5s | 0ms | 0.008 | 2.1s |
| 3 | 89 | 1.1s | 1.5s | 0ms | 0.007 | 2.0s |
| 4 | 91 | 0.9s | 1.4s | 0ms | 0.007 | 1.9s |
| 5 | 89 | 1.0s | 1.6s | 0ms | 0.007 | 2.1s |

### Desktop After — Averages

| Metric | Average |
|---|---|
| Performance Score | 89.2 |
| First Contentful Paint (FCP) | 1.0s |
| Largest Contentful Paint (LCP) | 1.48s |
| Total Blocking Time (TBT) | 0ms |
| Cumulative Layout Shift (CLS) | 0.0252 |
| Speed Index | 2.06s |

### MOBILE — After AI Update (5 Runs)

| Run | Performance | FCP | LCP | TBT | CLS | Speed Index |
|---|---|---|---|---|---|---|
| 1 | 61 | 3.1s | 5.7s | 250ms | 0 | 7.8s |
| 2 | 58 | 3.3s | 9.3s | 200ms | 0 | 8.0s |
| 3 | 63 | 2.4s | 9.9s | 200ms | 0 | 6.3s |
| 4 | 60 | 3.0s | 10.3s | 230ms | 0 | 6.3s |
| 5 | 66 | 2.9s | 5.2s | 200ms | 0 | 6.9s |

### Mobile After — Averages

| Metric | Average |
|---|---|
| Performance Score | 61.6 |
| First Contentful Paint (FCP) | 2.94s |
| Largest Contentful Paint (LCP) | 8.08s |
| Total Blocking Time (TBT) | 216ms |
| Cumulative Layout Shift (CLS) | 0 |
| Speed Index | 7.06s |

## Comparison Summary

The tables below compare averaged results across all 5 test runs for both phases. Green rows indicate improvement; red rows indicate regression; amber rows indicate no meaningful change.

### DESKTOP — Performance Change Summary

| Metric | Initial | After 2.8 | Change | Status |
|---|---|---|---|---|
| Performance Score | 83.2 | 89.2 | +6.0 | ✓ +7.2% improvement |
| FCP | 1.08s | 1.0s | -0.08s | ✓ Slight improvement |
| LCP | 2.08s | 1.48s | -0.60s | ✓ 28.8% improvement |
| TBT | 0ms | 0ms | 0ms | → No change |
| CLS | 0.0036 | 0.0252 | +0.0216 | ✕ ~600% increase |
| Speed Index | 2.36s | 2.06s | -0.30s | ✓ 12.7% improvement |

### MOBILE — Performance Change Summary

| Metric | Initial | After 2.8 | Change | Status |
|---|---|---|---|---|
| Performance Score | 60.8 | 61.6 | +0.8 | ✓ Slight improvement |
| FCP | 3.04s | 2.94s | -0.10s | ✓ Slight improvement |
| LCP | 7.48s | 8.08s | +0.60s | ✕ 8% degradation |
| TBT | 192ms | 216ms | +24ms | ✕ 12.5% increase |
| CLS | 0 | 0 | 0 | → No change |
| Speed Index | 7.6s | 7.06s | -0.54s | ✓ 7.1% improvement |

## Key Findings

### Desktop — Strong Improvements

- Performance score improved from 83.2 to 89.2 (+7.2%).
- LCP improved significantly: 2.08s → 1.48s, a 28.8% reduction. Now comfortably in the “Good” range (≤ 2.5s).
- Speed Index improved from 2.36s to 2.06s (-12.7%).
- TBT remained at 0ms on desktop across all 10 test runs.
- CLS increased from 0.0036 to 0.0252 — still within the “Good” threshold (≤ 0.1) but warrants monitoring, particularly Run 1 which scored 0.097.

### Mobile — Mixed Results

- Performance score marginally improved: 60.8 → 61.6 (+0.8). Mobile performance remains in the “Needs Improvement” band.
- Speed Index improved from 7.6s to 7.06s (-7.1%).
- FCP slightly improved: 3.04s → 2.94s.
- LCP degraded: 7.48s → 8.08s (+8%). High variance across runs (5.2s–10.3s) indicates instability in the mobile simulation environment.
- TBT increased: 192ms → 216ms (+12.5%). Both values exceed the “Good” threshold (≤ 200ms) on mobile. This is an area that requires further optimisation.
- CLS remained at 0 on mobile across all runs.
