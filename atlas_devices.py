"""Tech Atlas, sector 8: Devices."""

ENT = {
 "xiaomi": ("Xiaomi", "Smartphones, devices and electric cars."),
 "oppo": ("OPPO", "Smartphones."),
 "vivo": ("vivo", "Smartphones."),
 "hp": ("HP", "PCs and printers."),
 "essilor": ("EssilorLuxottica", "Eyewear maker that builds Meta's Ray-Ban and Oakley glasses."),
}

SECTOR = dict(
 id="devices", name="Devices", band="end",
 blurb="The phones, laptops and glasses people carry, all squeezed by the same memory shortage.",
 positions=[

  dict(id="phones", name="Smartphones",
   metric=("Q2 2026 shipments of 276.3 million, down 7.4% (IDC). Samsung 62.7m and 22.7% share, Apple 55.7m and 20.2%, Xiaomi about 11.3%, OPPO 10.4%, vivo 7.6%. IDC expects 2026 shipments to fall 16.7% to just over 1bn, the steepest annual drop on record."),
   metric_src="https://www.biztechreports.com/news-archive/2026/8/6/global-smartphone-shipments-fall-67-in-q2-2026-as-the-memory-crisis-splits-the-market-in-two-idc-august-11-2026",
   players=[
    dict(e="samsung", t="starter", stat="62.7m units and 22.7% share in Q2 2026, up about 8%.",
     why="Sells across every price band and makes its own memory.", cond="Memory costs are raising phone prices (IDC: average price up 27.6%).",
     src="https://www.biztechreports.com/news-archive/2026/8/6/global-smartphone-shipments-fall-67-in-q2-2026-as-the-memory-crisis-splits-the-market-in-two-idc-august-11-2026"),
    dict(e="apple", t="starter", stat="55.7m units and 20.2% share in Q2 2026, up about 15%. Samsung and Apple were the only top-five vendors that grew.",
     why="Premium buyers keep buying as prices rise.", cond="Component costs.",
     src="https://www.biztechreports.com/news-archive/2026/8/6/global-smartphone-shipments-fall-67-in-q2-2026-as-the-memory-crisis-splits-the-market-in-two-idc-august-11-2026"),
    dict(e="xiaomi", t="second", conf="reported", stat="About 11.2% to 11.3% share, with the steepest decline among the top vendors (down 26.3% in one IDC-based table).",
     why="Value-priced phones are hit hardest by memory prices.", cond="Sources differ on its exact share.",
     src="https://www.threads.com/@boxtobyte/post/Dax5DUqmYtL/idc-announced-smartphone-shipments-in-the-global-market-in-q-samsung-share/"),
    dict(e="oppo", t="second", conf="reported", stat="10.4% share, down 17.5% (IDC-based table).", why="Large presence in Asia.", cond="Memory costs.",
     src="https://www.threads.com/@boxtobyte/post/Dax5DUqmYtL/idc-announced-smartphone-shipments-in-the-global-market-in-q-samsung-share/"),
    dict(e="vivo", t="second", conf="reported", stat="7.6% share, down 19.4% (IDC-based table).", why="Large presence in Asia.", cond="Memory costs.",
     src="https://www.threads.com/@boxtobyte/post/Dax5DUqmYtL/idc-announced-smartphone-shipments-in-the-global-market-in-q-samsung-share/"),
   ]),

  dict(id="pcs", name="PCs",
   metric=("Q2 2026 PC shipments of 68.2 million, down 4.9% (IDC). Lenovo 24.4%, HP 19.1%, Dell 13.6% and Apple 9.9%. Counterpoint puts the decline at 4%, and IDC expects the DRAM shortage to last into early 2028."),
   metric_src="https://www.mactrast.com/2026/07/idc-apple-the-only-major-computer-maker-to-increase-shipments-in-q2-2026/",
   players=[
    dict(e="lenovo", t="starter", stat="24.4% share, shipments down 2.1% (IDC).", why="Scale and a wide range.", cond="Memory costs.",
     src="https://www.mactrast.com/2026/07/idc-apple-the-only-major-computer-maker-to-increase-shipments-in-q2-2026/"),
    dict(e="hp", t="starter", stat="19.1% share, shipments down 9% (IDC).", why="Commercial and consumer base.", cond="Memory costs.",
     src="https://www.mactrast.com/2026/07/idc-apple-the-only-major-computer-maker-to-increase-shipments-in-q2-2026/"),
    dict(e="dell", t="starter", stat="13.6% share, shipments down 5% (IDC).", why="Enterprise customers.", cond="Server business is now the bigger growth story.",
     src="https://www.mactrast.com/2026/07/idc-apple-the-only-major-computer-maker-to-increase-shipments-in-q2-2026/"),
    dict(e="apple", t="second", stat="6.7 million Macs and 9.9% share in Q2 2026, up about 10% (IDC), the only major maker to grow. IDC credits the MacBook Neo launch in part.",
     why="Rising while the rest of the market falls.", cond="Whether the new low-price Mac holds its volume as memory costs rise.",
     src="https://www.mactrast.com/2026/07/idc-apple-the-only-major-computer-maker-to-increase-shipments-in-q2-2026/"),
   ]),

  dict(id="wearables", name="Smart glasses and XR",
   metric=("XR and smart glasses shipments grew about 35% in Q2 2026 (IDC), down from 130% in the prior quarter. Glasses are nearly 85% of XR shipments and headsets about 15%. Meta's share of smart glasses is put at 69% to 76% depending on the source."),
   metric_src="https://mixed-news.com/en/idc-smart-glasses-shipments-q2-2026-vr-headsets-decline/",
   players=[
    dict(e="meta", t="starter", conf="reported",
     stat="Share of smart glasses reported at 69.2% in Q1 2026 and 76.1% in another IDC citation. Ray-Ban Display's international rollout was paused because US availability was backlogged. A $299 display-free line launched 23 June 2026.",
     why="Sells glasses through eyewear stores, not as a headset.", cond="Display glasses are supply constrained.",
     src="https://www.idc.com/resource-center/blog/smart-glasses-growth-cools-to-35-as-meta-doubles-down-on-distribution/"),
    dict(e="essilor", t="starter",
     stat="Sold over 7 million Ray-Ban and Oakley Meta glasses in 2025. First-half 2026 revenue from Meta glasses nearly doubled.",
     why="Makes the frames and owns the retail.", cond="Depends on one platform partner.",
     src="https://basic-tutorials.com/news/smart-glasses-are-booming-sales-of-meta-glasses-have-nearly-doubled/"),
    dict(e="google", t="second", conf="reported", stat="Google and Samsung plan Android XR glasses, starting with an audio-led model in fall 2026. No confirmed launch date or price.",
     why="Brings an operating system and Gemini to the category.", cond="Shipping a product people buy.",
     src="https://dymesty.com/blogs/articles/smart-glasses-release-calendar-2026"),
   ]),
 ])

