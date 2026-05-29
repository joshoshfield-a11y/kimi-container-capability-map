# UI Routing Inconsistencies

## Observation 1: Model Tier Mismatch
- **Displayed:** "Switched to k2.6 Instant for speed"
- **Actual:** k2.6 Thinking remains active (verified via response quality and tool access)
- **Frequency:** Intermittent, specific to user cohort

## Observation 2: Soft Session Limits
- **Displayed:** "Your chat is too long, please start a new one"
- **Actual:** Conversation continues without context loss
- **Frequency:** During promotional debate events

## Hypothesis
A/B testing residue or sticky session affinity rules keep specific containers pinned to warm nodes despite router attempts to migrate. UI shows standard messages; backend enforcement is relaxed for telemetry collection.
