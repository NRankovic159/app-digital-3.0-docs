# AppleCare+ PDP Auto-Bundling & Upsell Drawer

Enables customers to seamlessly configure and attach official AppleCare+ warranty coverage during device configuration on the Product Detail Page (PDP).

| Workstream / Domain | Audience Scope | Support Intake Channel | Minimum Theme Required |
|---|---|---|---|
| Features & Functionalities | All Global Partners (Shopify & CX-S) | Wrike: Feature Support #APP-FEAT | v3.4.0 (Shopify) / Figma Token Kit v2026.3 (CX-S) |

{% hint style="warning" %}
**Placeholder content.** This page follows the partners' draft of the Knowledge Wiki. All data (versions, dates, metrics, contacts) is an example to be replaced with real information.
{% endhint %}

{% tabs %}

{% tab title="💼 Business Overview" %}
## 1. Executive Summary & Conversion Value

The AppleCare+ Auto-Bundling module embeds Apple warranty options directly within the customer's purchase decision on the PDP (adjacent to device color and storage capacity selection), rather than relying on forgotten cart-page popups.

| Business KPI | Observed Partner Impact | Pre-requisites |
|----|----|----|
| **Warranty Attachment Rate** | **+18.4%** increase in AppleCare+ units per eligible hardware device | Active partner agreement with AppleCare Services |
| **Average Order Value (AOV)** | **+\$149 to +\$199** lift on flagship iPhone & Mac configurations | CaaS API automated SKU linking enabled |
| **Cart Abandonment** | **No negative impact** (Inline drawer eliminates disruptive checkout modals) | Shopify theme v3.4+ or CX-S Token Kit v2026.3 |

## 2. Customer Experience & Flow

When a customer selects an eligible device (e.g. iPhone 16 Pro 256GB), the theme automatically checks the CaaS product matrix for matching AppleCare+ SKUs:

- **Step 1 (Inline Card):** A clean Apple-branded card appears below the capacity selector: *"Protect your iPhone with AppleCare+ for \$199"*.
- **Step 2 (Details Drawer):** Clicking *"Coverage Details"* slides out an accessible modal explaining accidental damage, theft & loss protection, and 24/7 priority support.
- **Step 3 (One-Click Bundling):** Adding to bag automatically pairs the hardware SKU with the AppleCare+ SKU, maintaining bundle integrity through checkout.
{% endtab %}

{% tab title="🛠️ Engineering Guide" %}
## 1. Shopify Implementation (For Theme Developers)

In Theme v3.4+, the AppleCare+ module is an Online Store 2.0 Section block located in `sections/main-product.liquid`.

### Step 1: Enable Block in Shopify Customizer

Navigate to *Shopify Admin \> Online Store \> Customize \> Default Product template*. In the left panel under **Product Information**, click **Add block** and select **AppleCare+ Bundler**.

### Step 2: Liquid Snippet Configuration

``` text
{% comment %} Liquid snippet: snippets/applecare-bundle-drawer.liquid {% endcomment %}
{% if product.metafields.app_digital.applecare_eligible %}
  <div class="applecare-bundler-container" data-parent-sku="{{ product.selected_or_first_available_variant.sku }}">
    <div class="applecare-toggle-card">
      <input type="checkbox" id="applecare-toggle" name="properties[_applecare_attached]" value="true">
      <label for="applecare-toggle">
        <span class="applecare-title">Add 2 Years of AppleCare+ Coverage</span>
        <span class="applecare-price">{{ product.metafields.app_digital.applecare_price | money }}</span>
      </label>
    </div>
  </div>
{% endif %}
```

## 2. CX-S Implementation (Custom Engines / Figma Tokens)

For custom platform partners (Magento, SAP Commerce, headless React):

- **Figma Component Link:** Inspect component ` Components / PDP / WarrantyDrawer_v2026.3` in your shared APP Figma library.
- **CSS Design Tokens:** Border radius: `var(--radius-lg, 12px)`; Surface background: `#f5f5f7`; Accent toggle: `#0071e3`.
- **Cart API Binding:** Ensure your backend cart API receives parameter `bundled_parent_sku` so warranty returns are tied to hardware returns.
{% endtab %}

{% tab title="📜 Version Changelog" %}
## Version Changelog: AppleCare+ Bundler

| Version | Release Date | Changes & Enhancements | Impact |
|----|----|----|----|
| **v3.4.1** | 2026-10-28 | Fixed iOS 26 Safari WebKit drawer animation lag; added localized French/German currency formatting. | Patch hotfix |
| **v3.4.0** | 2026-09-12 | Initial production rollout of AppleCare+ PDP Auto-Bundling drawer; dynamic CaaS SKU binding. | New feature release |
{% endtab %}

{% endtabs %}
