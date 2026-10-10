# BUG-001 — Invalid email format accepted on login

**Related test case:** TC-003  
**Severity:** Medium  
**Priority:** Medium  
**Status:** Open  
**Environment:** Desktop / Chromium-based browser / DemoShop test scenario

## Summary

The login form accepts an obviously invalid email format such as `petros@` and attempts authentication instead of blocking submission with client-side validation.

## Preconditions

- Login page is open.
- User is signed out.

## Steps to Reproduce

1. Enter `petros@` in the email field.
2. Enter any value in the password field.
3. Select **Sign in**.

## Expected Result

Submission is blocked and the user sees a clear message explaining that a valid email address is required.

## Actual Result

The form submits the credentials and returns a generic authentication failure.

## Impact

Invalid input reaches the authentication flow unnecessarily and provides weaker user feedback. This is primarily a validation/usability defect rather than a direct security finding.

## Notes

Server-side validation would still be required even if client-side validation is added.
