# [2.8] Homepage Banner & Video Slider Tracking

## Overview

The homepage banner component displays up to eight sequential banner slots, but individual banner clicks were not being tracked in Adobe Analytics, making it impossible to measure campaign efficiency or evaluate the performance of each campaign creative in the slider independently. Each slot needed to fire a distinct, attributable analytics event linked to the specific banner creative shown.

Previously, video events in the homepage slider were identified using an internal Video_ID, which was not meaningful for campaign reporting. A more actionable identifier was needed — one that could be directly mapped back to a campaign or destination URL for performance analysis.

{% hint style="info" %}
**Goal**
Understand which homepage banner creative drives the most engagement (plays, completions) and clicks. With Click_URL as the identifier, each banner’s performance can be measured independently across all video event types and device categories, enabling creative A/B analysis and campaign attribution.
{% endhint %}

## Solution

Two changes were made in Release 2.8 to address this issue:

- Individual banner click events are now tracked for each of the up to eight banner slots in the homepage slider, allowing per-banner engagement measurement.
- The video event tracking logic has been updated to use Click_URL (the destination URL linked from the video/banner) as the primary identifier, replacing the previous Video_ID. This makes video event data directly actionable in Adobe Analytics reports — each row in the report corresponds to a recognisable page or campaign destination.

{% hint style="info" %}
**Key Change: Video_ID → Click_URL**
Video events (Video Play, Video Pause, Video Complete) previously reported against an internal Video_ID that required a separate lookup to understand which creative was involved. In Release 2.8, these events now report against the Click_URL of the video/banner in the slider. This makes the Adobe Analytics Video Plays (by Click URL) report immediately readable without any additional data joining.
{% endhint %}

## Before & After: Video Event Identifier

The table below shows how video event reporting has changed. The identifier field now carries the Click_URL value instead of the internal Video_ID.

| Event | Before (Video_ID) | After 2.8 (Click_URL) |
|---|---|---|
| Video Play | `video_id_7482a` | `/collections/macbook-neo` |
| Video Pause | `video_id_7482a` | `/collections/macbook-neo` |
| Video Complete | `video_id_7482a` | `/collections/macbook-neo` |
| Video Play | `video_id_3b19c` | `/collections/iphone-17-pro` |
| Video Complete | `video_id_3b19c` | `/collections/iphone-17-pro` |

## Events Tracked

The following video interaction events are tracked for each banner in the homepage slider. All events now use Click_URL as the identifying dimension in Adobe Analytics.

### VIDEO EVENTS — All Banner Slots (up to 8)

| Parameter | Value | Description |
|---|---|---|
| Event type | Video Play | Fired when the video in a banner slot begins playing (including auto-play start) |
| Event type | Video Pause | Fired when the video is paused by the user |
| Event type | Video Complete | Fired when the video plays to completion |
| Identifier | Click_URL | The destination URL of the banner/video slot. Replaces Video_ID as the primary dimension for all video events. |
| Breakdown | Device type | Each video event is broken down by device category: Mobile Phone, Tablet, Other (desktop/other) |
| Capacity | Up to 8 banners | The tracking logic supports up to eight banner slots in the slider sequence. Each slot fires events independently. |
| Platform | Adobe Analytics | Events are captured in Adobe Analytics. The report dimension is “Video Plays (by Click URL)”. |

## Adobe Analytics Report: Video Plays by Click URL

The updated tracking is visible in the Adobe Analytics “Video Plays (by Click URL)” report. Each row represents a distinct banner destination URL and shows Video Play, Video Pause, and Video Complete counts broken down by device type. The example data below reflects the actual report output captured from the staging environment.

{% hint style="info" %}
**Report Interpretation**
The top-performing banner in the example data is /collections/macbook-neo, accounting for 79.6% of all Video Plays and 72.2% of all Video Completes. This immediately shows that the MacBook Neo campaign creative is the most engaged banner in the current slider sequence, without any additional data joining or lookup.
{% endhint %}

### Sample Report Data

Report: Video Plays (by Click URL) — Top 10 Click URLs by Video Play volume. Device breakdown columns shown for Mobile Phone and Other. Full report includes Tablet column.

| Click URL (Video Slider) | Video Play | Video Pause | Video Complete | VP Mobile | VC Mobile | VC Other |
|---|---|---|---|---|---|---|
| `/collections/macbook-neo` | 41,420 (79.6%) | 15,288 (84.2%) | 23,784 (72.2%) | 29,016 (80.2%) | 16,516 (73.2%) | 6,869 (70.3%) |
| `/pages/istyle-dny` | 6,251 (12.0%) | 1,821 (10.0%) | 5,376 (16.3%) | 4,027 (11.1%) | 3,151 (14.0%) | 2,120 (21.7%) |
| `/collections/iphone-17-pro` | 3,167 (6.1%) | 642 (3.5%) | 3,045 (9.2%) | 2,497 (6.9%) | 2,471 (10.9%) | 482 (4.9%) |
| `/pages/istyle-dni` | 1,013 (1.9%) | 357 (2.0%) | 647 (2.0%) | 508 (1.4%) | 351 (1.6%) | 276 (2.8%) |
| `/ar/collections/iphone-17-pro` | 87 (0.2%) | 30 (0.2%) | 98 (0.3%) | 74 (0.2%) | 86 (0.4%) | 12 (0.1%) |
| `/` (homepage) | 87 (0.2%) | 1 (0.0%) | 2 (0.0%) | 43 (0.1%) | 1 (0.0%) | 1 (0.0%) |
| `/pages/iphone` | 7 (0.0%) | 0 (0.0%) | 0 (0.0%) | 6 (0.0%) | 0 (0.0%) | 0 (0.0%) |

Note: Percentage values shown are each URL’s share of the total for that metric column (e.g. 79.6% of all 52,044 Video Plays originate from the /collections/macbook-neo banner).

## Banner Slot Structure

The homepage slider supports up to eight banner slots. Each slot is tracked independently. The Click_URL for each slot is the destination URL configured in the banner CMS/Shopify admin for that creative.

| Slot | Click_URL (example) | Campaign / Creative |
|---|---|---|
| Banner 1 | `/collections/macbook-neo` | MacBook Neo launch campaign |
| Banner 2 | `/pages/istyle-dny` | iSTYLE Days promotional page |
| Banner 3 | `/collections/iphone-17-pro` | iPhone 17 Pro campaign |
| Banner 4 | `/pages/istyle-dni` | iSTYLE Days (alternate locale) |
| Banner 5–8 | (configured per campaign) | Additional campaign slots |

## Implementation Notes

- **Click_URL source:** The Click_URL value is the destination URL of the banner slot, not the current page URL. It is configured in Shopify/CMS against each banner creative and reflects the campaign landing page.
- **Auto-play included:** Auto-play video events are included. If a banner video auto-plays, the Video Play event fires from the moment the video begins playing. This is consistent with the existing auto-play tracking behaviour noted in the Adobe Analytics report subtitle.
- **Device breakdown:** All three event types (Video Play, Pause, Complete) are broken down by device category (Mobile Phone, Tablet, Other) in the Adobe Analytics report, enabling device-level campaign performance analysis.
- **Slot capacity:** Up to 8 banner slots are supported. If fewer than 8 banners are configured in the slider, only the active slots generate events. Empty or inactive slots do not fire events.
- **Historical data note:** The change from Video_ID to Click_URL is a breaking change in the reporting dimension. Historical data prior to Release 2.8 will show Video_ID values; data from Release 2.8 onwards will show Click_URL values. Reporting stakeholders should be aware of this split when comparing periods.
