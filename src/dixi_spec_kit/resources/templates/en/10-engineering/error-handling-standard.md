# Error handling standard

## Purpose

Make errors predictable for users, clients and operators: every failure has a stable code, a safe
message, enough context to diagnose it and a clear owner. Applies to services, APIs and workers.

## Error categories

| Category | Meaning | Typical HTTP status | Retry? |
|---|---|---|---|
| Validation | Input does not meet the contract | 400 / 422 | No, fix the input |
| Authentication | Identity missing or invalid | 401 | After re-authenticating |
| Authorization | Identity lacks permission | 403 (or 404 to hide existence) | No |
| Not found | Resource does not exist for this caller | 404 | No |
| Conflict | State or version mismatch | 409 | After refreshing state |
| Rate limit | Caller exceeded a quota | 429 | Yes, after the indicated delay |
| Dependency | An external system failed | 502 / 503 / 504 | Yes, with backoff |
| Internal | Unexpected defect | 500 | Maybe; it is a bug |

## Rules

1. **Domain errors are explicit types**, not generic exceptions with free text. The domain raises
   them; the boundary (controller, handler, consumer) translates them to the transport format.
2. **Stable, documented error codes** such as `ORDER_NOT_FOUND`. Clients branch on the code, never
   on the message. {{pending: error code naming convention and registry location}}
3. **One response shape for every error.** {{pending: error body format, e.g. RFC 9457 problem
   details or an internal envelope}} It includes code, safe message and a correlation ID.
4. **Safe messages.** No stack traces, queries, internal hostnames or personal data in responses.
   Visible messages come from translation catalogs.
5. **Never swallow errors.** Catch only what you can handle; otherwise let it propagate to the
   boundary, which logs it once with context.
6. **Log once, at the boundary**, with the correlation ID, following
   [the logging standard](logging-standard.md).
7. **Retries are bounded** (attempts, total time) with exponential backoff and jitter, and only
   for idempotent operations or operations protected by an idempotency key.
8. **Timeouts on every external call.** {{pending: default timeouts per dependency type}}
9. **Fail closed on security checks**: if authorization cannot be evaluated, deny.
10. **Each error code has a test** that proves its status, shape and message key.

## Example response

```json
{
  "code": "ORDER_NOT_FOUND",
  "message_key": "errors.order_not_found",
  "correlation_id": "{{pending: correlation ID format}}"
}
```

## Related

- [Logging standard](logging-standard.md)
- [API design standard](api-design-standard.md)
- [Secure coding standard](secure-coding-standard.md)
- [Coding standards](coding-standards.md)
