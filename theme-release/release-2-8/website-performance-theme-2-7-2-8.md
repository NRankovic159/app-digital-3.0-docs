# Website Performance: Theme 2.7 → 2.8

Core Web Vitals summary · Home, Collection & Product pages · Desktop and mobile

Google PageSpeed / Lighthouse (lab test)

**Bottom line:** Version 2.8 is meaningfully faster than 2.7, with the biggest gains on mobile and on the category (collection) page. Shoppers see content sooner, pages respond more quickly, and layouts are steadier while loading. A couple of desktop measurements moved slightly in the other direction but remain healthy.

## Headline improvements

- Mobile pages load about a third faster. Time for the main content to appear on a phone dropped from ~11–13 seconds to ~7–9 seconds on all three pages — the product page improved most (−45%).
- The category page is dramatically better on desktop. Its performance score jumped from 69 to 95, and the time the page spends frozen or unresponsive while loading fell about 90% (690 ms → 70 ms).
- Pages are more visually stable. On the product page, unexpected layout movement (content shifting as it loads) was cut by more than half.
- Performance scores rose on 5 of 6 page / device combinations.

## Overall performance score (0–100, higher is better)

| Page | Device | 2.7 | 2.8 | Change |
|---|---|---|---|---|
| Homepage | Desktop | 97 | 96 | ~flat |
| Homepage | Mobile | 63 | 70 | ▲ +7 |
| Collection (MacBook Pro) | Desktop | 69 | 95 | ▲ +26 |
| Collection (MacBook Pro) | Mobile | 61 | 71 | ▲ +10 |
| Product (MacBook Air) | Desktop | 77 | 80 | ▲ +3 |
| Product (MacBook Air) | Mobile | 61 | 61 | ~flat* |

\*Product-mobile score held flat, but its main-content load time still improved sharply (see below).

## Mobile main-content load time (seconds, lower is better)

| Page | 2.7 | 2.8 | Improvement |
|---|---|---|---|
| Homepage | 11.1 s | 8.6 s | −23% |
| Collection | 11.1 s | 7.5 s | −32% |
| Product | 12.8 s | 7.1 s | −45% |
