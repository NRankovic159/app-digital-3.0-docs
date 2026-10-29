# 2.8 Theme Release Notes

## Overview

**About v2.8**

Version 2.8 is a merchandising-and-conversion release. It introduces the Frequently bought together module — a multi-item "add all" block on the product page — together with automatic gift-with-purchase, energy-rating labels on product cards, and per-product order limits for controlling how many of an item a shopper can buy. A new Motif homepage preset ships alongside them to show off the content-section library in a ready-made layout.

The rest of the release is refinement: the cart now self-heals grouped add-on rows on load, frequently-bought-together cards can show a monthly-price line, recommendation de-duplication is tighter, and there is a round of performance and stability maintenance across the cart and product pages.

## Release Notes Document

{% file src="../.gitbook/assets/2.8-Theme-Release-Notes.pdf" %}
2.8 Theme Release Notes
{% endfile %}

## Highlights

### New in this release

**Frequently bought together**

A new product-page module shows the main product next to a short list of companion items, each with its own checkbox. A running total updates as items are ticked, and Add all puts everything in the cart as one grouped set — so a shopper buying a Test MacBook Pro 14 can add a compatible adapter and case in a single action instead of visiting each product.

**Gift with purchase**

When a product qualifies for a free-gift promotion, the eligible gift now attaches automatically as the shopper adds the qualifying item, and appears as a clearly labeled Free gift row in the cart and cart drawer. No code to enter and nothing for the shopper to hunt for.

**Motif homepage preset**

Motif is a new demo homepage layout you can apply from the theme editor. It arranges the existing content sections — stripes, image-with-text tiles, and the bento box — into a polished starting point, useful as a reference build or a fast way to restyle a seasonal landing page.

## Added

_New features, sections, or capabilities_

* Frequently bought together section for the product page, with per-item checkboxes, a running total, and a single Add all action.
* Gift with purchase — eligible free gifts attach automatically and show as a Free gift row in the cart.
* Energy-rating labels on product cards, with a details dialog for the full rating information.
* Per-product order limits — set a maximum purchasable quantity per product so shoppers can't exceed the cap.
* Motif homepage preset showcasing the content-section library.
* Auto-fill of the Frequently bought together module from Shopify's product recommendations when no items are hand-picked.

## Changed

_Enhancements, optimizations, and refinements_

* Grouped add-on rows in the cart now self-heal on page load, so an add-on always stays attached to its parent item.
* Frequently-bought-together cards can display a monthly-price line alongside the full price.
* Improved recommendation de-duplication so the same product no longer appears across multiple modules on one page.
* General maintenance and performance updates across the cart and product pages.

## Fixes

_Bug fixes and display issues_

**Product / Variant / Pricing**

* Monthly financing didn't recalculate when an add-on was toggled on or off.
* Fixed a variant price-morph edge case that could show a stale price on rapid variant selection.
* Sale badge could display the wrong value in some price configurations.

**Sections & Blocks**

* The Frequently bought together pending shell was mis-sized before the module finished loading, causing a layout shift.
* The recommendations carousel didn't advance correctly when it was scrolled off-screen and back.

**Cart & Cart Drawer**

* Corrected the alignment of nested add-on rows under their parent item.
* Fixed a quantity-sync race when the parent item's quantity was changed quickly.

**Accessibility & UX**

* Frequently-bought-together checkboxes now have correct, descriptive labels.
* Corrected the focus order through the add-all flow.

**Media / Display**

* Fixed the energy-rating details dialog image failing to load.
