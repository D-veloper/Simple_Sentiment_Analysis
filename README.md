# Simple Sentiment Analysis

## Introduction
This project aims to conduct sentiment analysis on articles sourced from various websites. Leveraging Python and natural language processing techniques, the sentiment of the articles is evaluated on a scale from -1 (extremely negative) to 1 (extremely positive).

---

### Skills Developed:

**Hard Skills:**
- **Python Programming**: Utilized Python for implementing sentiment analysis.
- **Natural Language Processing (NLP)**: Employed NLP techniques for sentiment analysis using NLTK and TextBlob libraries.
- **Web Scraping**: Extracted article content from websites using the Newspaper library.
- **Debugging**: Troubleshot errors encountered during code execution.
- **Problem Solving**: Addressed challenges related to library dependencies and script execution.

**Soft Skills:**
- **Attention to Detail**: Recognized nuances in text processing and analysis.
- **Critical Thinking**: Evaluated the effectiveness and limitations of sentiment analysis.
- **Adaptability**: Adjusted the approach based on observed outcomes and errors encountered.
- **Communication**: Articulated observations and conclusions in a clear manner.

### Libraries Used
- **NLTK**: A foundational library for NLP tasks in Python.
- **TextBlob**: Utilized for performing sentiment analysis.

---

### Approach
1. **Article Selection**: Articles were chosen from diverse sources including Wikipedia and news websites to capture different tones and subjects.
2. **Text Extraction**: The articles were retrieved using the Newspaper library, and their content was extracted for analysis.
3. **Summarization**: To streamline analysis and easily remove boilerplate content (e.g. generic headings like "See also", "Notes", "References" e.t.c), article summaries were used instead of full texts.
4. **Sentiment Analysis**: TextBlob was employed to analyze the sentiment polarity of each article summary, assigning a score between -1 and 1.

---

### Observations
- **Error Resolution**: Initially encountered an ImportError, necessitating the installation of an additional library, lxml-html-clean, to handle HTML parsing.
- **Content Filtering**: While the article.parse() method effectively removed the body of the boilerplate content, the headings themselves persisted. So I opted for summarization as an alternative to mitigate irrelevant content and streamline analysis. However, I noted how this might affect the accuracy of the analysis and performed tests to confirm this.
- **Sentiment Discrepancies**: Initial sentiment scores differed from personal expectations, prompting further investigation.
    - **Discrepancy in Perceived Negative AI Article**: I was surprised that the sentiment analysis score of the AI article was not lower, despite the negative content.

      The initial summary and score of the article was this:
      
      *Summary: "These Horror Stories Prove That AI Could Pose A Serious Threat
      At the center of the legendary Terminator film series is Skynet, an AI-powered system that controls the United States government's arsenal of nuclear weapons.
      In the films, Skynet became self-aware, determined that the entire human race was the greatest threat to its existence, and decided to launch a nuclear war to eradicate them.
      Skynet isn't real, but in 2024, the market for AI-powered applications is booming at an astonishing rate.
      AI image generators and large language models arguably infringe on copyrights, and safeguards designed to prevent the image generators from being used to create non-consensual, violent, or sexually explicit imagery of real people have failed.
      Data sets have been trained irresponsibly and could result in image generators stitching together elements of actual child abuse imagery."*

      score: 0.13435374149659868

      I ran the script with the full text and observed a slightly lower score (0.1089795918367347), indicating the limitations of summaries in representing the true sentiment.

    - **Refinement of Analysis**: By printing out the full text, I noticed that every subheading in the AI article was cut, potentially influencing the sentiment score. To verify this, I manually loaded the full
      article into the script and reran the analysis, resulting in a score closer to personal expectations, albeit still leaning slightly positive (0.06818075715134536). 

---

### Insights

- **Limitations of Summarization**: Summarized articles may inadequately capture the nuanced sentiments present in the original text, leading to possible discrepancies in sentiment analysis results. So one must be cautious to acknowledge the inherent limitation when relying solely on article summaries for sentiment assessment.

- **Contextual Importance**: I understand that TextBlob "calculates average polarity and subjectivity over each word in a given text using a dictionary of adjectives and their hand-tagged scores." [see here](https://stackoverflow.com/questions/43688542/textblob-sentiment-algorithm). While this is a great start, a model  that pays attention to keywords and lacks contextual understanding will struggle to accurately capture nuance. As a result, its sensitivity will be sort of directly proportional to the degree of extreme sentiment in the sentences. So its more accurate the more extreme the sentiment is and vise versa. One should also keep this limitation in mind.

---

### Conclusion
This simple project was my first step to exploring the complexities involved in sentiment analysis. I learnt the importance of context, content representation, and model accuracy as well as how to perform a very simple sentiment analysis.
