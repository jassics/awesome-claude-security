# secure-review reference: business logic checklist + PoC templates

## Business logic abuse checklist

For each business-critical flow identified in intake:

**Flow integrity**
- Step skipping: can a user jump from step 1 to step 3 without completing step 2 (place order without payment, skip OTP)?
- State tampering: is flow state stored client-side (cookie/localStorage/hidden field) and trusted on the next request?
- Replay: can a successful payment/OTP/token be replayed for a different transaction?
- TOCTOU races: check-then-act gap exploitable with parallel requests (double-spend, duplicate coupon use, concurrent order edits)?

**Pricing & financial logic**
- Can price/quantity/discount be modified in the request and is it re-validated server-side against the catalog?
- Negative quantity/price handling?
- Coupon codes: single-use enforced atomically (DB constraint), or racy?
- Refund logic: valid original transaction required? Refund amount capped at purchase amount?
- Wallet/credit: deduction+credit atomic in one DB transaction? Double-credit possible?

**Limits & quotas**
- Rate limits enforced per user *and* per IP? Bypassable by rotating IP/UA?
- Free-tier limits enforced at DB level or only in app logic (client-bypassable)?
- File upload size/type/count enforced server-side?

**Workflow & role abuse**
- Can an actor approve their own submission (self-approval)?
- Can a user act on another user's resource by guessing/enumerating an ID?
- Do irreversible ops (delete, refund) require a second factor/second approver?
- Can an approval step be bypassed by calling the post-approval endpoint directly?

**Time & scheduling**
- Flash sale/limited inventory: is stock check + reservation atomic? Race to negative inventory?
- Are scheduled jobs reachable via an exposed endpoint?
- Time-boxed offers: server time or client-supplied timestamp trusted?

### Abuse-scenario format

```
ABUSE SCENARIO:
  Actor: [guest / authenticated user / seller / ops]
  Goal: [financial gain / data theft / service disruption]
  Steps:
    1. ...
    2. ...
  Expected (buggy) outcome: ...
  Business impact: $X loss / N records exposed / ...
```

## PoC template (for `poc <FINDING-ID>`)

```
Steps to Reproduce (Burp Suite):
  1. Proxy > Intercept ON
  2. Trigger: <action in the app>
  3. Intercept request to: <METHOD /path>
  4. Modify: <field/value>
  5. Forward. Observe: <expected vulnerable response>

Steps to Reproduce (Postman):
  Method: POST/GET/PUT/DELETE
  URL: {{base_url}}<path>
  Headers:
    Authorization: Bearer <victim_token>
    Content-Type: application/json
  Body:
    { "<param>": "<malicious_value>" }
  Expected (vulnerable) response: HTTP 200 / <data that shouldn't be returned>
```

## Finding record template

```
ID: SEC-XXX
Title: <one line>
Severity: Critical | High | Medium | Low   (CVSS via security-reporting:cvss)
Category: Auth | AuthZ | Business Logic | Injection | Headers | PII | ...
File: <path>:<line>

Vulnerable code:
  <snippet>

Attack/abuse scenario:
  <who, how, what they get>

Recommended fix:
  <specific code/config change>

References: OWASP <link>, CWE-XXX
```
