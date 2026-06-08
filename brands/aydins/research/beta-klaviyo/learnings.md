# beta-klaviyo Cumulative Learnings


## 2026-06-08
### Actionable
- [Gmail says your unsubscribe "Needs work"](https://www.wordtothewise.com/2025/07/gmail-says-your-unsubscribe-needs-work/) - This directly addresses Gmail's 2024/2025 bulk sender requirements for one-click unsubscribe (RFC 8058), which is critical for inbox placement. **Action:** Audit Aydins' Klaviyo unsubscribe process immediately to ensure it's a single-step, RFC 8058-compliant link.
- [Stop using Entrust for your BIMI Certificates](https://www.wordtothewise.com/2024/12/stop-using-entrust-for-your-bimi-certificates/) - BIMI can improve brand trust and engagement, but using a distrusted certificate authority (Entrust) will cause BIMI to fail at Gmail. **Action:** If Aydins has or plans a BIMI setup, verify the VMC is not from Entrust and switch to a trusted provider like DigiCert or Sectigo.
- [The new DMARC is here](https://www.wordtothewise.com/2026/05/the-new-dmarc-is-here/) - DMARCbis (RFC 9989/9990) is an updated standard that may affect how authentication policies are interpreted by mailbox providers over time. **Action:** Review Aydins' current DMARC record and monitor for ESP/Klaviyo guidance on adopting the new standard to maintain compliance.

## 2026-06-08
### Actionable
- [Gmail says your unsubscribe "Needs work"](https://www.wordtothewise.com/2025/07/gmail-says-your-unsubscribe-needs-work/) - This directly addresses Gmail's 2024/2026 bulk sender requirements for a one-click unsubscribe, which is critical for Aydins' deliverability. **Action:** Audit your Klaviyo list-unsubscribe header implementation to ensure it's RFC 8058 compliant.
- [Stop using Entrust for your BIMI Certificates](https://www.wordtothewise.com/2024/12/stop-using-entrust-for-your-bimi-certificates/) - BIMI can improve brand trust and inbox placement, but using a distrusted certificate authority like Entrust will break the feature. **Action:** If Aydins has or plans to implement BIMI, verify the VMC is not from Entrust and switch providers if necessary.
- [Sendy and one-click unsubscribe](https://www.wordtothewise.com/2024/07/sendy-and-one-click-unsubscribe/) - While not about Sendy specifically, it highlights the critical importance of correctly implementing RFC 8058 one-click unsubscribe to meet Gmail/Yahoo mandates. **Action:** Confirm Klaviyo's one-click unsubscribe is functioning correctly for all campaigns, especially after the recent UTM fixes.
