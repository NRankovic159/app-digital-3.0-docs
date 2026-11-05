# Sticky Footer — Inconsistent Behaviour in Safari vs Non-Safari (Mobile)

## Bug Description

The PDP (Product Detail Page) sticky footer displayed inconsistent behaviour between Safari and non-Safari mobile browsers when the user scrolled the page. In non-Safari browsers (Chrome, Firefox), both the Checkout button and the Add to Cart button remained visible throughout scrolling. However, in Safari on mobile, the Apple Pay button disappeared while scrolling, leaving only the Add to Cart button visible.

This inconsistency created a degraded checkout experience for Safari users, who represent the primary Apple device user base. The Apple Pay button — the primary express checkout action for Safari users — was intermittently hidden exactly when users were most likely to act on it.

{% hint style="warning" %}
**Root Cause**

Safari on iOS handles the viewport height and scroll position differently from other mobile browsers, particularly around the address bar collapse behaviour. The sticky footer CSS relied on viewport height calculations that Safari interpreted differently during scroll, causing the Apple Pay button container to be pushed out of the visible sticky area.
{% endhint %}

## Before Fix: Inconsistent Behaviour

The table below shows the sticky footer behaviour across browsers before the fix was applied.

| Behaviour | Non-Safari (Chrome, Firefox) | Safari — BEFORE fix |
|---|---|---|
| Buttons visible while scrolling | ✓ Checkout + Add to Cart (both visible) | ✓ Apple Pay + Add to Cart (both visible) |
| Apple Pay / Checkout button | ✓ Checkout button stays visible | ✕ Apple Pay button hidden during scroll (bug) |
| Add to Cart button | ✓ Visible | ✓ Visible |
| Footer sticky behaviour | ✓ Consistent | ✕ Inconsistent — footer partially collapses |

## After Fix: Consistent Behaviour

After the fix in Release 2.8, sticky footer behaviour is consistent between Safari and all other mobile browsers. Both buttons remain visible throughout scrolling on all browsers.

| Behaviour | Non-Safari (Chrome, Firefox) | Safari — AFTER fix |
|---|---|---|
| Buttons visible while scrolling | ✓ Checkout + Add to Cart (both visible) | ✓ Apple Pay + Add to Cart (both visible) |
| Apple Pay / Checkout button | ✓ Checkout button stays visible | ✓ Apple Pay button stays visible |
| Add to Cart button | ✓ Visible | ✓ Visible |
| Footer sticky behaviour | ✓ Consistent | ✓ Consistent — parity with non-Safari |

## Fix Detail

The fix addresses the Safari-specific viewport height and scroll behaviour that caused the Apple Pay button to be hidden. The correction ensures the sticky footer renders with consistent height and button visibility across all mobile browsers.

- **CSS viewport fix:** Sticky footer height calculation updated to use Safari-compatible CSS viewport units (dvh/svh where supported, with fallback) to prevent the footer collapsing during the Safari address bar scroll animation.
- **Apple Pay container:** Apple Pay button container flex/visibility rules reviewed to ensure the button is not inadvertently hidden by overflow or height constraints during scroll on Safari.
- **Scope:** The fix is applied in the Shopify Theme 2.8 CSS and does not require any changes to the Apple Pay integration or button logic.
- **Non-Safari impact:** Non-Safari browsers are unaffected. The Checkout fallback button (introduced separately in Release 2.8) and the Add to Cart button continue to behave as before on Chrome and Firefox.

## Steps of Implementation

The fix was implemented and verified in the following sequence:

1. **Reproduce and confirm root cause:** Reproduce the bug on Safari iOS and confirm the sticky footer collapse coincides with the address bar show/hide animation during scroll, validating the viewport height root cause.
2. **Update CSS viewport units:** Replace the fixed viewport height calculation in the sticky footer CSS with Safari-compatible dvh/svh units, including a fallback for browsers without support, so the footer no longer collapses during the Safari scroll animation.
3. **Review the Apple Pay button container:** Audit the Apple Pay button container's flex and visibility rules to confirm it is not clipped by overflow or height constraints while the address bar animates.
4. **Deploy via Shopify Theme 2.8:** Ship the CSS changes as part of the Shopify Theme 2.8 release. No changes are required to the Apple Pay integration or button logic itself.
5. **Regression test across browsers and PDP versions:** Verify sticky footer behaviour on Safari and non-Safari mobile browsers, on both PDP 1.0 and PDP 2.0, confirming the Apple Pay/Checkout button and Add to Cart button remain visible throughout scroll.

## Affected Context

| Property | Detail |
|---|---|
| Page affected | Product Detail Page (PDP) |
| PDP version(s) affected | PDP 1.0 and PDP 2.0 — sticky footer behaviour and this fix apply to both template versions |
| Component | Sticky footer (Add to Cart + Apple Pay / Checkout button row) |
| Platform affected | Mobile devices running Safari (iOS) |
| Platform unaffected | Chrome, Firefox, and all non-Safari mobile browsers |
| Trigger | Occurs when the user scrolls the PDP page on Safari mobile |
| Symptom | Apple Pay button hidden; only Add to Cart button remains visible during scroll |
| User impact | Safari users could not access Apple Pay during scroll, reducing express checkout discoverability |
| Status | ✓ Fixed in Release 2.8 |