EDGES = [
 dict(a="essilor", b="meta", type="alliance", text="Builds and sells Ray-Ban and Oakley Meta glasses, over 7 million in 2025.", src="https://basic-tutorials.com/news/smart-glasses-are-booming-sales-of-meta-glasses-have-nearly-doubled/", date="2026", conf="reported"),
 dict(a="google", b="samsung", type="alliance", text="Planned Android XR glasses.", src="https://dymesty.com/blogs/articles/smart-glasses-release-calendar-2026", date="2026", conf="reported"),
 dict(a="samsung", b="apple", type="rivalry", text="First and second in Q2 2026 phone shipments, 62.7m against 55.7m.", src="https://www.biztechreports.com/news-archive/2026/8/6/global-smartphone-shipments-fall-67-in-q2-2026-as-the-memory-crisis-splits-the-market-in-two-idc-august-11-2026", date="2026-Q2", conf="reported"),
 dict(a="lenovo", b="hp", type="rivalry", text="First and second in Q2 2026 PC shipments, 24.4% against 19.1% (IDC).", src="https://www.mactrast.com/2026/07/idc-apple-the-only-major-computer-maker-to-increase-shipments-in-q2-2026/", date="2026-Q2", conf="reported"),
 dict(a="apple", b="lenovo", type="rivalry", text="Apple's Mac shipments rose about 10% while Lenovo's fell 2.1%.", src="https://www.mactrast.com/2026/07/idc-apple-the-only-major-computer-maker-to-increase-shipments-in-q2-2026/", date="2026-Q2", conf="reported"),
 dict(a="sk_hynix", b="samsung", type="dependency", text="A DRAM shortage is raising device prices and cutting phone and PC shipments (IDC).", src="https://www.biztechreports.com/news-archive/2026/8/6/global-smartphone-shipments-fall-67-in-q2-2026-as-the-memory-crisis-splits-the-market-in-two-idc-august-11-2026", date="2026", conf="reported"),
 dict(a="micron", b="apple", type="dependency", text="Memory cost increases hit Apple, Xiaomi and PC makers alike. IDC expects the shortage to last into early 2028.", src="https://www.mactrast.com/2026/07/idc-apple-the-only-major-computer-maker-to-increase-shipments-in-q2-2026/", date="2026", conf="reported"),
]
