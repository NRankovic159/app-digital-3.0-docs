# CaaS PDX Guidance

Integration guide for receiving official Apple product master data, localized technical specs, imagery and marketing copy through CaaS PDX (Product Data eXchange).

{% hint style="warning" %}
**Placeholder content.** The items below come from the partners' draft of the Knowledge Wiki. Replace them with real release data before publishing.
{% endhint %}

## About CaaS PDX

Apple's Catalog-as-a-Service Product Data eXchange (CaaS PDX) is the single source of truth for global Apple Premium Partner storefronts. It removes manual product entry, prevents copy and pricing mismatches, and keeps assets in sync during NPI launches.

## 1. Delivery models: which one do you need?

CaaS PDX supports two delivery mechanisms, depending on your e-commerce platform and locale architecture.

| | Shopify API Direct Push | CaaS PDX Flat File (email link) |
|---|---|---|
| **Eligible partners** | Shopify partners only | CX-S partners and multi-locale Shopify partners |
| **How it works** | CaaS PDX connects directly to your Shopify Admin through a private app / OAuth API. Products, variants, metafields and media are created and updated automatically. | CaaS PDX generates a structured master table (CSV / XLSX / JSON / XML) and emails an authenticated, one-time secure download link. |
| **Best for** | Single-storefront or primary-market Shopify partners who want fully hands-off catalog updates. | CX-S partners with custom engines (Magento, SAP, custom DB), and multi-locale Shopify partners with regional price books, tax schemas or translation layers. |

## 2. Onboarding steps

{% tabs %}

{% tab title="Option A: Shopify API Direct Push" %}
Follow these steps to set up automated real-time catalog syncing into your Shopify admin.

1. **Generate Shopify custom app credentials.** In your Shopify Admin, create an APP Digital integration app with the `write_products`, `write_inventory` and `write_metafields` scopes.
2. **Submit credentials through Wrike.** Open a ticket in Wrike Queue `#APP-CAAS` with your store URL and encrypted API access token.
3. **Confirm the metafield mapping.** APP Digital maps official Apple tech specs (chip, display, camera, battery) to standardized theme metafield definitions (`app_digital.spec_*`).
4. **Run the staging delta smoke test.** We trigger a 5-SKU test batch on your staging theme to verify pricing tiers and image rendering before production activation.
{% endtab %}

{% tab title="Option B: Flat File via Email Link" %}
Standard for custom platforms (CX-S) and multi-locale Shopify partners who ingest data through internal middleware or PIM systems.

1. **Register a distribution email group.** Submit a dedicated distribution list (for example `ecom-catalog@partner.com`) to APP Digital through Wrike. Do not use individual personal inboxes.
2. **Know the delivery schedule.**
   * **Regular cadence:** weekly refresh every Tuesday at 02:00 UTC.
   * **NPI keynote events:** an instant high-priority broadcast at zero-hour embargo unlock.
3. **Mind the link security and expiry.** The download link is signed and valid for **24 hours**. If it expires before your pipeline downloads it, trigger a re-delivery with the self-service webhook or through Wrike.
4. **Parse the file.** Ingest the master table using the standard CaaS PDX schema in section 4.
{% endtab %}

{% endtabs %}

## 3. Multi-locale and multi-market guidance for Shopify partners

If your Shopify store runs across several languages, regions or currencies (for example pan-European or APAC multi-country markets), a direct API push can overwrite regional pricing or custom translations. With the CaaS PDX flat file, your middleware or staging tool can parse region-specific columns (for example `Price_EUR`, `Title_FR`, `Tax_VAT_Rate`) before loading them into each Shopify Market.

## 4. Master schema data dictionary (core fields)

| Field column | Data type | Example value | Description |
|---|---|---|---|
| `apple_part_number` | String (unique key) | `MYW83LL/A` | Official Apple global MPN |
| `product_family` | String | `iPhone 16 Pro` | Primary device family classification |
| `capacity_storage` | String | `256GB` | Normalized hardware capacity |
| `color_finish_code` | String | `NAT_TITANIUM` | Normalized finish code for UI swatch matching |
| `applecare_eligible_sku` | String (nullable) | `S9824LL/A` | Linked AppleCare+ SKU for the auto-bundling drawer |
| `embargo_status` | Enum | `PUBLIC` \| `EMBARGOED` | Gates visibility during NPI launches |

## 5. Troubleshooting and support escalation

* **Missed or expired email link:** email `app-caas-pdx@apple.com` or post in `#app-caas-ops` with your Partner ID.
* **Missing SKU or price discrepancy:** file a Sev-2 ticket in Wrike with the affected `apple_part_number` and the expected vs actual values.

See also [Integration Setup (Shopify API vs. Flat File)](integration-setup.md).
