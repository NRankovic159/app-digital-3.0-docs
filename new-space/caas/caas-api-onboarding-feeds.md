---
layout:
  width: wide
---

# Catalog-as-a-Service (CaaS PDX) Onboarding & Data Delivery Guide

Integration guide for receiving official Apple product master data, localized technical specs, imagery, and marketing copy via CaaS PDX (Product Data eXchange).

| Workstream / Domain | Audience Scope | Support Intake Channel | Minimum Theme Required |
|---|---|---|---|
| CaaS Operations | All Global Partners (Shopify & CX-S) | Wrike Queue #APP-CAAS | CaaS PDX v2.4 / Shopify Theme v3.0+ |

{% hint style="info" %}

**About CaaS PDX:** Apple's Catalog-as-a-Service Product Data eXchange (CaaS PDX) is the single source of truth for global Apple Premium Partner storefronts. It eliminates manual product entry, prevents copy/pricing mismatches, and ensures instant asset synchronization during NPI launches.
{% endhint %}

## 1. CaaS PDX Delivery Models (Which Version Do You Need?)

CaaS PDX supports two delivery mechanisms depending on your e-commerce platform and locale architecture:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Delivery Mechanism</th>
<th>Eligible Partners</th>
<th>How It Works</th>
<th>Best For</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Shopify API Direct Push</strong></td>
<td>Shopify Partners Only</td>
<td>CaaS PDX connects directly to your Shopify Admin via private app/OAuth API. Products, variants, metafields, and media are created/updated automatically.</td>
<td>Single-storefront or primary-market Shopify partners seeking 100% hands-off automated catalog updates.</td>
</tr>
<tr>
<td><strong>2. CaaS PDX Flat File (Email Link)</strong></td>
<td>CX-S Partners &amp; Multi-Locale Shopify</td>
<td>CaaS PDX generates a structured master table (CSV / XLSX / JSON / XML) and delivers an automated email with an authenticated, one-time secure download link.</td>
<td>• <strong>CX-S Partners:</strong> Custom engines (Magento, SAP, custom DB).<br />
• <strong>Multi-Locale Shopify Partners:</strong> Stores managing regional price books, local tax schemas, localized translation layers, or multi-market sub-stores.</td>
</tr>
</tbody>
</table>

## 2. Detailed Architecture & Onboarding Steps

### Option A: Shopify API Direct Push (Shopify Partners)

Follow these steps to establish automated real-time catalog syncing into your Shopify admin:

1.  **Generate Shopify Custom App Credentials:** In your Shopify Admin, create an APP Digital integration app with `write_products`, `write_inventory`, and `write_metafields` scopes.
2.  **Submit Credentials via Wrike:** Open a ticket in `Wrike Queue #APP-CAAS` with your store URL and encrypted API access token.
3.  **Metafield Mapping Confirmation:** APP Digital maps official Apple tech specs (Chip, Display, Camera, Battery) to standardized Theme metafield definitions (`app_digital.spec_*`).
4.  **Staging Delta Smoke Test:** We trigger a 5-SKU test batch on your staging theme to verify pricing tiers and image asset rendering before production activation.

### Option B: CaaS PDX Flat File via Email Download Link

Standard for custom platforms (CX-S) and multi-locale Shopify partners who ingest data via internal middleware or PIM systems:

1.  **Register Distribution Email Group:** Submit a dedicated distribution list (e.g. `ecom-catalog@partner.com`) to APP Digital via Wrike. *Do not use individual personal email inboxes.*
2.  **Delivery Schedule:** CaaS PDX emails automated download links at scheduled cadences:
    - **Regular Cadence:** Weekly refresh every Tuesday at 02:00 UTC.
    - **NPI Keynote Events:** Instant high-priority broadcast triggered at zero-hour embargo unlock.
3.  **Link Security & Expiration:** The download link is signed and valid for **24 hours**. If a link expires before your automated pipeline downloads it, trigger a re-delivery via the self-service webhook or Wrike.
4.  **Schema Parsing:** Ingest the master table using the standard CaaS PDX schema dictionary detailed below.

## 3. Multi-Locale & Multi-Market Guidance for Shopify Partners

{% hint style="info" %}

**Why Multi-Locale Shopify Partners Use Flat Files:** If your Shopify store operates across multiple languages, regions, or currencies (e.g. pan-European stores or APAC multi-country markets), direct API pushes can overwrite regional pricing or custom translations. By utilizing the **CaaS PDX Flat File**, your middleware or staging tool can parse region-specific columns (e.g., `Price_EUR`, `Title_FR`, `Tax_VAT_Rate`) before loading to each respective Shopify Market.
{% endhint %}

## 4. CaaS PDX Master Schema Data Dictionary (Core Fields)

| Field Column | Data Type | Example Value | Description |
|----|----|----|----|
| `apple_part_number` | String (Unique Key) | `MYW83LL/A` | Official Apple Global MPN |
| `product_family` | String | `iPhone 16 Pro` | Primary device family classification |
| `capacity_storage` | String | `256GB` | Normalized hardware capacity |
| `color_finish_code` | String | `NAT_TITANIUM` | Normalized finish code for UI swatch matching |
| `applecare_eligible_sku` | String (Nullable) | `S9824LL/A` | Linked AppleCare+ SKU for auto-bundling drawer |
| `embargo_status` | Enum | `PUBLIC | EMBARGOED` | Used during NPI launches to gate visibility |

## 5. Troubleshooting & Support Escalation

- **Missed / Expired Email Link:** Email `app-caas-pdx@apple.com` or ping in `#app-caas-ops` with your Partner ID.
- **Missing SKU or Price Discrepancy:** File a Sev-2 ticket in Wrike with the affected `apple_part_number` and expected vs actual values.

{% hint style="warning" %}
**Placeholder content.** This page follows the partners' draft of the Knowledge Wiki. All data (versions, dates, metrics, contacts) is an example to be replaced with real information.
{% endhint %}
