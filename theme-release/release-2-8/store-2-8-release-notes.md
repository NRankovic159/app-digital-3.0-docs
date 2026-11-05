# Store 2.8 Release Notes

{% file src="../../.gitbook/assets/Store-2.8-Release-Notes.pdf" %}
Store 2.8 Release Notes
{% endfile %}

## Overview

The Store 2.8 Release comprises the following new features, general updates and upgrades, accessibility improvements, and defect resolutions. This document is the single reference for what changed in 2.8, how it was verified, and what partners need to do to adopt it.

## Release at a Glance

| Area | Summary |
|---|---|
| Target release | October 2026 |
| New features | 11 new features across PDP, Cart and Checkout, Homepage, Navigation, merchandising and SEO |
| General updates & upgrades | Analytics tracking, SMB video placement, PDP 2.0 performance, UX consistency fixes, and data and automation |
| Accessibility | 58 accessibility tickets resolved (keyboard navigation, screen-reader support and color contrast), including the OSAPS violations first released in the 2.7.4 patch |
| Defect fixes | 30 defects from previous versions resolved |
| Product classification | 13 LOB / Sub LOB rule mismatches corrected |
| AI-assisted quality work | 20 rounds of AI-powered code analysis driving more than 1,400 fixes before release (separate from the defect fixes above) |

## Release Packages

Release 2.8 is delivered in two formats.

| Package | Description | Upload |
|---|---|---|
| Comprehensive Theme Release | A zip file uploaded to the Shopify Theme library. Suitable for new APPs, or any partner who wants to adopt the full release. | Theme release (comprehensive) |
| Theme Patch | A diff patch file highlighting theme code changes between the previous and current release (for example 2.7 to 2.8). Suitable for partners already on a recent 2.x version. | Theme patch (incremental) |

{% hint style="warning" %}
To be confirmed before publishing: the source release-packaging document still contains unfilled placeholders for the version range covered by each package, the eligible partner groups, and the versions documented. These must be completed by the release owner.
{% endhint %}

## Major Features

### AppleCare+ Theft & Loss: Paid Upfront Option (PDP 1.0 and PDP 2.0)

A dedicated second add-on slot lets customers choose between standard AppleCare+ and AppleCare+ with Theft & Loss (T&L) on the PDP.

- Selection is strictly opt-in, and T&L is never added automatically.
- The two options are mutually exclusive. Selecting one removes the other, and the displayed price updates immediately.
- The hero product and the T&L add-on are added as separate line items. In the cart and side sheet, T&L is shown as a sub-item, and removing the hero product also removes its T&L add-on.
- Active Acceptance is a required step in the buy flow for the Paid Upfront Option.
- Content is managed with Shopify metaobjects and metafields, assigned at product or collection level (product level takes priority). Separate B2B (SMB) content can be configured.

### BOPIS Pre-selected Based on Store Locator

The pickup location a customer chooses on the storefront now carries through to checkout automatically, instead of defaulting to the nearest store. This reduces store mismatches at checkout.

- The store chosen on the storefront (for example on the PDP) is the store pre-selected on the checkout page.
- Applies to the customer’s first path to checkout only, not to every navigational instance.

### Checkout Button Fallback for Non-Safari Browsers

Apple Pay renders only on browsers that support the Apple Pay API, so Chrome, Firefox and other browsers previously showed no express checkout option.

- A Checkout express button is now shown on the Cart page and PDP when the Apple Pay API is unavailable.
- The button goes directly to Shopify checkout (`/checkout`) and uses the same slot and visual size as the Apple Pay button.
- On Safari, Apple Pay is unchanged and the fallback is suppressed.

### View Cart CTA on Checkout

A labelled “‹ Return to cart” link now appears inside the checkout header, below the logo, on every checkout step (delivery, shipping method, payment), on desktop and mobile. It gives customers a clear way back to the cart instead of relying on the small, unlabelled cart icon, which is unchanged.

It is implemented as a Shopify Checkout extension, which can be easily enabled or disabled in the checkout profile settings.

### Pre-sale Status

A collection-level setting that stops a product from being sold before its official availability date. It is built for late-wave and price-restricted NPI partners, who no longer need to hide prices manually.

- How it is enabled: through a metafield on the product’s Smart collection. Product tags do not enable it.
- What customers see: price and Add to Cart are hidden for pre-sale products. In-store pickup shows “Pickup unavailable” for every store.
- Where it applies: PDP 1.0 and 2.0, Family Stripe, bundles, Frequently Bought Together, LOB Dynamic Banner and Sub-LOB modules, the AI product carousel, Dynamic Product Prioritization, the Side Drawer and the Cart. Pre-sale products cannot be added to the cart, including as a free or discounted product.
- Notify Me (optional): can additionally be enabled for pre-sale products. It uses the same Notify Me functionality as out-of-stock products, so customers can enter an email address in a modal to be notified when the product becomes available. It is not required for Pre-sale Status to work.
- Notify Me settings: modal heading, success message and error text are configurable and translatable in Theme Settings → Back in Stock Notify.

