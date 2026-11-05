# H1 & H2 Heading Tag Corrections

## Background

A partner’s SEO agency identified a series of technical heading tag issues across the Shopify theme. These issues affect both SEO (search engine interpretation of page hierarchy and content relevance) and web accessibility (assistive technologies rely on a correct heading structure to help users navigate pages). All identified issues have been resolved in Shopify Theme 2.8.

The fixes span three areas: H1/H2 heading tag corrections, empty heading tag cleanup, and schema.org structured data updates. This document focuses on the heading tag changes. Structured data changes (Organisation, Product, ItemList) are documented alongside.

{% hint style="info" %}
**Why Heading Tags Matter for SEO & Accessibility**

Search engines use H1 and H2 tags to understand page structure and content hierarchy. A page with multiple H1 tags, empty heading tags, or content in `<div>` elements instead of `<h2>` sends unclear signals and can suppress rankings. Accessibility standards (WCAG) require a logical, single-H1 heading structure so screen readers can navigate page content correctly.
{% endhint %}

## Complete Fix Summary

All issues identified by the SEO agency have been resolved in Theme 2.8. The table below provides a compact reference of every fix.

| # | Issue | Scope | Fix | Status |
|---|---|---|---|---|
| 1 | Empty `<h2>` tags present sitewide | Sitewide | Empty `<h2>` tags removed | ✓ Fixed |
| 2 | `<h2>` “Your basket is empty” (Cart) | Sitewide | Removed from Cart page | ✓ Fixed |
| 3 | Logo has no H1 / H1 not descriptive | Homepage | H1 added to logo with descriptive aria-label | ✓ Fixed |
| 4 | Category names not in H2 tags | Homepage | Category/stripe titles wrapped in `<h2>` | ✓ Fixed |
| 5 | Category names not in H2 tags | PLP | Product category names wrapped in `<h2>` | ✓ Fixed |
| 6 | Two H1 tags on PDP | PDP | Second H1 removed; single H1 per PDP | ✓ Fixed |
| 7 | Two H1 tags on Cart page | Cart | Duplicate H1 removed; single H1 on Cart | ✓ Fixed |
| 8 | Page stripe titles in `<div>` not `<h2>` | Home/LOB/PLP | Stripe/section titles promoted from `<div>` to `<h2>` | ✓ Fixed |
| 9 | Organisation schema on every page | Sitewide | Organisation schema retained on HP only | ✓ Fixed |
| 10 | ItemList schema.org missing on PLPs | PLP | ItemList schema.org added on all PLPs | ✓ Fixed |

## Correct Heading Structure by Page Type

The table below defines the expected heading structure for each page type after the 2.8 fixes. This serves as the reference for future development and QA.

| Page | Expected H1 | H2 Elements | Notes |
|---|---|---|---|
| Homepage | Logo (descriptive alt/aria) | Category names (each stripe/section), no empty H2s | Logo H1 added. Category names promoted from `<div>` to `<h2>`. |
| LOB Page | Page/LOB title | Section titles wrapped in H2 (previously `<div>`) | Stripe titles now wrapped in H2. |
| PLP | Collection title | Product category names as H2; ItemList schema added | H2 for categories; structured data updated. |
| PDP | Product name (single H1 only) | Section headings as H2 | Second H1 removed. Only one H1 per PDP now. |
| Cart | Cart title (single H1 only) | Section headings | Duplicate H1 (“Your basket is empty”) removed. One H1 on cart page. |
| All pages | — | Empty H2 tags removed | Sitewide cleanup of empty `<h2>` tags. |

## Detailed Fix Breakdown

### FIX 1 — Empty `<h2>` Tags Removed (Sitewide)

Empty heading tags were found across multiple pages. These are invisible to users but are crawled by search engines and read by screen readers, causing confusion in both contexts.

**BEFORE — Empty H2 — Sitewide**

```html
<h2></h2>
<h2>   </h2>
```

**AFTER — Empty H2 — Sitewide**

```html
<!-- empty heading tags removed -->
<!-- no output rendered -->
```

### FIX 2 — “Your Basket is Empty” H2 Removed (Cart)

The cart page rendered “Your basket is empty” inside an H2 tag even when the cart contained items. This created an incorrect and misleading heading that conflicted with the page’s actual H1 and state.

**BEFORE — Cart — Empty basket H2**

```html
<h2>Your basket is empty</h2>
<!-- shown regardless of cart state -->
```

**AFTER — Cart — Empty basket H2**

```html
<!-- removed: condition-aware empty state
     handled via non-heading element -->
```

### FIX 3 — H1 Added to Logo (Homepage)

The homepage had no H1 at all, or the H1 was non-descriptive. The logo is the primary identity element on the homepage and is the correct anchor for the H1. An aria-label provides the descriptive text for search engines and screen readers.

