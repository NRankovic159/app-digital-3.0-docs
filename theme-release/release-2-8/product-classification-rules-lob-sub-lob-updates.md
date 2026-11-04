# [2.8] Product Classification Rules — LOB & Sub LOB Updates

Release 2.8

## Overview

Release 2.8 adds classification rules for the new products announced since August 2026 and includes a set of fixes and optimizations to the existing Product String Classification Rules. Ten of the 14 new products are already classified correctly by the current rules. The Home products (Apple HomeView, HomePod mini 2 and Apple TV 4K 4th generation) needed five new rules. Rules are evaluated from top to bottom and the last matching rule wins, so the new product rules are added at the end of the ruleset. After the release the ruleset contains 88 rules.

## New Products

All new product keys were verified in Adobe and return the expected LOB and Sub LOB.

| # | New product | Expected LOB | Expected Sub LOB | Rules |
|---|---|---|---|---|
| 1 | iPhone 18 Pro | iPhone | iPhone 18/Plus/Pro/Pro Max | Existing rules |
| 2 | iPhone 18 Pro Max | iPhone | iPhone 18/Plus/Pro/Pro Max | Existing rules |
| 3 | iPhone Duo | iPhone | iPhone Duo | Existing rules |
| 4 | Apple Watch Series 12 | Watch | Watch Series | Existing rules + Fix 7 |
| 5 | Apple Watch Ultra 4 | Watch | Watch Ultra | Existing rules + Fixes 7, 8 |
| 6 | AirPods 5 | AirPods | AirPods Non Pro | Existing rules |
| 7 | Mac mini M6 | Mac | Mac Mini | Existing rules |
| 8 | Mac mini M5 Pro | Mac | Mac Mini | Existing rules |
| 9 | Mac Studio M5 Max | Mac | Mac Studio | Existing rules |
| 10 | Mac Studio M5 Ultra | Mac | Mac Studio | Existing rules + Fix 8 |
| 11 | Apple HomeView (tabletop) | Home | Apple HomeView | Add Rules 73–74 at the end of the ruleset |
| 12 | Apple HomeView (Wall Mounted) | Home | Apple HomeView | Add Rules 73–74 at the end of the ruleset |
| 13 | HomePod mini 2 | Home | HomePod mini 2 | Add Rule 75 at the end of the ruleset |
| 14 | Apple TV 4K (4th generation) | Home | Apple TV 4K (4th generation) | Add Rules 76–77 at the end of the ruleset |

## Fixes

Rule mismatches fixed in this release.

| # | Issue | Expected LOB | Expected Sub LOB | Fix Method |
|---|---|---|---|---|
| 1 | Smart Folio, Bands — missing “\|” in Rule 52, accessory override never fired | Accessories | iPad Accessories | Fix Rule 52 |
| 2 | Non-English accessory names (Husa, Funda, Custodia, Kryt…) — wrong LOB | Accessories | iPhone Accessories | Add Rule 52b; update Rules 53, 55 |
| 3 | iPad Entry — Rule 24 too narrow | iPad | iPad Entry | Rewrite Rule 24 as RegEx |
| 4 | Apple Pencil — no dedicated rule | iPad | iPad Accessories | Add Rules 20b, 59; update Rule 54 |
| 5 | Apple Watch full-device SKUs (SKU codes, S11, GPS / Cellular, case + band) — treated as accessories | Watch | Watch Series / SE / Ultra | Update Rules 48, 51, 61; add Rules 51b, 61b, 61c, 62 |
| 6 | Watch Bands & Straps — wrong LOB, strap pattern unreliable | Watch | Watch Accessories | Add Rule 52d; update Rule 56 |
| 7 | Apple Watch — Rule 62 saved as Sub LOB instead of LOB, Sub LOB showed “Watch” | Watch | Watch Series / SE / Ultra | Set Rule 62 to LOB = Watch |
| 8 | “Ultra” without “Watch” (Mac Studio Ultra, SanDisk Ultra) — landed in Watch Ultra | Mac | Mac Studio | Update Rules 48, 50, 61 |
| 9 | iPad “Standard Glass” — classified as Accessories | iPad | iPad Pro | Update Rule 60; add Rule 63 |
| 10 | AirPods with charging case, AirPods Pro 3 — classified as Accessories | AirPods | AirPods Pro | Add Rules 37b, 58, 72 |
| 11 | iPhone 16e — merged into iPhone 16 | iPhone | iPhone e-line (SE-successor) | Add Rule 19b |
| 12 | Beats — no LOB rule | Beats | Beats | Add Rules 39b, 39c |
| 13 | AppleCare+ — spread over device LOBs | Services | AppleCare+ | Add Rules 64–65 |
| 14 | Software Subscriptions — fell to Accessories | Services | Software Subscriptions | Add Rules 66–67 |
| 15 | Gift Cards — attributed to a device LOB | Services | Gift Cards | Add Rules 68–69 |

## Optimizations

| # | Optimization | LOB | Sub LOB | Method |
|---|---|---|---|---|
| 1 | Duplicate rules 26, 30, 32 removed | — | — | Remove duplicates |
| 2 | Language-independent accessory check (for / per / para / für + device) | Accessories | by device | Add Rule 52c |
| 3 | Protection rules keep device LOB / Sub LOB when accessory words are present | AirPods / iPad | AirPods Pro / iPad Accessories | Add Rules 37b, 58, 59, 60 |
| 4 | Apple Services (Apple One, Apple Music, Apple Arcade…) — prepared in advance | Services | Apple Services | Add Rules 70–71 |
