# [2.8] Hamburger Menu Interaction Tracking

This document describes the new hamburger menu interaction tracking introduced in Release 2.8. Prior to this release, the mobile hamburger menu icon and its close button were not tracked — only the navigation items within the menu were captured. This update adds event tracking directly to the open and close gestures of the menu itself, enabling teams to measure how many users engage with the mobile navigation menu.

This tracking applies exclusively to the mobile view of the Shopify storefront, where the hamburger menu icon (☰) is visible. The feature is not applicable to desktop viewports where the full navigation bar is rendered.

## Tracked Events

Two new events have been introduced, both using the same data schema but differing in the event_action value.

### Event 1 — Hamburger Menu Open

Fired when the user taps the hamburger icon (☰) to open the navigation menu.

| Parameter | Value | Description |
|---|---|---|
| `event` | `click` | Standard interaction event type |
| `event_category` | `navigation` | Groups menu events under navigation |
| `event_location` | `Header` | Specifies the UI region where the event occurs |
| `event_action` | `hamburger_menu_open` | Distinguishes the open action from the close action |
| `event_label` | `Hamburger Menu` | Human-readable label for the element |
| `click_url` | `/collections/iphone-17-pro` | The URL of the page when the interaction occurs (contextual) |

### Event 2 — Hamburger Menu Close

Fired when the user taps the ‘X’ button to close the navigation menu.

| Parameter | Value | Description |
|---|---|---|
| `event` | `click` | Standard interaction event type |
| `event_category` | `navigation` | Groups menu events under navigation |
| `event_location` | `Header` | Specifies the UI region where the event occurs |
| `event_action` | `hamburger_menu_close` | Distinguishes the close action from the open action |
| `event_label` | `Hamburger Menu` | Human-readable label for the element |
| `click_url` | `/collections/iphone-17-pro` | The URL of the page when the interaction occurs (contextual) |
