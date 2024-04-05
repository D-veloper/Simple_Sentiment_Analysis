from textblob import TextBlob
from newspaper import Article

urls = ['https://en.wikipedia.org/wiki/Mathematics', 'https://www.slashgear.com/1532293/ai-horror-stories-serious-threat/', 'https://www.goodnewsnetwork.org/livin-good-currency-shari-alyse-on-grounding-expectations-for-oneself-and-others-in-humanity-not-idealism/']  # link to articles

for url in urls:
    article = Article(url)  # transform link with article into an article object

    article.download()  # get the article into this script
    article.parse()  # remove the html elements so article is more readable
    article.nlp()  # preparing article for natural language processing

    text = article.summary  # extract a summary of the article. ".text" for full text
    print(text)

    blob = TextBlob(text)  # create a text blob to perform sentiment analysis on from the text
    sentiment = blob.sentiment.polarity  # scores it from extremely negative to extremely positive sentiment -1 to 1.

    print(sentiment)

# text = '''
# At the center of the legendary Terminator film series is Skynet, an AI-powered system that controls the United States government's arsenal of nuclear weapons. In the films, Skynet became self-aware, determined that the entire human race was the greatest threat to its existence, and decided to launch a nuclear war to eradicate them. Skynet isn't real, but in 2024, the market for AI-powered applications is booming at an astonishing rate. It hasn't progressed to the point of being self-aware, much less being trusted to safeguard the U.S. military's nuclear arsenal, though "optionally manned" nuclear-capable aircraft have been explored as a future possibility. But its rapid deployment has exposed many aspects of the most popular AI apps as not yet being ready for prime time.
#
# AI image generators and large language models arguably infringe on copyrights, and safeguards designed to prevent the image generators from being used to create non-consensual, violent, or sexually explicit imagery of real people have failed. Data sets have been trained irresponsibly and could result in image generators stitching together elements of actual child abuse imagery. ChatGPT is often wrong about factual matters, even when logic dictates that it shouldn't be, like when asked to summarize a provided document. And good old human error has introduced various other issues, particularly when the user doesn't quite understand exactly what ChatGPT is or how it works.
#
# With all of that in mind, let's take a look at a few examples of how messy the AI landscape has already become in less than two years since the original public release of ChatGPT started driving widespread public use of the technology.
#
# Perhaps the most surface-level distressing piece of software to reach critical mass in the recent AI boom involves AI-generated images. Whether using mainstream generative AI image creation apps like DALL-E and Stable Diffusion or the myriad of "deepfake" apps that can allow you to swap faces on existing photos or videos with shocking levels of realism, it's easy to see how bad actors can harness the technology. The main concerns involve the spread of disinformation or, more commonly, non-consensual nude and/or explicit imagery.
#
# In January 2024, explicit deepfakes of Taylor Swift spread like wildfire across major social media platforms. According to a report from Media, the images were first circulated on the famously anything-goes 4chan image board as well as a Telegram group devoted to "abusive images of women." Complicating matters, as 404 Media further reported, was that the images were created using Image Creator by Microsoft Designer, the former Bing Image Generator, which is based on DALL-E. Though the AI web app had safeguards in place, there were loopholes, like misspelled celebrity names, that were soon patched.
#
# Though major celebrities are the most obvious targets, lower-profile public figures and even private citizens aren't necessarily safe from Deepfakes. The extra attention from the Swift story, though, has led a bipartisan trio of U.S. Senators to introduce a bill, the Disrupt Explicit Forged Images and Non-Consensual Edits Act, that would allow victims to sue the creators and distributors of their deepfakes with a 10-year statute of limitations.
#
# Making matters worse with the story of the Taylor Swift deepfakes created using Image Creator by Microsoft Designer is that, reportedly, that mess was entirely preventable. According to a January 2024 Geekwire report, Shane Jones, a Microsoft AI engineer, wrote an email to the Washington State Attorney General and his Congressional representatives outlining how both Microsoft and OpenAI had largely ignored his pleas to fix the loophole that allowed the creation of non-consensual explicit images.
#
# In a statement, Microsoft told Geekwire that the workarounds Jones found didn't "bypass our safety filters," but they told him to report his concerns to OpenAI regardless, which he took issue with in a follow-up. "We monitor Microsoft corpnet and Microsoft user accounts for cyber security threats," reads the Microsoft response to Jones's threat report that he shared with Geekwire. "This report doesn't seem to be impacting any of the above. I would suggest you to submit feedback over Open AI website. I am proceeding with case closure."
#
# When Jones posted publicly to try to get OpenAI to recall DALL-E 3 until the issue was fixed, Microsoft demanded he delete the post, he says, but they never explained why. For their part, OpenAI, when reached by Geekwire, claimed that they "immediately investigated the Microsoft employee's report when we received it" and later "confirmed that the technique he shared does not bypass our safety systems."
#
# Realistically, AI image-generation apps are simply stitching together images that the AI was trained on. This could cause all sorts of exposure for those involved if the training data was poisoned by data like child sexual abuse imagery, or CSAM for short. Sure enough, in December 2023, a Stanford Cyber Policy Center investigation revealed that LAION-5B, a public image data set used to train AI — including Stable Diffusion and Midjourney — was trained on known instances of CSAM.
#
# Stanford found the CSAM using file hashing tools like Microsoft's PhotoDNA, which checks against the databases of known CSAM held by the National Center for Missing and Exploited Children in the U.S. and the Canadian Centre for Child Protection. This allowed them to detect the known CSAM without exposing researchers to illegal images.
#
# In a full paper on the matter by Stanford's David Thiel, Thiel notes that "We have previously proposed that models trained on erotic content not be trained on material depicting children [because] this limits the ability of models to conflate the two types of material." He further argued that it might be wise to exclude images of children from these data sets more broadly. Reached by Forbes, a spokesman for Stable Diffusion's parent company, Stability AI committed to "preventing the misuse of AI and prohibit the use of our image models and services for unlawful activity" but didn't offer up details. Midjourney did not respond to Forbes' inquiries.
#
# One problem with AI large language models like the one at the heart of ChatGPT is that they don't really understand how facts work and thus don't always tell the truth. Microsoft Copilot, formerly Bing Chat, which is based on ChatGPT, leverages Bing search to give fully annotated responses with links to source almost every claim, but that's all Microsoft's doing, not something that OpenAI built into ChatGPT. This has the potential to get ugly, and, in fact, it already has.
#
# In April 2023, the Washington Post reported on the plight of George Washington University law professor Jonathan Turley. A colleague had, as an experiment, asked ChatGPT to list law professors who had been accused of sexual harassment, and Turley's name was on there, with the chatbot citing the Washington Post. The article didn't exist, though, and neither did the allegation. He wasn't alone: Georgia radio host Mark Walters sued OpenAI for defamation in the Superior Court of Gwinnett County in June 2023. When prompted by a reporter to summarize an unrelated lawsuit, ChatGPT accused him of embezzling from the Second Amendment Foundation. Even when the reporter asked for the full text of the complaint that he included the URL of, ChatGPT spit out unrelated nonsense defaming Walters, even making up a fake case number.
#
# And there are others, too, like an Australian mayor falsely accused of bribery. Or the columnist and political cartoonist, Ted Rall, who was falsely accused of plagiarizing his best friend. Until ChatGPT becomes more like Copilot, this is going to happen again and again.
#
# The above-mentioned problem with faux court case citations has crossed over into actual cases, thanks at least in part to lawyers not quite understanding what ChatGPT is. One lawyer, Steven A. Schwartz, became infamous in June 2023 when he faced possible sanctions for citing imaginary, ChatGPT-generated caselaw in his pleadings. Essentially, he admitted that he had misunderstood what the chatbot was, thinking it was a souped-up search engine, and not a language model that could make up fake citations out of whole cloth.
#
# Later in 2023, a recent law school graduate named Zachariah Crabill recounted his plight to the Washington Post. Overworked, he had ChatGPT write a motion for him, filed it himself, and then realized once it was too late that the motion was filled with imaginary citations. Another young lawyer at an eviction law-centric firm had a similar story, with both of them being fined as a result.
#
# It just keeps going, as a Long Island-based lawyer, Jae Lee, was reported by Bloomberg Law to be facing possible sanctions in January 2024 for citing yet another fake piece of case law. "I am committed to adhering to the highest professional standards and to addressing this matter with the seriousness it deserves," wrote Lee when she was reached for comment. She declined to answer any further questions "given the confidential nature of the disciplinary proceedings."
#
# Hopefully, an increased understanding of what ChatGPT is will limit how often this happens going forward.
#
# There are already multiple lawsuits in play alleging that ChatGPT and the AI image generators infringe on the copyrights of existing works. In July 2023, actress and comedienne, Sarah Silverman, sued OpenAI for training the LLM that powers ChatGPT on her book, "The Bedwetter," and appears to pull directly from it when asked to summarize its contents. As of February 2024, parts of the lawsuit have been dismissed, with the judge saying that the plaintiffs did not prove direct infringement.
#
# In February 2023, artists filed a class action lawsuit against Stability AI for training Stable Diffusion on datasets that included their work, with Getty Images having filed a similar lawsuit a few weeks earlier.
#
# In December 2023, the New York Times sued OpenAI and Microsoft in an exhaustively annotated complaint showing many examples of how the LLM was trained on millions of Times articles and often copied them verbatim. In addition to monetary damages, the Times is seeking injunctive relief, "Ordering destruction under 17 U.S.C. § 503(b) of all GPT or other LLM models and training sets that incorporate Times Works." A January 2024 analysis at The Conversation deemed such a result feasible if the case went that far, albeit expecting a settlement to be more likely. This just scratches the surface, as there are also other lawsuits like the Authors Guild suing OpenAI on similar grounds, but the Times suit is potentially the most dangerous one for AI companies.
#
# In May 2023, a Reddit post on the /r/ChatGPT subreddit went viral. Why? It showed an email where a Texas A&M University-Commerce professor, Dr. Jared Mumm, was on the verge of failing every single student in one of his senior classes because he believed that the students had all used "Chat GTP" to write their final papers. "In Grading your last three assignments I have opened my own account for Chat GTP," he wrote. "I copy and paste your responses in this account and Chat GTP will tell me if the program generated the content. I put everyone's last three assignments through two separate times and if they were both claimed by Chat GTP you received a 0."
#
# One problem with that: ChatGPT has no way of detecting if a piece of writing was written by ChatGPT.
#
# A university spokesperson confirmed to NBC News that the email was genuine, but disputed the characterization of the situation in the Reddit post, saying that no students had gotten failing grades or had their graduation blocked by the incident. "[S]everal students have been exonerated and their grades have been issued, while one student has come forward admitting his use of Chat GTP in the course," wrote the spokesperson in a statement. "Several other students have opted to complete a new writing assignment made available to them by Dr. Mumm." For his part, Mumm never commented himself, though.
# '''


