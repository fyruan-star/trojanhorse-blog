"""Trojan Horse of the Week: the revolt against the fast hit.

Written 3 November 2026 to the owner's brief, in diary mode (docs/STORY_PROMPT.md):
half first-person essay, half reporting on what companies are doing. One point:
every company is racing to make content faster to consume, and inside that race
rides a customer who will pay to slow down. Predictions are labelled.

The owner's premise that average YouTube upload length is falling is not
supported by any dataset found. What the data shows is that views have moved to
videos under a minute and that time spent per view has fallen, so the story says
that instead.

Sources read: Tubular Labs data via TVREV. Metricool's 2026 YouTube study.
Rozado, Hughes and Halberstadt in PLOS ONE (2022). Pew on Google AI summaries
(2025) and on teens and phones (April 2025). 9to5Mac on Apple's EU filing for
Huxe. Tech.eu on Kortext and StudyStash. TechCrunch on HBO Max Shorts. NEA
summary of NAEP reading-for-fun data. Ballotpedia on state phone bans. Brick's
Business Wire release. Publishers Weekly on Circana BookScan.

No em dashes, no semicolons, no rhetorical questions, no sub-description.
"""

WEEK = "3 November 2026"
SLUG = "attention-revolt"
KICKER = "Trojan Horse of the Week"
TITLE = "Tech Induced Dopamine Revolution"
HOOK = ("The average YouTube Short in one study of 800,000 videos held its viewer "
        "for 16 seconds, and the companies racing to shorten everything else are "
        "building the market for slowness.")
LOGO = {"file": "youtube.svg", "w": 90, "h": 20, "name": "YouTube", "height": 26}
GO = ("personalized-health.html",
      "The previous Trojan horse: Peptides Inject Their Way Into Tech &rarr;")

TUBULAR = ("https://www.tvrev.com/news/tube-trends-over-75-of-youtube-views-came-"
           "from-shorts-in-2025-tubular")
METRICOOL = "https://metricool.com/youtube-trends/"
HEADLINES = "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0276367"
PEW_AI = ("https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-"
          "likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/")
HUXE = "https://9to5mac.com/?p=1073521"
STUDYSTASH = ("https://tech.eu/2026/10/02/ai-study-platform-studystash-acquired-by-"
              "kortext-after-rapid-global-expansion/")
HBO = "https://techcrunch.com/2026/07/28/hbo-max-embraces-vertical-video-with-a-new-shorts-feed/"
NAEP = "https://www.arts.gov/stories/blog/2024/federal-data-reading-pleasure-all-signs-show-slump"
PEW_TEENS = "https://www.pewresearch.org/internet/2025/04/22/teens-social-media-and-mental-health/"
BANS = ("https://news.ballotpedia.org/2026/03/26/kansas-becomes-thirty-third-state-"
        "to-enact-a-k-12-cellphone-ban/")
BRICK = ("https://finance.yahoo.com/technology/articles/brick-launches-brick-night-"
         "automatically-163000194.html")
BOOKS = ("https://www.publishersweekly.com/pw/by-topic/industry-news/financial-"
         "reporting/article/101512-print-sales-stay-flat-through-september.html")

