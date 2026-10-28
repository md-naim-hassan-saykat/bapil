# Security Policy

## Scope

This policy covers the reference implementation in `implementation/` and the build scripts in `blueprint/` and `reports/`. The reference implementation is a research prototype (package version 0.1.0). It is not a production system and must not be used to process personal or confidential data.

## Supported versions

| Version | Supported |
|---|---|
| Repository release v1.1.x (package 0.1.x) | Yes |
| Earlier releases (documents only) | Not applicable |

## Reporting a vulnerability

Please do not open a public issue for a security problem. Report it privately through GitHub's "Report a vulnerability" function on the repository's Security tab, or contact the maintainer through the address on the GitHub profile. Include a description, the affected file or command, steps to reproduce and any suggested fix.

You can expect an acknowledgement within five working days. Confirmed problems are fixed in a new release, and the fix is recorded in `CHANGELOG.md`. Reporters are credited unless they ask not to be.

## Dependency and supply-chain practice

* The package uses only the Python standard library, so there are no third-party runtime dependencies to pin or audit.
* Any future dependency must be pinned to an exact version, listed in a software bill of materials and approved before use.
* The GitHub Actions workflows run with read-only repository permissions.
* Secrets, keys and personal data must never be committed. The demonstration corpus contains only BAPIL's own published documents.
