# Exploratory Testing Session

**Target:** DemoShop cart and checkout  
**Session type:** Time-boxed exploratory testing exercise  
**Duration:** 30 minutes  
**Charter:** Explore ways a user could create inconsistent cart or order state by changing quantities, navigating between steps and submitting actions repeatedly.

## Areas Explored

- Repeated Add to cart actions
- Quantity changes
- Quantity boundary values
- Removing products
- Browser refresh during cart updates
- Back/forward navigation between cart and checkout
- Repeated final order submission
- Invalid and missing checkout fields

## Observations

1. Adding the same product twice correctly increases the existing line quantity.
2. Quantity 0 is rejected as expected.
3. Changing quantity can leave the displayed total stale until refresh — documented as BUG-002.
4. Returning from checkout to cart preserves the selected products in this scenario.
5. Required checkout fields display useful validation messages.
6. Rapid double submission can create duplicate orders — documented as BUG-003.

## Risks Identified

- **Pricing consistency:** stale totals can confuse users and may indicate state-sync problems.
- **Transaction integrity:** duplicate submission is high risk because a real system could charge or fulfil an order more than once.
- **Client/server consistency:** important transaction controls should be enforced server-side, not only through UI state.

## Follow-up Testing

- Verify totals after several quantity changes in sequence.
- Test decimal prices and rounding behaviour.
- Test very large quantities and maximum allowed quantity.
- Repeat duplicate-submission checks under slow-network conditions.
- Verify backend idempotency if API access becomes available.

## Session Conclusion

The exploratory session found two meaningful transaction-flow defects that structured happy-path testing alone could miss. This demonstrates why exploratory testing complements predefined test cases rather than replacing them.
