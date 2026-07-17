# Secret & sensitive-file detection reference

## Cloud/provider key formats (regex, for the no-tool fallback)

| Provider | Pattern |
|---|---|
| AWS Access Key ID | `AKIA[0-9A-Z]{16}` |
| AWS Secret Access Key | `(?i)aws(.{0,20})?(secret|access)?_?key[^a-zA-Z0-9]*['\"][0-9a-zA-Z/+]{40}['\"]` |
| GCP API key | `AIza[0-9A-Za-z\-_]{35}` |
| GCP service-account JSON | `"type": "service_account"` present in a tracked file |
| Azure storage connection string | `AccountKey=[A-Za-z0-9+/=]{88}` |
| Slack token | `xox[baprs]-[0-9A-Za-z-]{10,48}` |
| GitHub token | `gh[pousr]_[0-9A-Za-z]{36,}` |
| Stripe key | `sk_live_[0-9a-zA-Z]{24,}` |
| Generic private key header | `-----BEGIN (RSA|EC|OPENSSH|PGP|DSA) PRIVATE KEY-----` |
| Generic high-entropy assignment | `(?i)(api_?key|secret|token|password|passwd|pwd)\s*[:=]\s*['\"][^'\"]{12,}['\"]` (flag, then eyeball — highest false-positive rate of this list) |
| JWT | `eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+` |

Real tools (gitleaks/detect-secrets) ship a maintained superset of these — prefer them;
this table exists so the check still runs when neither is installed.

## Files that must never be tracked (content-independent)

```
.env
.env.*
!.env.example
!.env.sample
*.pem
*.key
*.p12
*.pfx
id_rsa
id_rsa.pub
id_ecdsa
id_ed25519
credentials.json
service-account*.json
secrets.yml
secrets.yaml
.aws/credentials
.npmrc            # often contains auth tokens
.netrc
*.keystore
*.jks
kubeconfig
*.kubeconfig
```

The exact list this plugin checks `.gitignore` against lives in
`rules/gitignore-required.txt` (kept separate so it can be extended without touching
this reference file's prose).

## Why a matched secret still needs rotation even after removal

Git history retains every prior version of a file. Deleting the line in a new commit,
or even deleting the file, leaves the secret readable via `git log -p`, reflogs, and
any clone/fork already made. Treat any committed-and-pushed secret as **compromised**:
rotate the credential first, then clean history (`git filter-repo` / BFG) only as a
hygiene follow-up, not as the fix itself.
