"""Trojan Horse of the Week: The Hourglass, a fable by Francis Ruan.

Posted 4 November 2026 from the owner's own text. Four short passages were
added at his request to show the Anthropic IPO inside the fable without naming
it: the prospectus proof on the desk, the paper loss going into the
prospectus, Tom's margin sentence for the bankers, and the bound prospectus at
the end. One semicolon in Part III became a full stop (house rule).

Every claim in Behind the fable was checked on 4 November 2026: the S-1 text on
SEC EDGAR (cost per task, margins, each Claude helping build the next), Fortune
on the S-1 losses, Axios on the three-week lead (Innovation Endeavors report),
philippdubach on Amodei's model-as-company example, Epoch AI on 2.4x a year,
Bloomberg Law and Axios on Sacks and Anthropic's reply, Caixin on DeepSeek,
SiliconANGLE on Huang. The Altman epigraph is from reporters' accounts of a
2025 dinner, with no transcript. The leodex link for Huang was replaced by
SiliconANGLE, and a link was added for Anthropic's reply to Sacks.

This story is longer than the 1,200-word cap because it is the owner's own
fable, posted whole at his request.
"""

WEEK = "4 November 2026"
SLUG = "the-hourglass"
KICKER = "Trojan Horse of the Week"
TITLE = "The Hourglass"
HOOK = ("A family of engine builders gets three wishes from an hourglass in the "
        "autumn their works sells shares, and each wish lasts exactly as long as "
        "it takes a rival to copy it.")
LOGO = {"file": "anthropic.svg", "w": 24, "h": 24, "name": "Anthropic", "height": 34}
GO = ("attention-revolt.html",
      "The previous Trojan horse: Tech Induced Dopamine Revolution &rarr;")

