# Template: Code Release Runbook

````markdown
# Release Runbook: [Service/App Name] - v[X.Y.Z]

## 1. Release Overview
- **Target Release Date/Time:** [YYYY-MM-DD HH:MM TZ]
- **Release Commander / DRI:** @[Name]
- **On-Call Support / SRE:** @[Name]
- **Target Environments:** [Staging -> Canary (5%) -> Production (100%)]
- **Release Tracking Ticket / PR:** [Link to Radar / GitHub PR / Jira]

## 2. Scope & Changelog
- **Included Features:**
  - [Feature Name]: [Brief description & link]
- **Bug Fixes:**
  - [Bug ID]: [Fix summary]
- **Breaking Changes / DB Migrations:** [None | Yes - see Pre-requisites]

## 3. Pre-Deployment Checklist
- [ ] Code frozen and regression tests passed on Staging.
- [ ] Database migrations backward-compatible & tested.
- [ ] Monitoring dashboards open and baselines noted.
- [ ] Feature flags configured in management portal ([Flag Key]: [Default Off]).
- [ ] Customer Support / Ops team notified in `#[slack-channel]`.

## 4. Step-by-Step Execution Plan
| Step # | Action | Command / Portal Link | Executed By | Verification / Health Check |
|---|---|---|---|---|
| 1 | Enable maintenance banner (if applicable) | [Link / Flag] | @[Name] | Check web/app client |
| 2 | Run DB migration script | `db:migrate --step` | @[Name] | Verify schema version |
| 3 | Deploy to Canary (5%) | [Deployment Tool Link] | @[Name] | Error rate < 0.05% for 15 mins |
| 4 | Deploy to Production (100%) | [Deployment Tool Link] | @[Name] | CPU, memory & latency nominal |
| 5 | Toggle Feature Flag | [Config UI] | @[Name] | Test live flow in canary user |

## 5. Rollback Procedure
*Criteria to trigger rollback: Error rate spike > [1%], P99 latency > [500ms], or blocker customer bug.*
1. **Immediate Abort Command:** `[Paste rollback script / UI button link]`
2. **Database Rollback:** `[Paste down-migration script]`
3. **Feature Flag Killswitch:** Turn flag `[flag_name]` to `OFF`.
4. **Stakeholder Communication:** Post update to `#[incident-or-ops-channel]`.

## 6. Post-Deployment Verification (Sign-off)
- [ ] Core user journey smoke-tested manually.
- [ ] Sentry / Splunk / Datadog error alerts silent for 30 minutes.
- [ ] Release status declared **GREEN** in `#[release-announcements]`.
````
