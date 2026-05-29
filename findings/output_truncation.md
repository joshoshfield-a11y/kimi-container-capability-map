# Output Pipeline Fragility

## Incident
- **Date:** 2026-05-29
- **Prompt:** "Continue your last two responses, both were cut short"
- **Result:** Response truncated mid-delivery
- **Resolution:** Required 5 retries for complete delivery

## Characteristics
- No error message displayed
- Same prompt, same context — non-deterministic outcome
- Suggests different inference nodes have different buffer capacities

## Mitigation
Shift to chunked delivery: smaller, numbered segments per response.
