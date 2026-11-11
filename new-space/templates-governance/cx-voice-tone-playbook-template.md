# Template: CX Guidelines & Playbook

````markdown
# CX Guidelines: [Product / Service Area]

## 1. Voice and Tone Principles
- **Empathetic & Accountable:** Acknowledge frustration directly; never blame the user or external partners.
- **Concise & Direct:** Put the answer/solution in the first two sentences.
- **Human, Not Robotic:** Avoid corporate jargon ("We regret any inconvenience this may have caused"). Instead use: "We know how disruptive this is, and we're actively fixing it."

## 2. Dos and Don'ts Table
| Scenario | ❌ Do NOT Say | ✅ Recommended Response |
|---|---|---|
| System Downtime | "The servers are down, there is nothing we can do right now." | "Our team has identified the cause and is actively deploying a fix. Here is what you can do in the interim..." |
| Missing Feature | "That feature does not exist." | "That isn't currently supported, but I've logged this directly with our product team under ticket [ID]." |
| User Error | "You configured the setting incorrectly." | "To get this working as expected, let's update [Setting A] to [Value B]." |

## 3. Communication Matrix for Outages & Disruptions
- **Internal Alert:** Post in `#[incident-cx-coordination]` within 10 minutes.
- **External Banner:** Update public status page if disruption exceeds 15 minutes.
- **Proactive Notification:** Email users affected by batch jobs or failed transactions.

## 4. Customer Feedback Loop
- All customer feature requests and friction points must be tagged with `#voice-of-customer` in [Zendesk / Radar / Jira].
- Product & CX bi-weekly review meeting meets every alternate Thursday.
````