SECTIONS = [

 ('Part I', [
  '<em>&ldquo;Essentially very expensive sandcastles.&rdquo;</em> (<a href="https://officechai.com/ai/proprietary-frontier-ai-models-are-very-expensive-sandcastles-francois-chollet/">François Chollet</a>)',
  'Without, the rain came sideways off the river, but in the long front room of Ashgrove House the curtains were drawn and the fire was high. The house stood so near the Hale Calculating Works that its windows trembled whenever the great engine ran. The two brothers were at chess. Arthur, the elder, played as he did everything, boldly and a little too soon. Tom, four years younger, played as if he had already seen the end and was only waiting politely for his brother to arrive at it.',
  '&ldquo;You&rsquo;ve left your queen,&rdquo; said Tom.',
  '&ldquo;I&rsquo;ve left her on purpose.&rdquo;',
  '&ldquo;Then you&rsquo;ve lost her on purpose.&rdquo; Tom took it. Arthur frowned at the board for a long moment, saw the trap he had walked into, saw also how he might have avoided it, and set the pieces up to play again. Their mother, knitting by the fire, remarked that Tom had been sharpening his brother this way since they were children, and that Arthur was the better for it, though he would never say so.',
  'At the desk by the window their father sat with the ledger open and did not look up. Mr. Edmund Hale had built the finest thinking-engine in the county. It had taken him a year and very nearly everything he owned. It had been the finest engine in the county for three weeks.',
  'Beside the ledger lay a proof from the printers, still smelling of ink: the prospectus for the shares the Hale Works would offer on the Exchange in the last week of November. Every figure in it had to be true, and every figure in it would be read by strangers.',
  '&ldquo;Fenwick&rsquo;s showed their new one at the Exchange today,&rdquo; he said at last, to nobody. &ldquo;Faster than ours. Cheaper to run, they say.&rdquo;',
  '&ldquo;It&rsquo;s dodge-ball, father,&rdquo; said Arthur, still frowning at the board. &ldquo;Whoever picks up the ball throws it. There&rsquo;s no rule about waiting.&rdquo;',
  '&ldquo;There&rsquo;s no rule about anything,&rdquo; said Mr. Hale.',
  'Beneath them the engine was working. They felt it more than heard it, a steady tremor in the floorboards. It held, Tom liked to tell visitors, two thousand thousand little brass drawers, and in every drawer a single number. To teach it, you read it a book of fairy tales one word at a time and asked it to guess the next. It would guess &ldquo;tree&rdquo; when the word was &ldquo;once,&rdquo; and you would tell it how far it had missed, and it would open every drawer and change every number by a hair, and guess again. Do that ten million times and it could write a letter to the Board of Trade. Do it with more drawers, as Fenwick&rsquo;s had, and it could write a better one.',
  '&ldquo;There&rsquo;s Crane,&rdquo; said Tom, as the gate clanged and heavy boots came up the path.',
  'Mr. Crane of the Crane Foundry was a large, prosperous, weathered man who carried the cold in with him and seemed to enjoy it. Every thinking-engine in England, Hale&rsquo;s and Fenwick&rsquo;s included, was built upon the slates his foundry baked. &ldquo;You fellows put on the sauce and the toppings,&rdquo; he liked to say, &ldquo;but it is my bread, and it is my oven.&rdquo; He was the only man in the room who had done well out of every engine ever made, and it showed in his waistcoat.',
  'At the second glass he grew talkative. At the third he grew quiet, fumbled in his coat, and set something on the table among the chessmen.',
  'It was a small hourglass of dark glass in a frame of tarnished brass. The sand in it was running, though nobody had turned it.',
  '&ldquo;What&rsquo;s that, then?&rdquo; said Arthur.',
  '&ldquo;Nothing worth the telling,&rdquo; said Crane. Then he told it anyway. An old clockmaker in Zurich had made it, a man who wished to prove that the market ruled men&rsquo;s lives, and that those who tried to cheat it did so to their sorrow. He had put a working on the glass so that three men might each have three wishes from it.',
  '&ldquo;And you&rsquo;ve had yours?&rdquo; said Tom.',
  'Crane looked at the younger son the way a man long in business looks at a boy who is not. &ldquo;I have,&rdquo; he said, and his florid face went the colour of chalk.',
  '&ldquo;And the man before you?&rdquo;',
  '&ldquo;I don&rsquo;t know what his first two were. His third was to be done with business altogether. That&rsquo;s how the glass came to me.&rdquo; And before anyone could stop him, he tossed it into the fire.',
  'Mr. Hale was out of his chair in an instant and had it back again, burning his fingers.',
  '&ldquo;Better let it melt,&rdquo; said Crane.',
  '&ldquo;If you don&rsquo;t want it, give it to me.&rdquo;',
  '&ldquo;I won&rsquo;t sell it to you. I threw it on the fire. If you keep it, Hale, don&rsquo;t blame me for what comes.&rdquo; He took up his hat. &ldquo;Hold it in your right hand and say your wish aloud. But wish for something sensible.&rdquo;',
  'When he had gone, Mrs. Hale said that if the thing granted wishes she would like the engine to stop rattling her teacups, and Arthur laughed, and Mr. Hale did not.',
  '&ldquo;I don&rsquo;t know what to wish for,&rdquo; he said slowly. &ldquo;That&rsquo;s the truth of it. I only want the engine to pay for itself.&rdquo;',
  '&ldquo;Then wish that,&rdquo; said Arthur.',
  'Mr. Hale held up the glass in his right hand. &ldquo;I wish,&rdquo; he said distinctly, &ldquo;that my engine would pay for itself.&rdquo;',
  'The sand stopped. For one long moment it hung in the neck as if it were thinking. Then it began to fall upward.',
  'Mr. Hale gave a cry and dropped it on the hearthrug, where it lay with its sand running the right way again, small and ordinary.',
  '&ldquo;It&rsquo;s your fancy, Edmund,&rdquo; said his wife.',
  '&ldquo;Perhaps,&rdquo; said he. But nobody moved to pick it up, and long after the brothers had gone to bed, Tom lay awake listening to the engine in the floor, and to the rain, and to something he could not name that sounded very much like sand.',
 ]),

 ('Part II', [
  '<em>&ldquo;If we didn&rsquo;t pay for training, we&rsquo;d be a very profitable company.&rdquo;</em> (<a href="https://simonwillison.net/2025/Aug/17/sam-altman/">Sam Altman</a>)',
  'In the morning, under a thin winter sun, the glass looked like what it was, a curio on the mantel, and everyone laughed about it at breakfast.',
  'At ten o&rsquo;clock the post came. The first letter was from the accountants. The engine, they wrote with evident surprise, had earned twice what it had cost. Mr. Hale read the figure aloud twice and sat down heavily, and his wife kissed him, and Arthur whooped.',
  'The second letter was from the Crane Foundry. It was the bill for the slates of the next engine, which Arthur had ordered the week before so as not to fall behind Fenwick&rsquo;s. It was ten times the size of the first.',
  '&ldquo;Well,&rdquo; said Mr. Hale, after a silence. &ldquo;It paid for itself.&rdquo;',
  '&ldquo;It paid for itself,&rdquo; said Tom, &ldquo;and then the next one ate it.&rdquo; He held the accountants&rsquo; letter up to the window. &ldquo;And look at the bottom. They&rsquo;ve written us down for a loss so large I can&rsquo;t say it out loud.&rdquo;',
  'His father went grey.',
  'But Tom kept reading, and after a while he began, very quietly, to laugh. &ldquo;It&rsquo;s paper,&rdquo; he said. &ldquo;Nearly all of it. It&rsquo;s the notes we signed with the bank. The works is worth more than it was, so the notes are worth more, and the rules say that must be written down as a loss. The ugliest number in the letter is a disguise. The engine itself lost almost nothing.&rdquo;',
  '&ldquo;And that number goes in the prospectus,&rdquo; said Mr. Hale. &ldquo;Strangers will read it on the Exchange.&rdquo;',
  '&ldquo;The careless ones will read the big number,&rdquo; said Tom. &ldquo;The careful ones will read the line beneath it, and the line beneath it says the engine pays.&rdquo;',
  '&ldquo;Then why do I feel poorer?&rdquo; said Mr. Hale.',
  '&ldquo;Because you have one engine that pays and another that hasn&rsquo;t been built,&rdquo; said Tom, &ldquo;and Fenwick&rsquo;s will show theirs before yours is done.&rdquo;',
  'That evening, with the curtains drawn, Mr. Hale took the glass from the mantel without a word to anyone and held it in his right hand.',
  '&ldquo;I wish for time,&rdquo; he said. &ldquo;I wish that no engine may be shown in England until the one before it has had a full season to earn its keep.&rdquo;',
  'The sand stopped, and hung, and fell upward, and righted itself.',
  'The Engine Review Act passed in the spring. Every new engine would wait six months before it could be shown. The papers called it prudent. One columnist called it a cunning bit of capture by the men who had already built their engines, and Arthur cut the column out, pinned it over his desk, and laughed at it. For three months the Hale works ran day and night, and the ledger turned black.',
  'In the fourth month a ship came up the river from across the sea. It carried an engine built by men who had never heard of the Engine Review Act and did not care to. It was nearly as good as Hale&rsquo;s. It was a quarter of the price. By midsummer half the orders on Mr. Hale&rsquo;s desk had been cancelled, and the rest were asking for a discount.',
  '&ldquo;You stopped the game,&rdquo; said Arthur bitterly, &ldquo;and only our side of the yard stopped playing.&rdquo;',
 ]),

 ('Part III', [
  '<em>&ldquo;Our compute efficiency allows us to deliver these reductions while preserving our margins.&rdquo;</em> (<a href="https://www.sec.gov/Archives/edgar/data/0002130357/000162828026067168/anthropicpbc-sx1.htm">Anthropic, Form S-1</a>)',
  'It was Arthur who took the glass down the third time. He stood with it in the firelight, his jaw set, and said he would wish every foreign engine at the bottom of the sea.',
  'Tom caught his wrist.',
  '&ldquo;You&rsquo;ve had two wishes,&rdquo; he said, &ldquo;and both times you wished for the world to change. Money, then time. The glass gave you both, and the world took them back. Wish for the engine to change instead.&rdquo;',
  '&ldquo;Into what?&rdquo;',
  'Tom took a pencil from his pocket and wrote 1 + 1 in the margin of the newspaper. &ldquo;Ask our engine that, and it thinks for fifty steps before it says two. Every step burns coal, and every step wears the slates. Fenwick&rsquo;s takes forty. The foreigners take sixty, though they charge so little you&rsquo;d never notice.&rdquo; He looked up. &ldquo;Set a third-form boy and a scholar from the university the same hard sum. The boy takes three weeks. The scholar takes an afternoon and eats a biscuit. You pay the scholar more, and the scholar costs less. That difference is everything we&rsquo;re fighting over.&rdquo;',
  'His father understood him slowly, and then all at once.',
  '&ldquo;The customer pays for the answer,&rdquo; said Mr. Hale.',
  '&ldquo;Not for the thinking,&rdquo; said Tom. &ldquo;So make the thinking shorter, and keep the difference. They&rsquo;ll call it a gift: a faster, cheaper answer. They&rsquo;ll never ask what&rsquo;s inside it.&rdquo;',
  'Mr. Hale took the glass from Arthur. His hand was quite steady.',
  '&ldquo;I wish,&rdquo; he said, &ldquo;that my engine might always know the shortest road to its answer.&rdquo;',
  'The sand stopped. It hung in the neck for so long that Mrs. Hale put down her knitting. Then it fell upward, all of it, every grain, and did not right itself again.',
  'The change was not dramatic. In the morning the engine simply ran quieter. By the end of the week it was answering in ten steps what had taken fifty, and Mr. Hale, who had always been a fair man, cut his price by a little and kept the rest. The customers wrote to thank him. Crane&rsquo;s foundry sold him fewer slates that quarter. Crane came to dinner and was gracious about it, and looked several times at the empty glass on the mantel, and did not mention it.',
  'Tom wrote a sentence about it for the prospectus, that the works could make its answers cheaper and keep its profit, and the bankers underlined it twice.',
  'And the engine, which now knew the shortest road, began to help them build the next one. Tom drew the plans and the engine corrected them. The engine proposed and Tom checked. Each new engine came out sharper than the last, the way Arthur had come out of a thousand games of chess sharper than he went in. The younger was sharpening the elder now. Tom said that if it went on long enough, there might be no end to how sharp an engine could get.',
  'It was a fortnight before the first of the cancelled customers came back, and only three weeks after that when Arthur came in from the Exchange with his hat still on.',
  '&ldquo;Fenwick&rsquo;s,&rdquo; he said. &ldquo;They&rsquo;ve found the shortest road too. And the foreigners. Everyone has.&rdquo;',
  'Nobody spoke. The engine trembled in the floor.',
  '&ldquo;It doesn&rsquo;t matter how clever the scholar is,&rdquo; said Tom at last, &ldquo;once the whole class has graduated.&rdquo;',
  'The prospectus lay on the desk, printed and bound, with the shares to be offered in a fortnight. Tom&rsquo;s sentence was still on the first page. Every word of it was true, and now it was true of Fenwick&rsquo;s as well.',
  'Mr. Hale went to the mantel and picked up the hourglass. The sand was running again, though nobody had turned it, and it seemed to him that it ran faster than before. He understood then what the clockmaker in Zurich had built. The glass had never granted time. It had only ever shown a man how much he had left.',
  'He turned it over. It made no difference.',
  'Across the river, the lamps of Fenwick&rsquo;s works burned steady in the dark, and somewhere beneath them a new engine was already learning the way.',
 ]),

 ('Behind the fable', [
  'Every turn in the story has a real counterpart from 2025 and 2026.',
  '<strong>Three weeks at the top.</strong> New models typically <a href="https://www.axios.com/2025/06/25/ai-models-development-speed-growth">lead the usage charts for about three weeks</a> before newcomers and open-source rivals take over.',
  '<strong>The engine that paid for itself.</strong> Dario Amodei has argued that each model, taken as its own business, <a href="https://philippdubach.com/posts/ai-models-as-standalone-pls/">earns back its training cost</a>, roughly $100 million in and $200 million out. The loss comes from funding the next model, which costs far more. Epoch AI finds frontier training costs <a href="https://epoch.ai/blog/how-much-does-it-cost-to-train-frontier-ai-models">growing about 2.4x a year</a>.',
  '<strong>The paper loss.</strong> Anthropic&rsquo;s S-1 reports an $80.7 billion net loss for the first half of 2026, of which <a href="https://fortune.com/2026/10/26/anthropics-s-1/">$72.4 billion is a non-cash charge</a> on convertible notes. The operating loss was $693 million.',
  '<strong>The wish for time.</strong> Critics, including White House AI adviser David Sacks, have accused Anthropic of using safety regulation as <a href="https://news.bloomberglaw.com/artificial-intelligence/anthropic-is-running-a-strategy-based-on-fear-mongering-sacks">regulatory capture</a>. Anthropic <a href="https://www.axios.com/2025/10/21/anthropic-ai-czar-white-house-david-sacks-jd-vance">disputes this</a>.',
  '<strong>The ship from across the sea.</strong> In May, DeepSeek <a href="https://www.caixinglobal.com/2026-05-25/deepseek-cuts-flagship-ai-model-prices-by-75-as-funding-round-looms-102447441.html">permanently cut its flagship&rsquo;s price by 75%</a>, to a fraction of GPT-5.5&rsquo;s.',
  '<strong>The shortest road.</strong> Anthropic&rsquo;s <a href="https://www.sec.gov/Archives/edgar/data/0002130357/000162828026067168/anthropicpbc-sx1.htm">S-1</a> says Claude Opus 5.5 cut customer costs per task by about 40% while preserving margins. The same filing describes each Claude model helping to build the next.',
  '<strong>The foundry.</strong> Nvidia&rsquo;s Jensen Huang says <a href="https://siliconangle.com/2026/05/21/five-takeaways-nvidias-earnings-mean-ai-industry/">tokens are now profitable</a> for model makers, who are racing to produce more of them.',
 ]),
]

NOTE = ("A fable. The Hale family, Ashgrove House, the Crane Foundry and "
        "Fenwick&rsquo;s are invented. The epigraphs and every figure in Behind the "
        "fable were checked against their sources on 4 November 2026. The Altman "
        "line comes from reporters&rsquo; accounts of a 2025 dinner, and I found no "
        "transcript.")
