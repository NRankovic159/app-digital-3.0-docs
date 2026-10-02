# Integration Setup (Shopify API vs. Flat File)

{% hint style="info" %}
**Applies to:** Shopify / CX-S / Both — _(update per-topic if a page is Shopify-only or CX-S-only)_
{% endhint %}

## Integration Paths

{% tabs %}

{% tab title="Shopify API" icon="shopify" %}
Use the Shopify API path if your store is built on Shopify and you want real-time, automated syncing of product and catalog data.

**What you'll need:**
* A live Shopify store on a supported plan
* Admin API credentials (API key and access token) scoped for products, inventory, and orders
* A technical contact who can configure and maintain the integration

**Setup steps:**
1. Request API credentials through [Access & Account Provisioning](access-provisioning.md)
2. Configure the required API scopes for product, inventory, and order data
3. Connect your store in the APP Digital Program partner portal
4. Run a test sync and validate sample data against your catalog
5. Schedule your go-live sync with your APP Digital Program contact

**Best for:** partners who want automated, low-maintenance syncing and can support ongoing API credential management.
{% endtab %}

{% tab title="Flat File" icon="file" %}
Use the Flat File path if your catalog data lives outside Shopify, or if you prefer a scheduled batch-upload process instead of a live API connection.

**What you'll need:**
* Catalog data exportable in a supported file format (CSV)
* A defined delivery schedule (daily, weekly, etc.)
* A secure file transfer method (SFTP or equivalent), provided by the APP Digital Program team

**Setup steps:**
1. Request flat file specifications and a secure delivery endpoint through [Access & Account Provisioning](access-provisioning.md)
2. Map your catalog fields to the required flat file format
3. Submit a sample file for validation
4. Confirm your delivery schedule and automate the upload on your end
5. Monitor delivery confirmations after each scheduled upload

**Best for:** partners without a live Shopify API connection, or with more complex/legacy catalog systems.
{% endtab %}

{% endtabs %}

## Choosing the right path

| | Shopify API | Flat File |
|---|---|---|
| Data freshness | Real-time | Scheduled (batch) |
| Setup complexity | Moderate (API credentials, scopes) | Low-to-moderate (file mapping) |
| Best for | Native Shopify stores | Non-Shopify or legacy catalog systems |
| Ongoing maintenance | API credential upkeep | File delivery monitoring |

If you're unsure which path fits your setup, raise it with your APP Digital Program contact during the Due Diligence phase — see [Program Overview & Documentation Structure](program-overview.md) for where this fits in the program timeline.

## Common setup errors

{% hint style="warning" %}
**Missing or expired API credentials** — Shopify API connections fail silently if the access token has expired or scopes changed after setup. Re-issue credentials through [Access & Account Provisioning](access-provisioning.md) if syncs stop working.
{% endhint %}

{% hint style="warning" %}
**Flat file format mismatches** — the most common cause of failed flat file imports is a field mapping or encoding mismatch. Always validate against the sample file before your first scheduled delivery.
{% endhint %}

{% hint style="warning" %}
**Incomplete product data** — both paths reject records missing required fields. Review the [NPI Operations](/npi-operations) readiness checklists before your first sync to avoid last-minute rejections.
{% endhint %}