### Homepage Video Banner

Admins can use video, not only static images, in the homepage banner, which is useful for NPI and other launches.

- Carousel video banner: a dedicated section that can replace the original banner in the theme editor.
- Video slide in the Carousel banner: a Video slide can now also be added to the existing Carousel banner section, alongside the Image slides.

### Second Image on Hover (PLP)

When the Show second image on hover setting is on, product cards crossfade from the first to the second product image on mouse hover.

- Works on grid-layout PLPs (for example Accessories PLPs) and on the Search Results page.
- Requires at least 2 images per product. Single-image products behave as before.
- Desktop hover only. Touch devices always show the first image.

### Auto-tag Accessories from PDX into PLP

New accessory products are automatically tagged and routed to the correct PLPs when they land from PDX. This removes manual tagging and keeps accessory collections consistent.

- Built with Shopify Flow: the “Auto-tag Accessories After Data Push” workflow tags new products whose Product Type is Accessories, based on keywords in the Primary Display metafield.
- Requires the APP to set up the tagging rules in Shopify Flow. A partner guide is provided.
- Products reach a PLP only through Smart Collections that have a rule matching the tag.

### Dynamic Content: Specific Product Prioritization

A collection-level setting that lets partners manually promote a specific in-stock product, such as a newly released pre-order color, instead of the default lowest-price pick.

- How it is set: the partner selects the priority product in the collection’s Dynamic Product Prioritization metafield.
- What it drives: the image, CTA destination and displayed price in the Partner Stripe, BentoBox, LOB Dynamic Banner, LOB Module and PLP Module.
- Fallback: if the selected product goes out of stock, the display falls back to the lowest-priced in-stock product in the collection. If the first prioritized product is out of stock, the availability of the next one is evaluated.
- Not available for Accessories collections, which are not grouped into a base collection.

### Breadcrumbs for Navigation

Breadcrumbs now support both wayfinding and SEO, and appear on the Homepage, LOB pages, PLPs, PDPs, and Apple-defined landing pages such as AppleCare+.

- The first level is the homepage, labelled “APP” or shown as a home icon (the Apple logo is not used).
- All items except the current page are links, and the current page is plain text.
- Breadcrumbs are accompanied by schema.org BreadcrumbList JSON-LD that matches the visible trail.
- Powered by Shopify’s native breadcrumb capability. Not every page type builds a full hierarchy automatically, and the content-page gap and its trade-offs are covered in the breadcrumb guide.

### Heading Tag & Structured Data Cleanup (H1 + H2)

A partner’s SEO agency identified heading and schema issues. All were resolved in 2.8, which also improves screen-reader navigation.

| # | Fix | Scope |
|---|---|---|
| 1 | Empty `<h2>` tags removed | Sitewide |
| 2 | “Your basket is empty” no longer rendered as an `<h2>` | Cart |
| 3 | H1 added to the logo with a descriptive aria-label | Homepage |
| 4 | Category and stripe titles promoted to `<h2>` | Homepage |
| 5 | Product category names promoted to `<h2>` | PLP |
| 6 | Duplicate H1 removed (single H1 per page) | PDP |
| 7 | Duplicate H1 removed (single H1 per page) | Cart |
| 8 | Stripe and section titles promoted from `<div>` to `<h2>` | Home / LOB / PLP |
| 9 | Organisation schema retained on the homepage only | Sitewide |
| 10 | ItemList schema.org markup added | All PLPs |

## General Updates & Upgrades

### Analytics & Tracking

All additions are additive and do not change existing search, autocomplete or results tracking.

