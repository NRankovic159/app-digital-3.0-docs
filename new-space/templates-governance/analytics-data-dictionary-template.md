# Template: Analytics & Metric Data Dictionary

````markdown
# Metric & Analytics Guide: [Domain / Product Area]

## 1. Core KPIs
| Metric Name | Business Definition | Formula / SQL Logic | Source Table / Tool | Owner |
|---|---|---|---|---|
| Daily Active Users (DAU) | Unique accounts with ≥1 session event | `COUNT(DISTINCT user_id) WHERE active_time > 0` | `analytics.fact_sessions` | @[Analyst] |
| Churn Rate (%) | Canceled subs / total active subs at start | `[Churned] / [Total Base]` | `billing.subscriptions` | @[PM] |

## 2. Event Tracking Schema (Instrumentation)
| Event Name | Trigger Moment | Key Parameters / Payload | Target Platforms |
|---|---|---|---|
| `checkout_completed` | User clicks final confirmation | `order_id` (str), `cart_value` (float), `currency` (str) | iOS, Web, Android |
| `feature_clicked` | User expands collapsible view | `feature_id` (str), `screen_source` (str) | iOS |

## 3. Official Dashboards & Reports
- **Executive Overview Dashboard:** [Tableau / Superset / Grafana Link] (Refreshed Daily at 06:00 UTC)
- **Operational Real-time Dashboard:** [Splunk / Datadog Link]
- **Raw Data Query Access:** Schema: `prod_dwh.public_marts.*`

## 4. Known Data Caveats & Historical Nuances
- *Pre-2026 data does not include guest checkout sessions.*
- *Timezone conversion: All timestamps stored in UTC.*
````
