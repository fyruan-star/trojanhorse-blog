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
 "Every relationship line was checked against its source on 23 October 2026. "
 "Lines whose source did not state the claim were reworded or removed, and "
 "relationships that were only my reading are not drawn. Some sources block "
 "automated reading, so for those the figures were confirmed through other "
 "coverage of the same event.",
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

GAPS.update({
 "foundation": [
  "CoWoS capacity is estimated, since TSMC does not disclose it. The Amkor agreements with TSMC and Nvidia come from one commentary source.",
  "Wafer data is thin. There is no SEMI 2026 shipment data and no GlobalWafers share. Lynas was not found, and gallium and germanium licensing was not verified.",
  "The claim that US magnet capacity will not be meaningful until 2028 is single-sourced, and the customer in MP's gadolinium offtake is not named.",
 ],
 "fintech": [
  "The Stripe and Advent proposal for PayPal is reported and no board response was found. Block's 2026 volume was not found.",
  "Nubank's and Revolut's customer counts and Revolut's valuation come from aggregators. Robinhood and Klarna were not found. GENIUS Act final rules were not confirmed.",
  "Stablecoin supply figures vary by source and date.",
 ],
 "mobility": [
  "Waymo's rides and fleet come from trackers, and Alphabet's own figure was not retrieved. Tesla's fleet figures are older and secondary. Mobileye and Nvidia automotive data were not found.",
  "BYD's lead over Tesla rests on third-party sales charts and not company filings. Fleet and city counts conflict across sources.",
 ],
 "robotics": [
  "Humanoid shipment counts, Tesla Optimus output and Figure's deployment are single-source or conflicting. Unitree's IPO was not confirmed. No funding figure was verified for Agility, Apptronik or 1X.",
  "Fanuc, Yaskawa, ABB and KUKA were not found for 2026. Amazon's robot count is a year old.",
  "No starter was verified for robot foundation models. Nvidia's and Google's robot models were not found.",
 ],
 "health": [
  "AI scribe and OpenEvidence valuations come from aggregators and conflict on dates. No usage share exists.",
  "Epic, Microsoft's Dragon Copilot, Hims and Hers, and Oracle Health were not researched.",
  "Insilico's Phase 3 start date is reported as July and as September. Recursion's trial stage conflicts.",
 ],
 "defense": [
  "SpaceX's 2026 launch count was not found and Starship's flight history conflicts across sources. Amazon Leo deployment totals were not found.",
  "Northrop Grumman, Shield AI's valuation, Golden Dome awards and European defense spending were not found. The authorization act's status is as of the source's date.",
 ],
 "quantum": [
  "Quantinuum's IPO valuation ranges from about $13bn to $15bn across sources, and IQM's and Infleqtion's listings come from aggregators.",
  "PsiQuantum's 2026 funding and Microsoft's Majorana update were not found. A reported reproduction of an IBM advantage claim is from a third-party tracker.",
 ],
 "energy": [
  "Sodium-ion and solid-state battery timelines were not found. Hitachi Energy was not found. Fluence's June deployment total was not retrieved.",
  "Fusion funding totals differ between trackers, and Commonwealth Fusion's raised total ranges from $2.9bn to $3.9bn. TAE's merger terms are single-sourced.",
 ],
})

NOT_YET = ("Not covered. The atlas holds nine sectors, chosen for what a Bay Area "
           "technology coverage banker or a tech M&A banker works on. Telecom, "
           "robotics, mobility, health technology, defense and space, quantum, "
           "energy technology and the materials foundation were researched and "
           "then removed. The companies are mostly American and Chinese, and "
           "Europe, India, Japan and Korea are thin outside the sectors where "
           "they lead.")