<table>
<thead>
<tr><th>Event</th><th>Where it fires</th><th>How to trigger / reproduce</th><th>Key values</th></tr>
</thead>
<tbody>
<tr><td>Hamburger menu open (mobile)</td><td>Global (Header)</td><td>On mobile viewport (≤768px), tap the ☰ icon when menu is closed (<code>aria-expanded="false"</code>).</td><td><ul><li>event_action:hamburger_menu_open</li><li>category:navigation</li><li>event_location:Header</li><li>Adobe Analytics:event61</li></ul></td></tr>
<tr><td>Hamburger menu close (mobile)</td><td>Global (Header)</td><td>Tap the (X) or ☰ icon a second time while menu is already open (<code>aria-expanded="true"</code>).</td><td><ul><li>event_action:hamburger_menu_close</li><li>category:navigation</li><li>event_location:Header</li><li>Adobe Analytics:event61</li></ul></td></tr>
<tr><td>Search bar initiation</td><td>Global (Header / Search modal)</td><td>Click or focus the search input (<code>input[name="q"]</code>) or click search icon. Fires once per page load.</td><td><ul><li>event_action:search_initiate</li><li>category:engagement</li><li>event_location:Search Bar</li><li>Adobe Analytics:event61</li></ul></td></tr>
<tr><td>Pre-Sale: Collections Button</td><td>Collection / PLP</td><td>Click "Notify Me" button on an out-of-stock product card or image-with-text promo block.</td><td><ul><li>event_action:Notify Me Button Click</li><li>category:marketing</li><li>Adobe Analytics:event61</li></ul></td></tr>
<tr><td>Pre-Sale: PDP Sticky Footer</td><td>PDP (Out-of-stock items)</td><td>Scroll down an out-of-stock product page until sticky bar appears, then click "Notify me".</td><td><ul><li>event_action:Notify Me Click</li><li>event_label:Notify me when it's available</li><li>category:marketing</li><li>Adobe Analytics:event61</li></ul></td></tr>
<tr><td>Pre-Sale: Modal Email Input</td><td>Notify Me Modal</td><td>Click or focus into the email input field (<code>.js-notify-input</code>). Fires once per modal open.</td><td><ul><li>event_action:Notify Me Input Click</li><li>category:marketing</li><li>Adobe Analytics:event61</li></ul></td></tr>
<tr><td>Pre-Sale: Modal Submit &amp; Close</td><td>Notify Me Modal</td><td>Submit the email form (<code>.js-notify-submit</code>) or close modal via (X) button (<code>.modal-close-button</code>).</td><td><ul><li>event_action:Notify Me Submit / Notify Me Modal Close</li><li>category:marketing</li><li>Adobe Analytics:event61</li></ul></td></tr>
<tr><td>Breadcrumbs navigation</td><td>PDP / PLP / Category pages</td><td>Click on any parent category link or current item inside the breadcrumbs bar (<code>.breadcrumbs__item a</code>).</td><td><ul><li>event_action:breadcrumbs</li><li>category:navigation</li><li>Adobe Analytics:event61</li></ul></td></tr>
<tr><td>AppleCare+ &amp; Protection Plans</td><td>PDP 1.0, PDP 2.0 &amp; Attach Sidebar</td><td>Select coverage plan radio/label (<code>#theftloss-add</code>, <code>label[for="add-theftloss"]</code>, <code>#secWarranty-add</code>, or confirm T&amp;L modal).</td><td><ul><li>Metric added:apple_care+_type (AppleCare+, AppleCare+ with Theft and Loss, Partner Protection Plan, No coverage)</li><li>Value fixed:Renamed legacy Third-Party Warranty to Partner Protection Plan</li></ul></td></tr>
<tr><td>Landing Page CTAs</td><td>Business / Service landing pages</td><td>Click action buttons: Schedule Appointment (<code>.business-hero-billboard__button</code>), Banner CTA (<code>.business-banner__link a</code>), or Repair Prices (<code>.rich-text__buttons a</code>).</td><td><ul><li>event_action:cta_click</li><li>event_location:Business Hero Billboard, Business Banner, Rich Text Section</li><li>Adobe Analytics:event61</li></ul></td></tr>
<tr><td>Landing Page Category Tiles</td><td>Service / Business landing pages (e.g. Repair, Support)</td><td>In the device selection grid (<code>.featured-blocks-grid</code>), click any category tile card (<code>a.featured-blocks-grid__card</code>).</td><td><ul><li>event_action:category_tile_click</li><li>category:navigation</li><li>event_location:Featured Blocks Grid: &lt;heading&gt;</li><li>event_label:&lt;Card Title&gt; (e.g. iPhone, iPad)</li><li>Adobe Analytics:event61</li></ul></td></tr>
<tr><td>PDP Attach Sidebar: Special Offers (GWP)</td><td>Slide-out Attach Sidebar (PDP 2.0)</td><td>Add item to cart to open sidebar. In <code>.cto-gwp-item</code> block: click Title, click Add, click Remove, or click Learn More.</td><td><ul><li>event_action:Special Offer &gt; Title click / Add / Remove / Learn More &gt; &lt;product&gt;</li><li>event_location:pdp_cart_preview</li><li>Adobe Analytics:event61</li></ul></td></tr>
<tr><td>PDP Attach Sidebar: Cross-Sell Carousel</td><td>Slide-out Attach Sidebar (PDP 2.0)</td><td>Add item to cart to open sidebar. In carousel (<code>.cto-drawer-carousel</code>), click product card or navigation arrows.</td><td><ul><li>event_action:cart_slide_click / slider_arrow_click</li><li>event_location:Attach Section: &lt;heading&gt;</li><li>category:navigation / engagements</li><li>Adobe Analytics:event61</li></ul></td></tr>
<tr><td>PDP Attach Sidebar: Continue Shopping</td><td>Slide-out Attach Sidebar (PDP 2.0)</td><td>Click "Continue Shopping" link in the sidebar header (<code>.continue_link--cto</code>).</td><td><ul><li>event_action:Return to Main Page</li><li>event_label:Continue Shopping</li><li>event_location:pdp_cart_preview</li><li>Adobe Analytics:event61</li></ul></td></tr>
</tbody>
</table>

**Reporting impact:**

- Warranty & Protection Plans: The legacy PDP 1.0 label "Third-Party Warranty" has been renamed to "Partner Protection Plan" to match the UI; historical reports comparing periods across this release will show a split between these two values. Additionally, the new apple_care+_type dimension is only available from this release onward and will appear as unspecified in historical data.
- New additive tracking: Breadcrumbs, Pre-Sale ("Notify Me" flow), and PDP Attach Sidebar interactions are entirely additive under event61: Clicks. Any trend or period-over-period comparisons for these touchpoints will have no historical baseline prior to this deployment.

### Performance: PDP 2.0 Page Size and Total Blocking Time

Measured with Lighthouse on PDP 2.0, average of 5 runs per phase on each device. Test conditions: theme 2.8, logged-out user, non-bundle product, incognito browser, staging URL. Only PDP 2.0 was in scope for this release. Homepage and PLP optimizations are not included.

| Metric | Desktop before | Desktop after | Mobile before | Mobile after |
|---|---|---|---|---|
| Performance score | 83.2 | 89.2 | 60.8 | 61.6 |
| First Contentful Paint | 1.08 s | 1.00 s | 3.04 s | 2.94 s |
| Largest Contentful Paint | 2.08 s | 1.48 s | 7.48 s | 8.08 s |
| Total Blocking Time | 0 ms | 0 ms | 192 ms | 216 ms |
| Cumulative Layout Shift | 0.0036 | 0.0252 | 0 | 0 |
| Speed Index | 2.36 s | 2.06 s | 7.60 s | 7.06 s |

- Desktop: performance score up 7.2%, LCP down 28.8% and Speed Index down 12.7%. CLS rose but stays within the “Good” threshold (0.1 or less), though one run reached 0.097 and should be monitored.
- Mobile: results are mixed. The score, FCP and Speed Index improved slightly, but LCP rose 8% and TBT rose 12.5%. TBT of 216 ms is above the 200 ms “Good” threshold, and mobile LCP varied widely between runs (5.2 s to 10.3 s). Mobile performance remains in the “Needs Improvement” band and is a candidate for further optimization.

### UX Consistency Fixes

- Sticky footer on Safari (mobile): the Apple Pay button was hidden while scrolling on Safari for iOS, while Chrome and Firefox kept the Checkout and Add to Cart buttons visible. The footer height now uses dvh / svh viewport units (with a fallback), so both buttons stay visible on every browser. Apple Pay logic is unchanged.
- Pickup / Ships message alignment: the Cart page icon and text are vertically aligned, the PDP 1.0 Pickup icon is sized to the text line height, and on PDP 2.0 the text is aligned and the Pickup time shows inline.

### Data & Automation

- Product classification rules: 13 LOB / Sub LOB mismatches in the Product String Classification Rules were fixed, spanning iPhone, Watch, iPad, Accessories, Beats and Mac. They include new rules for iPhone Air, Apple Pencil and MacBook Neo, and corrections for Apple Watch Ultra/Series/SE, Watch bands, Smart Folio, Magic Keyboard for iPad, MagSafe Charger, EarPods and generic cables and adapters.

### SMB Video Placement

A new Video block in the Rich Text section of the Business page template plays a video inline beneath the heading and description text on desktop and mobile.

- Shopify upload limits apply: maximum 0.97 GB and 10 minutes.
- If an upload fails without an error message, the store’s Shopify video limit has been reached. Delete unused videos in Files, or contact Shopify Support.

## Accessibility Proof of Work

We are making sure features meet the W3C Web Content Accessibility Guidelines (WCAG) 2.2 Level A/AA and the internal corporate standard.

- 58 accessibility tickets resolved in 2.8, covering keyboard-only navigation, screen-reader support and color contrast. The full list is in the Accessibility Ticket List appendix.
- Includes the OSAPS accessibility violations identified and first released in the 2.7.4 patch.
- Newly released 2.8 features were confirmed to have no violations against WCAG 2.2 AA and the internal standard.

### Verification Approach

| Disability group | Coverage |
|---|---|
| Visual (blindness, low vision, color blindness) | Screen readers (NVDA, JAWS, VoiceOver), high contrast mode, browser zoom up to 200%, color contrast analyzers |
| Motor / physical (limited mobility, tremors, paralysis) | Keyboard-only navigation, switch access, touch target size checks |
| Cognitive (dyslexia, ADHD, memory impairments, learning disabilities) | Consistent navigation review, error message clarity, timeout warnings |
| Auditory (deafness, hard of hearing) | Out of scope, as the product has no first-party video or audio (video content is third-party) |

### What Was Fixed

**Screen reader clarity**

- Dozens of buttons and links (Add, Added, Out of Stock, Start trade-in, Learn more, Save 10% bundle, VAT info, Energy Label, Explore financing, Plan A/B/C, Cart’s Done / Continue shopping) are now announced correctly as buttons or links with clear names.
- “Protect your product” and AppleCare+ plan options now behave as proper checkboxes and radio buttons, and the “checked” state that was misannounced on mobile is corrected.
- Content that was invisible to screen readers is now accessible: the Theft and Loss modal, the My Store modal, the “Prepare for your repair” section, and the Filter modal’s close button and text across Apple Services pages (TV, One, Music, Arcade, Fitness+, News+).
- “Item added to your cart” is rebuilt as a proper pop-up dialog, the AppleCare+ Theft/Loss modals have clear names, and the “Length” field in the Financing modal is connected to its label.
- Heading structure is cleaned up sitewide. Each page starts with one main heading, duplicate and triple headings are removed (Home, Support, Repair & Service, View All Mac/iPad), and several visual section titles are now proper headings.
- Decorative images, leftover invisible headings, and the “Previous slide” / “Next slide” buttons on mobile that confused screen reader users are hidden.
- Status messages (“item added to cart” and selected bundle, financing and trade-in options) are now announced when they appear.

**Keyboard navigation**

- Buttons and links sitewide (Learn more, Energy Label, Compare models, store map, business financing link, mobile Quick checkout carousel and similar) work with the keyboard, not only the mouse.
- Keyboard dead ends and focus traps are fixed in the mobile filter menu, the business financing modal, and after adding items to the cart.
- Focus order is correct after adding to cart, after closing the cart, store and financing modals, and when moving into the footer.
- Cart Remove and Add buttons work with the keyboard.

**Visual clarity**

- Clearly visible, high-contrast focus outlines on radio buttons (Color, Processor, Memory, Storage, AppleCare+, Trade-in, Financing), the Add button inside AppleCare+, mobile menu items and search suggestions.
- Better color contrast on error messages, and persistent underlines on text links so they are not identified by color alone.

**Motion and media**

- New settings stop auto-playing animations on the Home page after 5 seconds.
- Repeated slide announcements no longer interrupt screen reader users.

## AI-Assisted Work: Store Briefing, Defects and Hardening Scans

2.8 is the first theme version where AI was part of how the theme was built, not just what was built.

{% hint style="info" %}
Not part of the defect fixes in this document. The fixes described here were found by AI-assisted scanning during development. They are not defects from previous versions and were not reported by partners.
{% endhint %}

| Measure | Result |
|---|---|
| AI-powered code analysis | 20 rounds before release, clearing defects highest-severity first |
| Fixes driven | More than 1,400 |
| Regression sweeps | 8 dedicated sweeps to protect existing functionality |
| Where fixes concentrate | Highest-traffic journeys: cart, product configuration and search. Strong emphasis on cross-browser consistency, notably Safari |

### How AI Was Used

- AI-assisted bug and code review: AI and human reviewers examine every change from different angles, working through defects highest-severity first. Dedicated reviewers then try to disprove what was found, repeating until nothing new turns up.
- AI-driven code optimization: AI identifies opportunities to simplify, clean up or remove redundant code as part of the build, keeping the codebase leaner with every release.
- Automated quality gates: every change is checked for security, performance, accessibility and design consistency before it ships. Nothing is considered done until every applicable check passes or is explained.

## Defect Fixes

This section lists defects from previous versions that were resolved in 2.8. Each fix was tested and verified against the expected result. The 30 items below are grouped by area, and numbering follows the engineering tracker.

### Cart & Side Drawer (8)

| # | Area / Component | Issue | Resolution |
|---|---|---|---|
| 2 | Cart | The price is displayed as 0 for the free product if it was added as a Hero product when over the quantity limit | The correct price is now displayed for free products added as a Hero product when the quantity limit is exceeded. |
| 3 | Cart | Nothing happens when exceeding max quantity in cart if AppleCare is added to a bundle | A notification now appears when the maximum allowed quantity is exceeded, the cart and total price update accordingly, and the user can remove AppleCare from the cart. |
| 4 | Cart | Pickup message only considers main product availability, ignores Free/Discounted product availability | ‘Pickup unavailable’ is now correctly displayed when a Free/Discounted product is not available at the selected store. |
| 5 | Cart | Unable to add AppleCare to any cart product when max quantity notification is displayed | Users can now add AppleCare to any cart product even when a maximum quantity notification is being shown. |
| 6 | Cart | VAT link does not work after adding a discounted product | The VAT pop-up now opens correctly after a discounted product is added to the cart. |
| 7 | Cart / Side Drawer | Protection Plan added to Bundle product leaves only Hero product in the cart | Adding a Protection Plan to a Bundle product no longer removes the Bundle. All bundle items remain in the cart. |
| 25 | Side Drawer | Free/offered product stuck in cart if user navigates to the cart page during add action | The free product is now correctly added to the cart and can be managed or removed normally. |
| 26 | Side Drawer | If Free/Discounted product added to cart automatically, the count of added products changes incorrectly when AC+ is added | The quantity of each added product item (Hero, AppleCare) now correctly reflects 2 when two items are present. |

### BOPIS & Pickup (10)

| # | Area / Component | Issue | Resolution |
|---|---|---|---|
| 9 | BOPIS | Does not work when ‘Use my current location’ is clicked with location access disabled | The system no longer fails or hangs when location access is denied. Users can continue using the site normally. |
| 10 | BOPIS | Information inconsistency for Bundles (Hero, Hero+Bundle on PDP/Cart/Checkout show different pickup times) | Pickup information is now consistent across the Hero component, Hero+Bundle on PDP, Cart, and Checkout. |
| 11 | BOPIS | Selected store cannot be changed on other pages after switching store on Checkout | The selected pickup store is now correctly persisted and changeable across all pages. |
| 12 | BOPIS | Currency changes when switching between available stores on Checkout page | Switching the pickup store on the Checkout page no longer affects the displayed price currency. |
| 13 | BOPIS | Nearest available store is displayed for bundles on Checkout page instead of the selected one | The previously selected store is now pre-selected and displayed correctly for bundles on the Checkout page, with radio button selection available. |
| 14 | BOPIS | Checkout page: Distance to selected store always displays as 0 mi | The actual distance to the selected store is now correctly calculated and displayed. |
| 15 | BOPIS | Checkout: Incorrect pickup store displayed as selected | The correct previously selected store is now shown as selected on the Checkout page. |
| 16 | BOPIS – BTB | Pickup is not available for some products | Fixed. Pickup is now available for the affected products. |
| 17 | BOPIS | Checkout: Incorrect pickup time displayed | Pickup time is now correctly displayed on the Checkout page (e.g. Bundle pickup time shows 3-4 weeks). |
| 34 | PDP 1.0 | Incorrect pickup message displayed if AppleCare is added to the cart (shows ‘24 hours’ instead of ‘1 day’) | The pickup message now correctly shows ‘1 day’ when AppleCare is added to the cart. |

### Header, Navigation & Search (6)

| # | Area / Component | Issue | Resolution |
|---|---|---|---|
| 18 | Header | Language Switcher is absent in the Header | The Language Switcher is now present in the Header with the ability to change language options. |
| 19 | My Store | Select another Store CTA: Header with My Store popup are not faded out when Side Drawer is opened | The Header menu and My Store pop-up are now correctly faded out (inactive) when the Side Drawer is opened. |
| 20 | Mobile / Header | Header is displayed on Filter popup | The Header is no longer displayed on the Filter popup. Fixed. |
| 21 | Bug – Lab9 (Navigation) | Persistent Menu Dropdown in Safari and Chrome — dropdown stays visible after clicking outside | The dropdown now correctly closes when the user clicks elsewhere on the page. |
| 22 | B2B – Search Results | Product card alignment issue: ‘Shop’ button and badge are misaligned between cards in the same row | All product cards in the same row are now vertically aligned. Key elements (badge, ‘Shop’ button) are consistently positioned regardless of content length. |
| 23 | Search Suggestions | No visible scroll bar or indicator in the scrollable Product section of the search suggestions dropdown | The entire product list in the search suggestions dropdown is now scrollable with a visible scroll indicator. |

### CTO (Configure-to-Order) (1)

| # | Area / Component | Issue | Resolution |
|---|---|---|---|
| 1 | CTO | Selected values in Financing sections are not reset after changing options in Advanced Customization section | When options change in the Advanced Customization section, the AppleCare, Trade-in, and Financing section values are now properly reset so the user can re-select them. |

### PDP 1.0 / PDP 2.0 & AppleCare+ (3)

| # | Area / Component | Issue | Resolution |
|---|---|---|---|
| 28 | PDP 1.0 | Free/Discounted product is displayed in Additional Services section instead of Additional Offers | Free/Discounted products are now correctly displayed in the Additional Offers section. |
| 29 | Additional Offers | ‘Additional offers’ label displayed for each individual product item instead of once as a common label | The ‘Additional offers’ label is now displayed once as a common label for all offered products. |
| 35 | PDP 2.0 | Incorrect styles applied to the Monthly Pricing link after closing the Financing popup | The correct styles are now applied to the Monthly Pricing link after the Financing popup is closed. |

### Merchandising, Content & Localization (2)

| # | Area / Component | Issue | Resolution |
|---|---|---|---|
| 51 | Bug – Epos Austria | Store Locator: wrong decimal separator for German (shows ‘0.2 km’ instead of ‘0,2 km’); ‘Get Directions’ string cannot be translated | Decimal separator now correctly uses a comma for German (e.g. ‘0,2 km’). The ‘Get Directions’ string is now available in theme content settings for translation (e.g. ‘Route berechnen’). |
| 55 | Marketing Page | Broken UI elements and missing images on the marketing page | Resolved. The page was using the wrong template; the correct template has been applied and the page now displays correctly. |

### Additional Fixes Documented in Feature Guides

These fixes are described in detail in their own guides and are not part of the 30 numbered items above.

| Area | Fix |
|---|---|
| Sticky footer (mobile, Safari) | Apple Pay button no longer hidden while scrolling. Behavior is now consistent with Chrome and Firefox. |
| Cart, Pickup / Ships message | Ships text and icon vertically aligned |
| PDP 1.0, Pickup / Ships message | Pickup icon size corrected to match text line height |
| PDP 2.0, Pickup / Ships message | Text aligned with icon, and Pickup time displayed inline |
| Product classification | 13 LOB / Sub LOB rule mismatches corrected |

## Notes for Partners

- Plan the upgrade. Estimated effort to implement the theme is 4+ weeks in total: about 2 weeks for the code upgrade and about 2 weeks for content and testing.
- Pre-sale is collection-driven. Pre-sale Status is enabled through a metafield on the Smart collection, not through product tags. To verify, toggle it on and off, then check PDP, Family Stripe, Bundle, FBT, LOB page and Cart.
- Smart Collections only. Auto-tag Accessories assigns products to collections only when those are Smart Collections with a rule matching the tag.
- Dynamic Product Prioritization is not available for Accessories collections.
- Regional guidance. Defer to local Marcom / PCM guidance where regional instructions differ.

## Appendix: Accessibility Ticket List

All 58 accessibility tickets resolved in 2.8. Ticket references are internal Wrike IDs, and titles are shown as originally filed (WCAG success criterion, conformance level and area).

| # | Ticket ref | Ticket (as filed) |
|---|---|---|
| 1 | 4491165270 | [AA+][Structure][Support] Two H1 are present on Customer Support page |
| 2 | 4486170432 | [1.3.2][A][Stores][mobile]The content in the “My store” dialog is not screen reader accessible |
| 3 | 4486181499 | [1.4.3][AA][Store dialog] Contrast ratio is failed for “Please fill this out” message |
| 4 | 4470070820 | [AA+][Visual indicators][Repair and Service] “Specialist” and Phone number inline links are not persistently underline |
| 5 | 4470110775 | [1.1.1][A][Repair and Service] Decorative images inside “We repair all devices” section are not hidden |
| 6 | 4470162395 | [1.3.1][A][Repair and Services] Visual headings inside “Authorized Apple Solutions” section are not implemented as one |
| 7 | 4469826486 | [2.1.1, 1.3.2][A][Repair and Services] The list inside “Prepare for your repair” section is not keyboard accessible when navigating by screen reader |
| 8 | 4465834155 | [2.2.2][A][Home] Animation inside carousel can not be paused or stopped |
| 9 | 4467380493 | [4.1.2][A][PDP] “Protect your product” elements are not implemented as checkboxes |
| 10 | 4466909938 | [1.3.2][A][PDP] The content of the “Theft and Loss modal” modal is not screen reader accessible |
| 11 | 1799103074 | [2.5.3][A][Product bundle] Chosen bundle name is not announced as part of ‘Bundle’ summary accessible name |
| 12 | 4469556228 | [2.1.1][A][Your Cart] “Remove” and “Add” buttons for AC+ and Partner Protection Plan are disabled when navigating by keyboard |
| 13 | 4471953027 | [4.1.2][A][PDP] “Learn more about…” elements do not have an accessible name and role |
| 14 | 4472085348 | [4.1.2][A][PDP] “AppleCare+ with Theft and Loss” modal has incorrect accessible name |
| 15 | 4399754362 | [2.2.2][A][Business Home] Animation can not be paused or stopped |
| 16 | 4390456043 | [2.1.1][A][Product]“Learn more” button can not be activated by keyboard |
| 17 | 4389443579 | [4.1.2][AA][Product] “Add” and “Added” buttons have incorrect role and non-descriptive accessible name |
| 18 | 4373329479 | [2.4.7][AA] [Product] The “Add” button does not have a visible focus indicator |
| 19 | 4471941895 | [4.1.2][A][PDP] “Learn more” elements does not have an accessible role |
| 20 | 4375847416 | [2.1.2][A][Search results][Mobile] Screen reader focus is trapped after checking/unchecking checkboxes in the “Filter” modal dialog |
| 21 | 4375796777 | [1.3.1][A][Search results][Mobile] Hidden heading receives screen reader focus, the “Filter by” heading is not semantically marked at the appropriate level |
| 22 | 4374302373 | [1.3.2][A][Apple Services] The text in the “Apple TV features” section is not screen reader accessible |
| 23 | 4374269920 | [1.3.1][A][Apple Services] Headings are not semantically marked as such |
| 24 | 4372332038 | [2.1.1][A][PLP] The “B” Energy Label button is not keyboard operable |
| 25 | 4465884655 | [4.1.2][A]Product] “Out of Stock” element has incorrect role and does not not have a “disabled” state |
| 26 | 1801642895 | [4.1.3][AA][Cart side bar] Status message after adding a product in the “Your cart” modal dialog is not announced by screen reader |
| 27 | 1707833410 | [1.4.11] [AA] [Mobile] Low contrast on the focused option in the search suggestion list |
| 28 | 1707904707 | [4.1.2, 2.4.3][A][Cart] ‘Item added to your cart’ modal is not implemented as dialog |
| 29 | 1801632362 | [2.4.3][A][Cart side bar] Incorrect focus order after adding a product in the “Your cart” modal dialog |
| 30 | 1801624220 | [2.1.1][A][Cart side bar] The “Learn more” button is not keyboard operable |
| 31 | 1801574969 | [1.4.3][AA][Business account] The contrast ratio is failed for the text of the “Create business account” button in focus state |
| 32 | 1801546304 | [2.4.7][AA][Product] Radio button option for “Color” section does not have a visible focus indicator |
| 33 | 1801522875 | [2.1.1, 4.1.2][A][Product] AppleCare+ options are not implemented as radio button and do not receive a keyboard focus |
| 34 | 1800050417 | [2.4.3][A][Cart side bar] Incorrect focus order when the ‘Your cart’ modal dialog is closed |
| 35 | 1800039929 | [1.3.1, 4.1.2][A][Business Financing modal] ‘Length’ label is not semantically connect with input field |
| 36 | 1800034584 | [2.4.3][A][Business Financing modal] Focus does not moves forward after choosing Plan B or Plan C |
| 37 | 1800032889 | [2.4.3][A][Business Financing modal] Keyboard focus is not managed appropriately within ‘How does Business Financing work’ modal dialog |
| 38 | 1800019619 | [4.1.2][A][Business Financing modal] ‘Plan A’ is implemented as a button |
| 39 | 1800008454 | [4.1.2][A]Product][mobile] After selecting a radio button, the “checked” radio button state is announced by screen reader as “unchecked” |
| 40 | 1800006319 | [2.1.1][A][Business Financing modal] ‘Explore business financing options’ element is not keyboard accessible |
| 41 | 1800005443 | [4.1.2][A][Business Financing modal] ‘Explore business financing options’ element does not have an accessible role |
| 42 | 1799105934 | [4.1.2][A][Your Cart] ‘Start trade-in’ element does not have an accessible name |
| 43 | 1799105574 | [4.1.2][A][Your Cart] ‘Learn more’ elements do not have an accessible role |
| 44 | 1798983319 | [4.1.2][A][Product bundle] ‘Save 10% when you bundle’ element does not have an accessible role |
| 45 | 1798983178 | [1.3.1][A][Bundle] Visual heading are not semantically marked as one |
| 46 | 1798536352 | [1.3.2][A][Business Home][mobile] Visually hidden “Previous slide”, “Next slide” buttons are focused by screen reader |
| 47 | 1798528243 | [4.1.2][A][Product] ‘VAT Information’ button does not have an accessible name and role |
| 48 | 1793971409 | [1.3.1][A][Business account] Visual headings are not semantically marked as one |
| 49 | 1793955519 | [1.3.2][A][Business account] Hidden heading receives focus |
| 50 | 1792675792 | [2.4.3][A][Cart] Incorrect focus order when closing ‘Item added to your cart’ modal |
| 51 | 1792136138 | [2.4.3][A][Store Dialog] Incorrect focus order when “My store” modal is closed from “Apple Norway” modal |
| 52 | 1708687754 | [sCarah] First heading not h1 |
| 53 | 1707876501 | [4.1.2][A][Collection] ‘Learn more’ element does not have an accessible role |
| 54 | 1707851626 | [4.1.3][AA][mobile] “Current item” instant announcement for the auto-rotated carousel interrupts announcement of all elements on the home page |
| 55 | 1707814807 | [4.1.2][A][Home] ‘Energy Label’ element does not have an accessible role |
| 56 | 1707738955 | [2.4.3][A][Home] Incorrect focus order when moving from main section to Footer |
| 57 | 4466472656 | [1.3.1][A][Home] Two links are improperly grouped within a single H1 heading, causing inconsistent screen reader behavior across platforms |
| 58 | 4469531089 | [AA+][Structure][Home] Two H1 are present on Home page |

## Appendix: Source Documents

The following documents were used to compile these notes.

- Bugs & Issues Fixed, and Theme 2.8 APP Release Briefing (overview)
- APP Shopify Theme Release (packaging)
- Accessibility Release Notes (June 2026)
- Pre-sale Fixes (PDP 1.0 / 2.0), and Pre-Sale “Notify Me” for PDP
- Theft & Loss: Paid Upfront Option, and Checkout Button Fallback for Non-Safari Browsers
- View Cart CTA on Checkout, and Breadcrumbs for Navigation
- Homepage Video Banner, SMB Video Placement, and Second Image on Hover
- Hamburger Menu, Search Bar, Notify Me Flow, and Homepage Banner & Video Slider tracking guides
- H1 & H2 Heading Tag Corrections, and PDP Page Size & Total Blocking Time Reduction
- Pickup / Ships Message Alignment, Sticky Footer on Safari, Product Classification Rules, and Auto-tag Accessories Automation
