# Analysis and Visualization of Supreme Court Oral Arguments
### Metis Project 4 - NLP - Brian Newborn  

#### Readme

For our fourth project during the Metis NYC Spring Bootcamp, we went over the tools necessary to analyze text and extract topics from hundreds of thousands of data points. Since I am particularly interested in increasing transparency of our government, I decided to analyze the Supreme Court's oral arguments. I figured that understanding these could help with (not limited to):
* Predicting judgments
* Understanding how each justice approaches different types of legal cases
* Identifying what types of cases the Supreme Court works on during a session

Ultimately, my analysis struggled to extract topics from cases, but after many attempts I was able to do so. This was also my first work in NLP/topic analysis, and since then I've definitely gotten more comfortable with tools like Gensim, TextBlob and related visualization aspects (t-SNE especially).

This is a distilled version of my data pipeline but is saved here in a few files

* 1_scrape.ipynb: this code reflects using the OYEZ API to extract over 100,000 cases from 2000-2018. These were cleaned and entered into a MongoDB to allow for flexibility and data adjustments afterwards.
* 2_textclean.ipynb: here I used tools like TextBlob and Lemmatization to clean the informal and somewhat repetitive text of oral arguments. These steps dramatically increase the effectiveness of topic analysis later on
* 3_topics_tsne.ipynb: finally, using the cleaned text, I ran Latent Direchlet Allocation steps (using Count Vectorizer of all words as input) to extract 30 topics from our body of text. I also used t-SNE to visualize these topics into meaningful clusters. This data was pickled and ultimately the basis of the visualization I presented in class. This visualization will be uploaded shortly and the link added to this readme as soon as possible.
* the **oyez_api** folder were functions designed by Ben Musch (with a few personal additions for this project by me)
  [Ben's Page](https://github.com/BenMusch/oyez-api-python/blob/master/oyez_api/__init__.py)

Please let me know if you have any questions, thanks for reading!
