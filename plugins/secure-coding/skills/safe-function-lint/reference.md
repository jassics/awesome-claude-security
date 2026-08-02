# Rule pack: banned/outdated functions → safe alternatives

Severity scale: Critical (RCE/auth bypass), High (data exposure/injection), Medium
(weak-but-exploitable defaults), Low (deprecated, hardening opportunity).
Standards cited: CWE, OWASP ASVS 5.0 (`security architecture/OWASP_Application_Security_Verification_Standard_5.0.0`),
OWASP Code Review Guide v2.

## Python

| Banned pattern | Severity | CWE / ASVS | Risk | Safe alternative |
|---|---|---|---|---|
| `eval(...)`, `exec(...)` on any non-literal input | Critical | CWE-95 | Arbitrary code execution | Remove; if evaluating expressions, use `ast.literal_eval` for literals only, or a real parser |
| `pickle.load(s)` on untrusted/network data | Critical | CWE-502 / ASVS 1.5.2 | Deserialization → RCE | `json` for data interchange; if you must pickle, sign+verify with HMAC before unpickling |
| `yaml.load(stream)` without `Loader=yaml.SafeLoader` | Critical | CWE-502 | Arbitrary object construction → RCE | `yaml.safe_load(stream)` |
| `subprocess.*(..., shell=True)` with interpolated input | Critical | CWE-78 | Shell/command injection | `shell=False` with an argument list; never string-format user input into the command |
| `os.system(...)`, `os.popen(...)` with interpolated input | Critical | CWE-78 | Command injection | `subprocess.run([...], shell=False, check=True)` |
| `hashlib.md5(...)` / `hashlib.sha1(...)` for passwords or tokens | High | CWE-916 / ASVS 6.2.1 | Fast hash → brute-forceable | `argon2-cffi` (Argon2id) or `bcrypt`; never roll your own KDF |
| `random.random()`, `random.randint()` for tokens/secrets/session IDs | High | CWE-330 / ASVS 6.3.1 | Predictable secrets | `secrets.token_urlsafe(32)` / `secrets.token_hex(32)` |
| `requests.get/post(..., verify=False)` | High | CWE-295 | TLS validation disabled → MITM | Remove `verify=False`; pin CA bundle if internal CA: `verify="/path/ca.pem"` |
| `ssl._create_unverified_context()` / `ssl.CERT_NONE` | Critical | CWE-295 | TLS validation disabled | Use default `ssl.create_default_context()` |
| Raw SQL built via f-string/`%`/`.format()` + params | Critical | CWE-89 / ASVS 5.3.4 | SQL injection | Parameterized queries (`cursor.execute(sql, params)`) or the ORM's query builder |
| `flask.Flask(...).run(debug=True)` in anything reachable outside local dev | High | CWE-489 | Werkzeug debugger → RCE via console | `debug=False`; gate `debug=True` behind an env check that can't reach prod |
| `tempfile.mktemp()` | Medium | CWE-377 | TOCTOU race → symlink attack | `tempfile.mkstemp()` / `NamedTemporaryFile()` |
| `assert` used for authz/validation checks | High | CWE-703 | Stripped under `-O`, no exception on failure | Explicit `if not check: raise PermissionError(...)` |
| Hardcoded credential/API-key/token literal (`AKIA...`, `sk-...`, `password = "..."`) | Critical | CWE-798 / ASVS 6.4.1 | Secret in source, in git history forever | Load from env/secret manager (see `secret-guard` skill); rotate if already committed |
| `input()` result passed to `eval`/`exec`/shell | Critical | CWE-95/CWE-78 | Injection via user input | Never; validate/parse explicitly |

## React / JavaScript / TypeScript

| Banned pattern | Severity | CWE / ASVS | Risk | Safe alternative |
|---|---|---|---|---|
| `dangerouslySetInnerHTML={{__html: <unsanitized var>}}` | Critical | CWE-79 / ASVS 5.2.3 | Stored/reflected XSS | Avoid; if HTML rendering is required, sanitize with `DOMPurify.sanitize()` first |
| `element.innerHTML = <var>` / `outerHTML =` with dynamic data | Critical | CWE-79 | DOM-based XSS | `element.textContent =`, or sanitize with DOMPurify before assigning innerHTML |
| `eval(...)`, `new Function(...)` on dynamic strings | Critical | CWE-95 | Arbitrary JS execution | Remove; use `JSON.parse` for data, explicit dispatch tables instead of dynamic code |
| `window.postMessage(data, "*")` or handler missing `event.origin` check | High | CWE-346 | Cross-origin data leak/injection | Always pass an explicit target origin; validate `event.origin` against an allowlist in the listener |
| `href={"javascript:" + var}` or unsanitized `href`/`src` from user input | High | CWE-79 | `javascript:` URI XSS | Validate scheme is `http(s)`; strip/reject `javascript:`, `data:` where not expected |
| Storing JWT/session tokens in `localStorage`/`sessionStorage` | High | CWE-522 / ASVS 3.2 | Any XSS → full token theft, no HttpOnly protection | `HttpOnly`, `Secure`, `SameSite=Strict/Lax` cookies for session tokens |
| `fetch`/`axios` calls to hardcoded `http://` endpoints | Medium | CWE-319 | Cleartext transport | `https://` only; fail closed if TLS unavailable |
| TLS/cert checks disabled: `rejectUnauthorized: false`, `NODE_TLS_REJECT_UNAUTHORIZED=0` | Critical | CWE-295 | MITM | Remove; fix the underlying cert/CA trust issue instead |
| `Math.random()` used for tokens, password reset codes, CSRF tokens | High | CWE-330 | Predictable secrets | `crypto.getRandomValues()` (browser) / `crypto.randomBytes()` (Node) |
| Lodash `_.template()` on untrusted input, or outdated lodash (< 4.17.21) | High | CWE-1104 | Template injection / prototype pollution (CVE-2021-23337 class) | Upgrade lodash; avoid `_.template` on user-controlled strings |
| `child_process.exec(cmd)` with string-interpolated input (Node) | Critical | CWE-78 | Command injection | `child_process.execFile(bin, argsArray)` — no shell interpolation |
| Disabled CSP / `unsafe-inline`, `unsafe-eval` in `Content-Security-Policy` | Medium | ASVS 14.4 | Weakens/defeats XSS mitigation | Nonce- or hash-based CSP; remove `unsafe-inline`/`unsafe-eval` |
| Hardcoded API key/secret in frontend bundle (`const API_KEY = "..."`) | Critical | CWE-798 | Shipped to every client, unremovable post-release | Never ship secrets client-side; proxy the call through a backend that holds the secret |

## Notes

- This pack is deliberately small and curated — it grows as real findings show up in
  review, not by importing every linter rule that exists (avoid alert fatigue).
- Anything not in this table but that looks unsafe: still flag it, just say so
  explicitly ("not in the rule pack, but...") rather than silently skipping it.
