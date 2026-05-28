# Google Ads API Tool — Design Documentation

**Applicant:** Aydins Jewelry
**Account ID requesting access:** 684-011-8076
**Account holder:** Amir Lakhani (lakhani.amir@yahoo.com)
**Document date:** 2026-05-27
**Tool name:** BETA Google (internal automation)

---

## 1. Purpose

BETA Google is a private internal automation tool built to help the owner of Aydins Jewelry (a single direct-to-consumer e-commerce business) monitor and optimize the operation of one Google Ads account (Customer ID 684-011-8076). The tool is not commercially offered, not made available to third parties, and not resold. It accesses only the account holder's own advertising data.

## 2. Business Context

Aydins Jewelry is a direct-to-consumer online jewelry retailer founded in 2011, selling men's wedding bands and custom-engraved rings at shopaydins.com. The business operates on the Shopify platform and uses Google Ads as its primary paid customer acquisition channel. Current monthly Google Ads spend is approximately $15,000 across Performance Max and Search campaigns.

Annual revenue: approximately $340,000. Single-location, single-owner business.

## 3. Use Case

The tool will be used by the account owner to:

- Pull daily campaign performance data (impressions, clicks, conversions, CPA, ROAS) for internal monitoring
- Cross-reference Google Ads conversion data against Google Analytics 4 and Google Merchant Center data to identify attribution gaps and feed quality issues
- Generate draft Responsive Search Ad asset variations and headline/description suggestions for manual review and approval before publishing
- Monitor spend pacing and flag anomalies including unexpected CPA spikes, Quality Score drops, and disapproved ads
- Audit Google Merchant Center feed health and identify products that are not eligible to serve

No third-party clients will use this tool. No data will be exposed to external services. No automated ad changes, budget changes, or campaign structure changes will be applied without explicit human approval from the account owner.

## 4. Architecture

```
[ Aydins Jewelry Google Ads Account ]
              |
              |  (read-only API calls)
              v
[ BETA Google Internal Tool on Linux VPS ]
              |
              +---> [ Local report files (mode 600) ]
              +---> [ Slack notification channel (owner only) ]
              +---> [ Internal Markdown digest for owner review ]
              |
              v
[ Account owner (Amir Lakhani) reviews and manually approves any proposed changes ]
              |
              v
[ Approved changes pushed back through Google Ads API ]
```

## 5. Hosting and Storage

- **Server:** Linux VPS, Ubuntu 24.04, located on Hetzner cloud (Germany), single-tenant
- **Access:** SSH key only (no password authentication), firewall open only to port 22 SSH
- **Credentials:** Stored in environment files with Unix permissions 0600 (readable only by the owner-controlled service account on the VPS)
- **Data retention:** API responses cached locally for at most 30 days for analysis purposes, never shared outside the owner's environment
- **Backups:** Daily file system backup, encrypted

## 6. Security

- API credentials (Developer Token, OAuth Refresh Token, Client Secret) are stored only on the VPS in mode 600 files, never logged, never echoed in code output, never transmitted to any third-party service.
- All API calls use the official Google Ads API endpoints over HTTPS.
- No customer personal data is collected, processed, or stored.
- No Google Ads data is shared, sold, or made available to any party outside the account owner.
- The tool does not allow login or access by any user other than the account owner.

## 7. Volume Estimates

- **Customer IDs managed:** 1 (Aydins Jewelry, 684-011-8076)
- **Expected daily API operations:** Under 500 (mostly campaign/ad group/keyword report queries)
- **Expected monthly API operations:** Under 15,000
- **Mutating operations expected:** Under 50 per month (ad copy edits, paused/enabled ads — only after manual owner approval)

## 8. Approval Gates and Safety

The tool implements a strict human-approval workflow for any change that affects ad serving or spend:

1. **Daily monitoring** runs automatically and produces a digest summary for the owner.
2. **Draft proposals** (ad copy, budget recommendations, pause/enable suggestions) are surfaced to the owner via Slack and email for manual review.
3. **No automatic spend, budget, or structural changes** are permitted. Every change passes through explicit owner approval before being applied via the API.
4. **Anomaly alerts** (spend over threshold, Quality Score drops, disapproved ads) trigger immediate owner notifications without any automatic remediation.

## 9. Third-Party Use Statement

This tool will not be used to:

- Provide Google Ads management services to other businesses
- Build a multi-tenant SaaS platform
- Resell or redistribute Google Ads data
- Aggregate competitive intelligence across multiple advertisers
- Build any consumer-facing application

This tool is a private, internal, single-account automation built and used exclusively by the Aydins Jewelry account owner.

## 10. Contact

- **Owner:** Amir Lakhani
- **Email:** lakhani.amir@yahoo.com
- **Account ID:** 684-011-8076
- **Business name:** Aydins Jewelry
- **Website:** https://shopaydins.com
- **Year founded:** 2011

End of design documentation.
