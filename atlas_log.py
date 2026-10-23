"""The research log for the Tech Atlas: what each sector rests on and what it does not."""

METHOD = [
 "Every figure on a card carries a period and a link. Sourced means a company "
 "filing or release, or a named research firm such as Dell'Oro, IDC, "
 "TrendForce, Counterpoint, Synergy or Nielsen. Reported means credible press "
 "or an industry tracker without the underlying document in hand. Inferred "
 "means the line or the badge is my reading of the structure and no source "
 "states it. The lines that say why a company leads and what could change the "
 "order are my reading of the evidence on each card.",
 "A starter is a company with a measurable lead in its row. A second-string "
 "player has shipping product or named customers. A practice-squad player is "
 "private or recently public, with a disclosed funding round or a named "
 "transaction. Where sources conflict on a figure, the card shows the range or "
 "says that the sources conflict, and a startup whose funding could not be "
 "confirmed was left off. Search summaries can paraphrase, so the figures "
 "above come from the cited pages and not from memory, and some pages could "
 "not be opened directly. Those are marked reported.",
]

# per sector: what was single-sourced or conflicting, and what was not found
GAPS = {
 "silicon": [
  "Estimates of Nvidia's share of AI accelerator revenue range from about 70% to over 80% and none comes from a primary breakdown.",
  "Cerebras's valuation sources conflict. SambaNova and Positron were left off because their funding reports conflict. Etched's later offers are unconfirmed.",
  "Not found: Arm's server share, SiFive's 2026 funding, the terms of the US government stake in Intel, and China's equipment localization rate.",
  "Counterpoint and IDC rank the DRAM leaders differently, and the card shows both.",
 ],
 "infra": [
  "No audited AI storage share exists. DDN's 2026 revenue was not found. VAST's recurring revenue is company-reported.",
  "Vertiv's backlog figures conflict between two reports. Schneider Electric was not found. Lightmatter and Enfabrica were not verified.",
  "Stargate's live capacity differs between trackers, from 0.3 GW to 618 MW at Abilene, so it is not charted.",
  "CBRE and JLL vacancy data for 2026 were not found.",
 ],
 "cloud": [
  "Synergy's shares come through secondary coverage, and one outlier source disagrees. Alibaba, Huawei and Tencent shares were not found.",
  "Google and Microsoft backlogs and growth rates come from secondary coverage of their reports. The primary releases were not retrieved.",
  "Baseten's and Modal's valuations conflict. Lambda's current valuation was not found.",
 ],
 "models": [
  "Valuations and revenue run rates come from news coverage and aggregators, except where a firm or CNBC is cited. Totals raised by Anthropic and OpenAI conflict between sources.",
  "Thinking Machines' 2026 valuation is unresolved, and no 2026 Perplexity round was found.",
  "Meta AI's user count differs from 640 million to 1.5 billion and none is Meta-confirmed. DeepSeek's developer share is from one source.",
  "No 2026 update to the Menlo enterprise survey was found. The figures are from late 2025.",
 ],
 "software": [
  "The size of the February selloff is commentary, and estimates run from $285bn to $2tn.",
  "Microsoft's July Copilot seat count and GitHub Copilot's 50 million users rest on one report of the earnings call.",
  "Atlassian, GitLab and Dynatrace were not found. No Databricks IPO filing was found. Salesforce's latest Agentforce figure is secondary.",
 ],
 "security": [
  "One outlier report of CrowdStrike's quarter conflicts with the company release and was not used.",
  "Wiz's $1bn ARR is from one trade outlet. Microsoft's security revenue, Chainguard and Abnormal were not found. No CNAPP market share figure was found.",
  "Cyera's round size differs between two sources.",
 ],
 "internet": [
  "Nielsen's September Gauge had not been published. Search share is StatCounter referral traffic and not searches.",
  "Advertising revenue for Google, Meta, Amazon and YouTube comes from secondary summaries of earnings.",
  "Not found: Microsoft, Sony and Nintendo gaming data, the Electronic Arts take-private terms, Temu and Shein shares, and Instagram's user count.",
 ],
 "devices": [
  "Xiaomi's share differs between sources, and the OPPO and vivo declines come from one IDC-based table.",
  "Gartner's PC figures, Apple's Vision Pro sales and Apple's glasses plans were not found. Meta's glasses share runs from 69% to 76%.",
 ],
 "telecom": [
  "Not verified: T-Mobile's 2026 results, Verizon's third quarter (due 26 October), Akamai, Amazon Leo, AST SpaceMobile and the EchoStar spectrum deal.",
  "Nokia's AI radio work with Nvidia was not verified. SpaceX's AI revenue is from secondary coverage of its first results as a listed company.",
 ],
}

NOT_YET = ("Not charted yet. The Phase 2 sectors are the foundation (materials and "
           "other inputs), fintech and payments, mobility and autonomy, robotics, "
           "health technology, defense and space, quantum computing, and energy "
           "technology. Some of their companies appear here because they connect "
           "to Phase 1 sectors, such as the nuclear developers, SpaceX and "
           "Rapidus.")
