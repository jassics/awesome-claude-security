# Reference: secure coding quick-reference by language

Canonical source for depth: **OWASP Cheat Sheet Series** (cheatsheetseries.owasp.org)
— cite the specific cheat sheet name when going deeper than this table.

## Python

| Risky pattern/API | Why | Safe replacement |
| --- | --- | --- |
| `pickle.load`/`loads` on untrusted data | Arbitrary code execution on deserialize | `json` for data interchange; if pickling is required, sign/HMAC the payload |
| `yaml.load` (default loader) | Can instantiate arbitrary Python objects | `yaml.safe_load` |
| `eval`/`exec` on external input | Code injection | Parse/validate explicitly; use `ast.literal_eval` for literals only |
| `subprocess` with `shell=True` + string interpolation | Command injection | `shell=False` with an argument list; never interpolate untrusted input into a shell string |
| `os.system`/`os.popen` | Command injection, no escaping | `subprocess.run([...], shell=False)` |
| String-formatted SQL (`f"SELECT ... {user_input}"`) | SQL injection | Parameterized queries / ORM query builders |
| `random` for tokens/secrets | Not cryptographically secure | `secrets` module |

**Risky libraries:** unmaintained forks of `requests`/`urllib3` pinned to old CVEs;
`Flask-Login`/`Django` versions below current LTS with known auth CVEs — pin to
maintained, patched versions (see `sast-sca:sca-review`).

## JavaScript / TypeScript (Node)

| Risky pattern/API | Why | Safe replacement |
| --- | --- | --- |
| `eval`, `new Function(str)` | Code injection | Avoid; use structured data + explicit logic |
| `child_process.exec` with string interpolation | Command injection | `execFile`/`spawn` with an argument array, `shell: false` |
| `res.send(userInput)` without encoding in templating | XSS | Auto-escaping template engine (e.g. React JSX default escaping, EJS `<%= %>` not `<%- %>` for untrusted data) |
| Deprecated `request` package | Unmaintained since 2020, known CVEs | `undici`, `node-fetch`, or native `fetch` |
| `JSON.parse` of untrusted input into prototype-polluting merge (`_.merge`, `Object.assign` on nested attacker keys) | Prototype pollution | Validate/allowlist keys; use `Object.create(null)` or a schema validator |
| Hardcoded `jsonwebtoken` secret / `alg: none` accepted | Token forgery | Fixed algorithm allowlist, secret from vault/env, verify signature always |

**Risky libraries:** abandoned/typosquat npm packages — verify maintenance status
and provenance (see `supply-chain-security:dependency-supply-chain-review`).

## Java

| Risky pattern/API | Why | Safe replacement |
| --- | --- | --- |
| `ObjectInputStream.readObject()` on untrusted data | Deserialization RCE (gadget chains) | Avoid native Java serialization for untrusted input; use JSON with a schema, or `ObjectInputFilter` allowlisting |
| String-concatenated JDBC queries | SQL injection | `PreparedStatement` with bind parameters |
| `Runtime.exec(String)` | Command injection, shell parsing issues | `ProcessBuilder` with an argument list |
| Log4j versions with JNDI lookup enabled (pre-patched) | Log4Shell-class RCE | Current patched Log4j2 / disable JNDI lookups explicitly |
| XML parsing without disabling external entities | XXE | Disable DTD/external entity resolution on the parser (`DocumentBuilderFactory` hardening) |

## Go

| Risky pattern/API | Why | Safe replacement |
| --- | --- | --- |
| `exec.Command` with unsanitized user input in args | Command injection | Validate/allowlist arguments; avoid shell interpretation (Go's `exec` doesn't invoke a shell by default — don't wrap in `sh -c` with interpolated input) |
| `text/template` for HTML output | No auto-escaping | `html/template` (context-aware auto-escaping) |
| Disabled TLS verification (`InsecureSkipVerify: true`) | MITM exposure | Verify certs properly; use a private CA pool if needed instead of skipping verification |
| `math/rand` for tokens/secrets | Predictable | `crypto/rand` |

## C / C++ (where still in scope)

| Risky pattern/API | Why | Safe replacement |
| --- | --- | --- |
| `strcpy`/`sprintf`/`gets` | Buffer overflow | `strncpy`/`snprintf`; avoid `gets` entirely |
| Manual memory management without RAII/smart pointers | Use-after-free, double-free | `unique_ptr`/`shared_ptr` (C++), clear ownership discipline (C) |
| `system()` with unsanitized input | Command injection | `execve`-family with argument arrays |

## Ruby

| Risky pattern/API | Why | Safe replacement |
| --- | --- | --- |
| `eval`/`instance_eval` on external input | Code injection | Avoid; use explicit parsing |
| `Marshal.load` on untrusted data | Arbitrary object instantiation | JSON with schema validation |
| Raw SQL string interpolation (outside ActiveRecord parameterization) | SQL injection | ActiveRecord query interface / parameterized `where` |

## Framework-specific defaults to check

- **Django**: `DEBUG = True` in production (leaks stack traces/secrets),
  `SECRET_KEY` committed, missing `SECURE_*` cookie/CSRF settings.
- **Flask**: debug mode enabled in production (Werkzeug debugger allows RCE),
  `render_template_string` on user input (SSTI).
- **Express**: missing `helmet` (security headers), body-parser without size
  limits (DoS), permissive CORS (`origin: '*'` with credentials).
- **Spring**: Actuator endpoints exposed without auth, permissive CORS/CSRF
  disabling without justification.
- **Rails**: `render inline:`/`raw` on user input (SSTI/XSS), mass-assignment
  without strong parameters.

Always cite the matching **OWASP Cheat Sheet** (e.g. "Deserialization Cheat Sheet",
"Injection Prevention Cheat Sheet", "Cross-Site Scripting Prevention Cheat Sheet")
when a finding needs a deeper, authoritative reference than this table.
