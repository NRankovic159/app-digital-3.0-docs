# Bugs & Issues Fixed

This document provides an overview of all bugs and issues resolved as part of the 2.8 release. The engineering and QA teams have addressed a total of 58 reported items spanning multiple areas of the platform, including BOPIS (Buy Online, Pick Up In Store), Cart behaviour, PDP 1.0 and 2.0, Pre-Sale product handling, AppleCare / Theft & Loss flows, navigation, search, and SEO/accessibility improvements. Each fix has been tested and verified against the expected results described below.

## Fixed Issues — 2.8 Release

| # | Area / Component | Issue | Resolution |
|---|---|---|---|
| 1 | CTO | Selected values in Financing sections are not reset after changing options in Advanced Customization section | When options change in the Advanced Customization section, the AppleCare, Trade-in, and Financing section values are now properly reset so the user can re-select them. |
| 2 | Cart | The price is displayed as 0 for the free product if it was added as a Hero product when over the quantity limit | The correct price is now displayed for free products added as a Hero product when the quantity limit is exceeded. |
| 3 | Cart | Nothing happens when exceeding max quantity in cart if AppleCare is added to a bundle | A notification now appears when the maximum allowed quantity is exceeded, the cart and total price update accordingly, and the user can remove AppleCare from the cart. |
| 4 | Cart | Pickup message only considers main product availability, ignores Free/Discounted product availability | 'Pickup unavailable' is now correctly displayed when a Free/Discounted product is not available at the selected store. |
| 5 | Cart | Unable to add AppleCare to any cart product when max quantity notification is displayed | Users can now add AppleCare to any cart product even when a maximum quantity notification is being shown. |
| 6 | Cart | VAT link does not work after adding a discounted product | The VAT pop-up now opens correctly after a discounted product is added to the cart. |
| 7 | Cart / Side Drawer | Protection Plan added to Bundle product leaves only Hero product in the cart | Adding a Protection Plan to a Bundle product no longer removes the Bundle. All bundle items remain in the cart. |
| 8 | Cart | Two H1 tags on Cart page | The Cart page now contains only one H1 tag, resolving the accessibility and SEO violation. |
| 9 | BOPIS | Does not work when 'Use my current location' is clicked with location access disabled | The system no longer fails or hangs when location access is denied. Users can continue using the site normally. |
| 10 | BOPIS | Information inconsistency for Bundles (Hero, Hero+Bundle on PDP/Cart/Checkout show different pickup times) | Pickup information is now consistent across the Hero component, Hero+Bundle on PDP, Cart, and Checkout. |
| 11 | BOPIS | Selected store cannot be changed on other pages after switching store on Checkout | The selected pickup store is now correctly persisted and changeable across all pages. |
| 12 | BOPIS | Currency changes when switching between available stores on Checkout page | Switching the pickup store on the Checkout page no longer affects the displayed price currency. |
| 13 | BOPIS | Nearest available store is displayed for bundles on Checkout page instead of the selected one | The previously selected store is now pre-selected and displayed correctly for bundles on the Checkout page, with radio button selection available. |
| 14 | BOPIS | Checkout page: Distance to selected store always displays as 0 mi | The actual distance to the selected store is now correctly calculated and displayed. |
| 15 | BOPIS | Checkout: Incorrect pickup store displayed as selected | The correct previously selected store is now shown as selected on the Checkout page. |
| 16 | BOPIS – BTB | Pickup is not available for some products | Fixed. Pickup is now available for the affected products. |
| 17 | BOPIS | Checkout: Incorrect pickup time displayed | Pickup time is now correctly displayed on the Checkout page (e.g. Bundle pickup time shows 3-4 weeks). |
| 18 | Header | Language Switcher is absent in the Header | The Language Switcher is now present in the Header with the ability to change language options. |
| 19 | My Store | Select another Store CTA: Header with My Store popup are not faded out when Side Drawer is opened | The Header menu and My Store pop-up are now correctly faded out (inactive) when the Side Drawer is opened. |
| 20 | Mobile / Header | Header is displayed on Filter popup | The Header is no longer displayed on the Filter popup. Fixed. |
| 21 | Bug – Lab9 (Navigation) | Persistent Menu Dropdown in Safari and Chrome — dropdown stays visible after clicking outside | The dropdown now correctly closes when the user clicks elsewhere on the page. |
| 22 | B2B – Search Results | Product card alignment issue: 'Shop' button and badge are misaligned between cards in the same row | All product cards in the same row are now vertically aligned. Key elements (badge, 'Shop' button) are consistently positioned regardless of content length. |
| 23 | Search Suggestions | No visible scroll bar or indicator in the scrollable Product section of the search suggestions dropdown | The entire product list in the search suggestions dropdown is now scrollable with a visible scroll indicator. |
| 24 | AASP LP – Grid View | Cards have different heights when text of varying length is added | All cards now have uniform height regardless of the length of their content. |
| 25 | Side Drawer | Free/offered product stuck in cart if user navigates to the cart page during add action | The free product is now correctly added to the cart and can be managed or removed normally. |
| 26 | Side Drawer | If Free/Discounted product added to cart automatically, the count of added products changes incorrectly when AC+ is added | The quantity of each added product item (Hero, AppleCare) now correctly reflects 2 when two items are present. |
| 27 | Side Drawer | AC+ Theft & Loss is not displayed as added to the cart; only added for one product | Two AC+ Theft & Loss products are now correctly shown as added to the cart. |
| 28 | PDP 1.0 | Free/Discounted product is displayed in Additional Services section instead of Additional Offers | Free/Discounted products are now correctly displayed in the Additional Offers section. |
| 29 | Additional Offers | 'Additional offers' label displayed for each individual product item instead of once as a common label | The 'Additional offers' label is now displayed once as a common label for all offered products. |
| 30 | Mobile – AC+ T&L | Active Acceptance: Incorrect design applied | The correct design has been applied for AC+ T&L Active Acceptance on mobile. |
| 31 | PDP 1.0 – T&L | Active Acceptance popup is not displayed after clicking the Add button | The T&L Active Acceptance popup now correctly appears after clicking the Add button. |
| 32 | AppleCare T&L – UI | Chevron icon in incorrect position for 'Learn more about Theft & Loss' link; 'Learn more about AppleCare+' link visually associated with wrong card | The chevron is now aligned correctly. The 'Learn more about AppleCare+' link is now displayed closer to its corresponding product card, matching the placement of the T&L link. |
| 33 | AC+ T&L | T&L pop-up is not displayed when re-adding AC+ T&L after switching to standard AC+ | The AC+ T&L pop-up for active acceptance is now correctly displayed when re-adding AC+ T&L after switching to standard AC+. |
| 34 | PDP 1.0 | Incorrect pickup message displayed if AppleCare is added to the cart (shows '24 hours' instead of '1 day') | The pickup message now correctly shows '1 day' when AppleCare is added to the cart. |
| 35 | PDP 2.0 | Incorrect styles applied to the Monthly Pricing link after closing the Financing popup | The correct styles are now applied to the Monthly Pricing link after the Financing popup is closed. |
| 36 | PDP 2.0 | Empty Theft & Loss slot displayed if Theft & Loss is not configured for the collection | The empty T&L slot is no longer shown. Only the AppleCare+ component is displayed when T&L is not configured. |
| 37 | PDP 2.0 | AppleCare Theft & Loss is not displayed on the page for CTO products | AppleCare Theft & Loss is now correctly displayed in the 'Protect your product' section for CTO products. |
| 38 | PDP 2.0 | 'Learn More' link cannot be configured separately for Theft and Loss | The 'Learn More' link is now configurable separately for Theft and Loss. |
| 39 | CTO – PDP 2.0 | Next option (Trade-in) unavailable after selecting T&L | The next configuration step (Trade-in) is now correctly available after selecting T&L. |
| 40 | Pre-Sale – PDP | Switching between product configurations is not working (colour remains unchanged) | Selecting a different product configuration now correctly updates all product details. |
| 41 | Pre-Sale | Monthly pricing displayed on Financing pop-up for BTC users when Financing is selected | Monthly Pricing is no longer displayed in the Summary section for BTC users when Financing is selected. |
| 42 | Pre-Sale | Pre-sale product shown as available for pickup in the Store Side Drawer | 'Pickup unavailable' is now displayed for all stores in the Store Side Drawer for pre-sale products. |
| 43 | Pre-Sale | Price displayed for pre-sale product when used in a bundle; user can add it to the cart | Price is no longer displayed for pre-sale products in a bundle, and users cannot add a pre-sale product to the cart. |
| 44 | LOB Page – Pre-Sale | Price is displayed for Pre-Sale product on Dynamic Banner and Sub-LOB modules | Price is no longer displayed for pre-sale products on the Dynamic Banner and Sub-LOB modules; a 'Notify me' CTA is shown instead. |
| 45 | Family Stripe – Pre-Sale | Title for pre-sale product is misaligned with titles of other products | The pre-sale product title is now correctly aligned with the titles of other products. |
| 46 | FBT – Pre-Sale | Price is displayed for Pre-Sale product (e.g. iPhone Air 256GB Space Black) | Price is no longer displayed for pre-sale products in the FBT (Frequently Bought Together) component. |
| 47 | Cart / PLP – AI Carousel | Product Carousel (AI suggestions): Price is displayed for Pre-Sale product | Price is no longer displayed for pre-sale products in the AI Product Carousel. |
| 48 | Pre-Sale | Pre-Sale product can be added to the cart as a Free/Discounted product | Pre-sale products can no longer be added to the cart via the Side Drawer or Cart page. Price is not displayed for pre-sale products on the Cart page. |
| 49 | Pre-Sale – Dynamic Product Prioritization | Price is displayed for Pre-Sale product when configured as Dynamic Product Prioritization | Price is no longer displayed for pre-sale products regardless of their prioritization configuration. |
| 50 | Bug – Appstaging (Accessories) | Accessories with Multiple Compatibility: Apple Displays incorrectly appearing in accessory collections due to wrong auto-generated tags | Tags are now generated correctly, preventing Displays from being pulled into accessory collections. |
| 51 | Bug – Epos Austria | Store Locator: wrong decimal separator for German (shows '0.2 km' instead of '0,2 km'); 'Get Directions' string cannot be translated | Decimal separator now correctly uses a comma for German (e.g. '0,2 km'). The 'Get Directions' string is now available in theme content settings for translation (e.g. 'Route berechnen'). |
| 52 | Bug – Epos Austria | 'Show second image on hover' in the collection display does not work | Fixed. The setting now works correctly for pages with Grid layout (Accessories PLPs and Search Results page). |
| 53 | Product Prioritization | If the first prioritized product is out of stock, the availability of the second product is ignored | The second prioritized product is now correctly evaluated and displayed when the first prioritized product is out of stock. |
| 54 | Family Stripe | 'From Pricing' is not displayed on Mac Accessories card | From Pricing is now correctly displayed on the Mac Accessories card in the Family Stripe. |
| 55 | Marketing Page | Broken UI elements and missing images on the marketing page | Resolved. The page was using the wrong template; the correct template has been applied and the page now displays correctly. |
| 56 | SEO / Accessibility – PLP | ItemList schema.org markup is missing on PLP pages | ItemList schema.org markup is now correctly present on all PLP pages. |
| 57 | SEO / Accessibility – PDP | Multiple H1 tags on PDP pages for out-of-stock products | PDP pages now contain only one H1 tag for out-of-stock products. |
| 58 | SEO / Accessibility | Non-semantic H2 tags present in markup (hidden or structural elements using H2) | H2 tags are now only used for headings that are visible to users and represent the actual page structure. |