**BEFORE — Homepage — Logo H1**

```html
<a href="/" class="logo-link">
  <img src="logo.svg" alt="Partner" />
</a>
```

**AFTER — Homepage — Logo H1**

```html
<h1>
  <a href="/" class="logo-link"
     aria-label="Partner — Apple Premium Partner">
    <img src="logo.svg" alt="Partner" />
  </a>
</h1>
```

### FIX 4 — Category Names Wrapped in H2 (Homepage)

Homepage section/stripe titles (e.g. product category names within promotional banners) were wrapped in `<div>` elements. These carry no semantic weight for SEO. Promoting them to `<h2>` correctly signals their importance to search engines.

**BEFORE — Homepage — Category/Stripe Titles**

```html
<div class="stripe-title">iPhone</div>
<div class="stripe-title">Mac</div>
```

**AFTER — Homepage — Category/Stripe Titles**

```html
<h2 class="stripe-title">iPhone</h2>
<h2 class="stripe-title">Mac</h2>
```

### FIX 5 — Category Names as H2 on PLP

Product category names on the PLP (Product Listing Page) were not marked up as heading tags. Wrapping them in `<h2>` correctly identifies them as sub-sections of the collection page for both SEO and accessibility.

**BEFORE — PLP — Category Names**

```html
<div class="category-name">Mac Accessories</div>
```

**AFTER — PLP — Category Names**

```html
<h2 class="category-name">Mac Accessories</h2>
```

### FIX 6 — Duplicate H1 Removed on PDP

The PDP (Product Detail Page) rendered two H1 tags: the product name (correct) and a secondary element that was also marked as H1 (incorrect). Having two H1 tags on a page is both an SEO and accessibility violation. The second H1 has been removed; only the product name H1 remains.

**BEFORE — PDP — Duplicate H1**

```html
<h1>Apple Watch Series 11</h1>
<!-- ... page content ... -->
<h1>Trade-In</h1>
<!-- two H1s on same page ✕ -->
```

**AFTER — PDP — Duplicate H1**

```html
<h1>Apple Watch Series 11</h1>
<!-- ... page content ... -->
<h2>Trade-In</h2>
<!-- single H1, section promoted to H2 ✓ -->
```

### FIX 7 — Duplicate H1 Removed on Cart Page

The Cart page contained two H1 tags: the cart title and the “Your basket is empty” state. This violates WCAG accessibility guidelines and SEO best practices. The cart page now has a single H1.

**BEFORE — Cart — Duplicate H1**

```html
<h1>Your Cart</h1>
<!-- ... cart items ... -->
<h1>Your basket is empty</h1>
<!-- two H1s on cart page ✕ -->
```

**AFTER — Cart — Duplicate H1**

```html
<h1>Your Cart</h1>
<!-- ... cart items ... -->
<p class="empty-state">Your basket is empty</p>
<!-- single H1; empty state uses <p> ✓ -->
```

### FIX 8 — Stripe/Section Titles Promoted from `<div>` to `<h2>` (Home, LOB, PLP)

A broader audit identified that many page section titles across the Homepage, LOB (Line of Business) pages, and PLP were wrapped in `<div>` elements with CSS styling to look like headings visually, but carried no semantic heading value. All such titles have been promoted to `<h2>` tags.

**BEFORE — LOB Page — Section Titles**

```html
<div class="section-heading">
  Featured Products
</div>
```

**AFTER — LOB Page — Section Titles**

```html
<h2 class="section-heading">
  Featured Products
</h2>
```

### FIX 9 — Organisation Schema Scoped to Homepage Only (Sitewide)

The schema.org Organisation structured data block was being output on every page of the site. Best practice is to include Organisation schema only on the Homepage, where it contextually represents the business. Duplicate Organisation schema across all pages adds noise without benefit and may dilute structured data signals.

**BEFORE — Organisation Schema — Scope**

```html
<!-- Output on EVERY page: -->
<script type="application/ld+json">
  { "@type": "Organization", ... }
</script>
```

**AFTER — Organisation Schema — Scope**

```liquid
<!-- Output on Homepage ONLY: -->
{% if template == "index" %}
<script type="application/ld+json">
  { "@type": "Organization", ... }
</script>
{% endif %}
```

### FIX 10 — ItemList Schema Added on PLPs

schema.org ItemList structured data was missing on all PLP pages. ItemList markup allows search engines to display rich results for product collections, improving click-through rates from search. It has been added to all PLPs in Theme 2.8.

**BEFORE — PLP — ItemList Schema**

```html
<!-- No ItemList schema present on PLP ✕ -->
```

**AFTER — PLP — ItemList Schema**

```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Mac Accessories",
    "itemListElement": [
        { "@type": "ListItem", "position": 1,
          "url": "/products/magic-mouse" },
        ...
    ]
}
</script>
```