SECTIONS = [

 ("", [
  "Open YouTube and count how long you stay on one thing. A Short, then another, "
  "then a thumbnail of a shocked face beside a red arrow. The interesting "
  "question is what you would pay to stop.",

  "Lately I want to smash my phone. I want an older kind of day, one book and an "
  "afternoon with nothing pinging, and the peace I remember feeling at the end "
  "of it. I think a lot of people share that feeling, and the companies that "
  "caused it will be the ones that end up selling to it.",

  "My argument is that the race to make everything faster is consumer "
  "tech&rsquo;s Trojan horse. Users welcome the shortcut as a gift of time, and "
  "companies buy it because nobody wants to be the slower hit. Inside it rides a "
  "customer who is worn out by the shortcut, and that customer will pay to slow "
  "down.",
 ]),

 ("Everything is getting shorter", [
  "Videos under a minute drew 77% of global YouTube views in 2025, according to "
  f"<a href=\"{TUBULAR}\">Tubular Labs</a>, and videos of 20 minutes or more fell "
  "from 6.98% of views in 2023 to 4.08% in 2025. Attention is shrinking inside each "
  f"view too. In <a href=\"{METRICOOL}\">Metricool&rsquo;s study</a> of 799,718 "
  "videos, the average Short held its viewer for about 16 seconds, down from "
  "about 48 a year earlier, and the average view of a long video fell from 3.98 "
  "minutes to 2.51.",

  "When the click lasts less, the headline has to work harder to win it. A "
  f"<a href=\"{HEADLINES}\">study of 23 million headlines</a> from 47 American "
  "outlets found that headlines signalling anger rose 104% between 2000 and "
  "2019, and those signalling fear rose 150%. I feel that pull every time I open "
  "an app, and a feed tuned for anger and fear is tuned for a short stay.",
 ]),

 ("The deals are buying the shortcut", [
  "Every deal I found from the last six months buys compression. In June, Apple "
  "agreed to make job offers to members of Huxe and take a license to its "
  f"technology, according to an EU filing <a href=\"{HUXE}\">reported by "
  "9to5Mac</a> in October. Huxe was founded by the people behind Google&rsquo;s "
  "NotebookLM, and it turned a user&rsquo;s email and calendar into a daily "
  "audio briefing. It raised $4.6 million and shut down in May. Apple went "
  "after the team that turns a morning of reading into one listen.",

  f"On 2 October, Kortext <a href=\"{STUDYSTASH}\">bought StudyStash</a>, which "
  "turns course material into flashcards, practice tests and podcasts for "
  "students at more than 160 institutions. In July, HBO Max "
  f"<a href=\"{HBO}\">began testing a Shorts feed</a> of clips from its library, joining "
  "Netflix, Disney+ and Peacock, which already have vertical feeds. A streamer "
  "built on two-hour films now offers two-minute clips because every rival "
  "does.",

  "The summary is winning search as well. When Google showed an AI summary, users "
  f"clicked through to a link on <a href=\"{PEW_AI}\">8% of visits</a>, against "
  "15% without one, Pew found. The answer arrives, and fewer people read what sits underneath.",
 ]),

 ("It lands hardest in school", [
  f"Only <a href=\"{NAEP}\">14% of 13-year-olds</a> read for fun almost every day "
  "in 2023, down from 27% in 2012, according to federal NAEP data. Tools like "
  "StudyStash will help those students pass the quiz, and I think that is a real "
  "gain. My worry is the skill underneath it, the hour spent staying with one "
  "hard thing, which a summary is built to remove. My prediction is that students who learn "
  "from a twenty-card deck grow into customers who expect every product to "
  "come pre-chewed. That habit moves from the classroom into the jobs, apps and "
  "media those students pick next.",
 ]),

 ("The revolt has started", [
  "I am not the only one who wants out. In Pew&rsquo;s April 2025 survey of "
  f"1,391 teenagers, <a href=\"{PEW_TEENS}\">44% said they had cut back</a> on "
  "social media, and the same share said they had cut back on their phones. "
  f"By March, 33 states had <a href=\"{BANS}\">enacted K-12 cellphone "
  "bans</a>, five of them this year. Teenagers are cutting back on their own, "
  "and legislators are cutting back for them.",

  "Companies are starting to sell the exit. On 22 October, Brick launched "
  f"<a href=\"{BRICK}\">Brick Night</a>, a $129 device that blocks the apps you "
  "choose once your phone enters the bedroom. Its whole job is to make a "
  "smartphone do less. Print book sales were flat through "
  f"early October, and crafts, hobbies and games <a href=\"{BOOKS}\">rose "
  "17.4%</a> while self-help fell 23%, according to Circana. My reading is that "
  "people are buying things that keep their hands busy and their phones in "
  "another room.",
 ]),

 ("Who wins the slow hit", [
  "My prediction is that slowness becomes a premium product. Long-form writing, "
  "physical books, phones that do less and apps that end on purpose will charge "
  "more than the feeds, because the scarce thing in 2026 is an hour that "
  "nothing interrupts.",

  "My second prediction is that the platforms that sell the fast hit will buy "
  "the slow one. A company like Brick, a reading app or a focus tool is a "
  "natural acquisition for a phone maker or a streamer that wants to keep its "
  "users from leaving altogether. Even Huxe pointed this way. A briefing that "
  "covers your morning and then ends is a fast product that sells calm, and "
  "my guess is that is part of why Apple wanted the team.",

  "I am betting on the revolt because I feel it myself. I want to read one long "
  "thing and finish it, and I think a lot of people my age want the "
  "same.",
 ]),

 ("What would prove me wrong", [
  "If time spent per view keeps falling while the share of teens cutting back "
  "stops rising, the fast hit is still winning. If phone bans are rolled back, "
  "or Brick-style devices stay a niche, the revolt stays a mood that nobody "
  "has found a way to sell to.",
 ]),
]

NOTE = ("YouTube figures come from Tubular Labs as reported by TVREV and from "
        "Metricool&rsquo;s sample of accounts using its tools, so they describe "
        "those samples. I found no dataset showing average "
        "upload length falling. Apple did not buy Huxe outright: the EU filing "
        "covers job offers and a non-exclusive license, and terms were not "
        "disclosed. StudyStash terms were not disclosed. Pew&rsquo;s "
        "AI-summary data is from March 2025. Book figures are Circana BookScan as "
        "reported by Publishers Weekly. Statements marked as predictions are mine.")
