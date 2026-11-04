# [2.8] Search Bar Initiation Tracking

This document describes the search bar initiation tracking introduced in Release 2.8. The feature captures a new engagement event at the moment a user clicks or taps into the search bar — before any keyword has been typed. This provides visibility into search intent that was previously unmeasured, allowing teams to understand how many users attempt to search without necessarily completing a query.

{% hint style="info" %}
This event fires on search bar focus/click only — BEFORE the user types any keyword. It is distinct from existing search query events and is designed to measure top-of-funnel search intent. No search term is captured at this stage.
{% endhint %}

## Scope & Prerequisites

Tracking applies to the search bar component rendered within the Shopify storefront header, on both mobile and desktop viewports. The event is triggered on the initial activation (focus) of the search input field.

- Applies to: All viewports where the search bar is accessible
- Trigger moment: On search bar click/focus, before any keystroke

## Tracked Events

A single new event has been introduced. The event_action value `search_initiate` identifies this as a pre-search engagement touch point, separate from events that fire when a query is submitted.

### Search Bar Initiation Event

Fired when the user clicks or taps into the search bar to activate it, before any search keyword is entered.

| Parameter | Value | Description |
|---|---|---|
| `event` | `click` | Standard interaction event type |
| `event_category` | `engagement` | Categorises the event as a user engagement action (V43) |
| `event_location` | `Search Bar` | Identifies the UI component that was interacted with (V41) |
| `event_action` | `search_initiate` | Captures the moment of search bar activation, before typing (V42) |
| `event_label` | `" "` (empty) | No label at initiation stage — no keyword has been entered yet |
| `click_url` | `/` (dynamic) | The URL of the page where the user initiated the search |

## Variable Mapping

The following variable references correspond to the analytics implementation tags referenced in the task specification.

| Variable | Field | Value |
|---|---|---|
| V41 | `event_location` | "Search Bar" |
| V42 | `event_action` | "search_initiate" |
| V43 | `event_category` | "engagement" |

## Implementation Notes

- **Trigger timing:** The event fires on search bar focus, not on input or form submission. It represents intent to search, not a completed search action.
- **Empty event_label:** event_label is intentionally empty at this stage. Keyword-level tracking is handled by separate downstream events once the user types and submits a query.
- **click_url is dynamic:** click_url reflects the page the user is on when they activate the search bar. It will vary depending on where in the storefront the interaction occurs.
- **Adobe Analytics event61:** Adobe Analytics fires event61 in addition to the digitalData push. Ensure this event is correctly mapped in the Adobe Analytics tag configuration.
- **Backward compatibility:** No changes are required to existing search query, autocomplete, or results tracking. This event is additive only.
