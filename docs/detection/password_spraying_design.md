# Cloud Security Lab

# Password Spraying Detection

## 1. Introduction

Password Spraying is one of the most common password-based attacks observed in enterprise environments.

Unlike traditional brute-force attacks, where multiple passwords are tested against a single account, Password Spraying attempts to authenticate against many different user accounts using the same password.

This technique reduces the probability of triggering account lockout policies while increasing the likelihood of compromising weak or commonly used passwords.

The objective of this detector is to identify this behavior during attack simulations executed within Cloud Security Lab.

---

# 2. Detection Objective

The detector aims to identify situations where a single source IP performs authentication attempts against multiple user accounts while repeatedly using the same password.

This behavior differs from Credential Stuffing because the attacker is not using many different leaked credentials.

Instead, the attacker assumes that several users may share the same weak password.

---

# 3. Attack Characteristics

A typical Password Spraying attack follows this sequence:

```text
Source IP

↓

Password: Spring2025!

↓

User A

↓

User B

↓

User C

↓

User D

↓

User E
```

The password remains constant while the targeted usernames change.

---

# 4. Difference from Other Detectors

## Brute Force

* One user.
* Many passwords.

---

## Credential Stuffing

* Many users.
* Many different passwords.

---

## Password Spraying

* Many users.
* One identical password.

Although these techniques may appear similar, each one represents a different attack strategy and therefore requires an independent detection rule.

---

# 5. Proposed Detection Logic

The detector will evaluate authentication events generated from the same source IP during a configurable time window.

The detection rule will verify:

* Number of distinct usernames.
* Number of authentication attempts.
* Number of distinct passwords.

An alert will be generated when:

* The number of targeted usernames exceeds the configured threshold.
* The same password has been used across those authentication attempts.

---

# 6. Required Event Data

The current Event Model stores:

* Username
* Source IP
* Event Type
* Resource
* Timestamp

To support Password Spraying Detection, the event model must be extended to include:

* Attempted Password

This attribute will only be used within the laboratory for attack simulation purposes.

It does not represent secure password storage.

Instead, it represents the password value intentionally supplied during the simulated authentication attempt.

---

# 7. Proposed Configuration

Initial configuration:

* Username Threshold: 5 users
* Time Window: 10 minutes

These values may be adjusted in future versions depending on simulation requirements.

---

# 8. Generated Alert

Successful detections will generate the following alert type:

```text
PASSWORD_SPRAYING
```

This alert will subsequently be processed by the Alert Manager and may later participate in future correlation rules.

---

# 9. Known Limitations

Version 2.0 focuses exclusively on detecting repeated password reuse from a single source IP.

The detector does not currently evaluate:

* Password similarity
* Distributed Password Spraying
* Botnet-based attacks
* Device fingerprinting
* User behavior analysis

These capabilities remain part of the long-term roadmap.

---

# 10. Future Evolution

Future versions may expand this detector through:

* Risk scoring
* Correlation with Brute Force Detection
* Integration with Threat Intelligence
* User and Entity Behavior Analytics (UEBA)
* Machine Learning models

The current implementation establishes the architectural foundation required for these future improvements while maintaining the modular design of Cloud Security Lab.
