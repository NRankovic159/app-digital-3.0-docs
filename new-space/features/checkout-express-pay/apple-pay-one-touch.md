---
layout:
  width: wide
---

# Apple Pay & One-Touch Express Checkout

Integration guidelines for displaying official Apple Pay branded express payment buttons on Product Detail Pages and Mini-Cart drawers.

| Workstream / Domain | Audience Scope | Support Intake Channel | Minimum Theme Required |
|---|---|---|---|
| Features & Functionalities | All Global Partners (Shopify & CX-S) | Wrike: Feature Support #APP-FEAT | v3.2.0 (Shopify) / CX-S Guidelines v2026.1 |

{% tabs %}

{% tab title="💼 Business Overview" %}
## 1. Executive Summary & Value

Apple Pay Express Checkout eliminates checkout friction by allowing Apple device users to complete purchases in seconds using Touch ID, Face ID, or Optic ID without filling out billing and shipping forms.

Partners adopting the PDP one-touch Apple Pay button report a **24% to 32% increase in mobile conversion** on high-velocity items like AirPods and Apple Watch accessories.
{% endtab %}

{% tab title="🛠️ Engineering Guide" %}
## 1. Shopify Implementation

Apple Pay is supported natively via Shopify Payments or authorized gateways (Adyen, Stripe):

``` text
<!-- Ensure Shopify dynamic checkout buttons are enabled -->
{{ form | payment_button }}

<style>
  .shopify-payment-button__button--branded {
    border-radius: 8px !important;
    min-height: 48px !important;
  }
</style>
```
{% endtab %}

{% tab title="📜 Version Changelog" %}
## Version Changelog: Apple Pay

| Version | Changes                                                          |
|---------|------------------------------------------------------------------|
| v3.2.0  | Initial release of PDP Apple Pay button placement guidelines.    |
| v3.3.1  | Added multi-currency support for cross-border European partners. |
{% endtab %}

{% endtabs %}

{% hint style="warning" %}
**Placeholder content.** This page follows the partners' draft of the Knowledge Wiki. All data (versions, dates, metrics, contacts) is an example to be replaced with real information.
{% endhint %}
