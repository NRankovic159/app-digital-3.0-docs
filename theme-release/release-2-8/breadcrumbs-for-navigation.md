# [2.8] Breadcrumbs for Navigation

## Overview

This document describes the breadcrumb navigation implementation in the Shopify theme for Release 2.8. Breadcrumbs serve two purposes: improving user wayfinding (helping customers understand where they are in the site hierarchy and navigate back to parent pages) and providing structured data for SEO (via schema.org BreadcrumbList JSON-LD markup).

The implementation is primarily powered by Shopify’s native breadcrumb capability. Breadcrumb path construction differs by page type, and not all page types support a full hierarchy trail automatically. This document clarifies how breadcrumbs behave across all page types, and sets out the proposal and trade-offs for handling the content page gap.

## Original Requirements

The following requirements were defined in the breadcrumb feature request and are addressed by this implementation.

- Breadcrumbs serve both navigation and SEO purposes.
- Breadcrumbs are positioned in or near the footer area, helping route users to relevant parts of the site.
- Footer content remains consistent site-wide but may vary contextually between high-level spaces (e.g. Support or Business may show a different footer than the B2C store).
- All breadcrumb items except the current page are clickable links leading to navigable pages.
- The root/home element uses “APP” or a home icon in place of the Apple logo.

## How Breadcrumbs Work in the Theme

Breadcrumbs in the Shopify theme operate differently depending on the type of page being viewed. There are few examples how old breadcrumbs was, and how they looks after 2.8 release.

Before 2.8 release:

After 2.8 reelease:

## Core Behaviour Rules

The following rules apply across all breadcrumb implementations in the theme, regardless of page type.

- The first level is always the Homepage, labelled as “APP” or rendered with the home icon. The Apple logo is not used.
- All breadcrumb items except the current page are hyperlinks leading to navigable pages.
- The current page (final item) is plain text — it is never a link.
- Breadcrumbs are accompanied by JSON-LD schema.org BreadcrumbList structured data for SEO. The markup reflects the visible trail exactly.
