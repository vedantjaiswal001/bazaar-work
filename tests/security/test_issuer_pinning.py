"""Issuer-key pinning is fail-CLOSED.

The one control that stops a compromised agent from minting its own mandate (with
its own key and a bigger cap) is issuer-key pinning. This test locks in that the
service refuses to run without it, so a future caller cannot silently disable the
pin by omission. Running unpinned is possible only with an explicit opt-in.
"""
from __future__ import annotations

import sqlite3

import pytest
from bazaar.crypto.signing import generate_keypair
from bazaar.verifier.service import AuthorizationService


def test_service_is_fail_closed_without_issuer_pinning():
    conn = sqlite3.connect(":memory:")

    # No trusted issuer set -> refuse to run (do not silently self-verify).
    with pytest.raises(ValueError):
        AuthorizationService(conn)

    # An empty set is not a trusted set either.
    with pytest.raises(ValueError):
        AuthorizationService(conn, trusted_issuer_keys=set())

    # Running unpinned must be a deliberate, explicit choice (tests/dev only).
    AuthorizationService(conn, allow_unpinned=True)

    # The normal, pinned construction is accepted.
    _sk, vk = generate_keypair()
    AuthorizationService(conn, trusted_issuer_keys={vk})
