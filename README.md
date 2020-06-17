# Sentiment-Analysis-of-Reviews
A program to analyze user reviews of the movie: "Avengers: Endgame" </br>
</br>
The program starts off with crawling user reviews from https://www.imdb.com/title/tt4154796/reviews?ref_=tt_ql_3 </br>
with the help of BeautifulSoup. The crawled data are classified under 'Scores', 'Title', 'Writer', 'Date' and 'Content'.
</br></br>
The class under consideration is the 'Content'. The review content is tested for sentiment analyzing, with the help of 
SentimentIntensityAnalyzer from nltk.sentiment.vader. </br> Each reviews on the page are tested for sentiment analysis,
and those with negative sentiment intensities are grouped for further analysis.</br>
</br>
The project was implemented with the aim to discover whether it is possible to extract the 'keywords' in negative reviews
in order to pinpoint the problem of the movie. For example, if someone did not like the movie as he or she thinks that
there are less action scenes, a possible keyword could be 'action'. </br>
</br>
Hence review contents with negative sentiment intensities were implemented with LSA (Latent Semantic Analysis), in order
to extract words with the most relevance in a sentence. Each review was tokenized into sentences, and further into words.
Document Term Matrix was created from each review, and through LSA, with truncated value of 2 (k=2), each sentence was matched
to a most relevant word, and the words were grouped for each review as a whole. </br>
</br>
Although the project seemed hypothetically reasonable, there were definitely parts to improve, as although stopwords were
taken into account, the keywords extracted hardly could tell much about each sentence in a review. Possible improvements
could be extraction or generation of key sentences, which would tell more about the whole review.
